import bpy
from bpy.props import (
    BoolProperty,
    StringProperty,
    CollectionProperty,
    PointerProperty,
)
from bpy.types import Operator, Panel, PropertyGroup, UIList, Object, VertexGroup
from typing import List, Dict, Set, Optional, Any

bl_info = {
    "name": "Vertex Group Merger",
    "author": "kxn4t",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Edit Panel > Vertex Group Merger",
    "description": "Merge multiple vertex groups into a target group",
    "category": "Mesh",
}


class MESH_OT_merge_vertex_groups(Operator):
    """Merge selected vertex groups into specified target group"""

    bl_idname = "mesh.merge_vertex_groups"
    bl_label = "Merge Vertex Groups"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context) -> bool:
        obj = context.active_object
        return obj and obj.type == "MESH" and len(obj.vertex_groups) > 1

    def execute(self, context) -> Set[str]:
        obj: Object = context.active_object
        settings = context.scene.vertex_group_merger

        # Get target group
        target_group_name: str = settings.target_group
        target_group: Optional[VertexGroup] = obj.vertex_groups.get(target_group_name)

        if not target_group:
            self.report({"ERROR"}, "Target group not found")
            return {"CANCELLED"}

        # Get source groups
        source_group_names: List[str] = [
            group.name for group in settings.source_groups if group.use
        ]

        if not source_group_names:
            self.report({"ERROR"}, "No source groups selected")
            return {"CANCELLED"}

        source_groups: List[VertexGroup] = [
            obj.vertex_groups.get(name) for name in source_group_names
        ]

        # Perform merge operation
        self.merge_vertex_groups(
            obj,
            source_groups,
            target_group,
            settings.maintain_total_weight,
            settings.keep_source_groups,
        )

        # Update list
        update_source_groups(self, context)

        return {"FINISHED"}

    def merge_vertex_groups(
        self,
        obj: Object,
        source_groups: List[VertexGroup],
        target_group: VertexGroup,
        maintain_total_weight: bool,
        keep_source_groups: bool,
    ) -> None:
        """
        Merge source vertex groups into target group

        Args:
            obj: Object containing vertex groups
            source_groups: List of source vertex groups to merge
            target_group: Target vertex group to merge into
            maintain_total_weight: Flag to keep total weight ≤ 1.0
            keep_source_groups: Flag to keep source groups after merging
        """
        # Pre-compute set of vertices to process
        vertices_to_process: Set[int] = self._collect_vertices_to_process(
            obj, source_groups, target_group
        )

        # Calculate weights for each vertex
        vertex_weights: Dict[int, float] = self._calculate_vertex_weights(
            vertices_to_process, source_groups, target_group, maintain_total_weight
        )

        # Apply new weights to target group
        for vertex_index, weight in vertex_weights.items():
            target_group.add([vertex_index], weight, "REPLACE")

        # Save source group names before deletion
        source_names: List[str] = [group.name for group in source_groups]

        # Remove source groups (only if keep_source_groups is False)
        if not keep_source_groups:
            for group in reversed(source_groups):
                obj.vertex_groups.remove(group)

        # Report success
        success_message = f"{', '.join(source_names)} merged into {target_group.name}"
        if keep_source_groups:
            success_message += " (source groups kept)"
        self.report({"INFO"}, success_message)

    def _collect_vertices_to_process(
        self, obj: Object, source_groups: List[VertexGroup], target_group: VertexGroup
    ) -> Set[int]:
        """Collect vertices that need processing from all groups"""
        vertices_to_process: Set[int] = set()

        # Add vertices from target group
        for v in obj.data.vertices:
            try:
                target_group.weight(v.index)
                vertices_to_process.add(v.index)
            except RuntimeError:
                pass

        # Add vertices from source groups
        for source_group in source_groups:
            for v in obj.data.vertices:
                try:
                    source_group.weight(v.index)
                    vertices_to_process.add(v.index)
                except RuntimeError:
                    pass

        return vertices_to_process

    def _calculate_vertex_weights(
        self,
        vertices_to_process: Set[int],
        source_groups: List[VertexGroup],
        target_group: VertexGroup,
        maintain_total_weight: bool,
    ) -> Dict[int, float]:
        """Calculate new weights for vertices"""
        vertex_weights: Dict[int, float] = {}

        for vertex_index in vertices_to_process:
            # Start with target weight (0.0 if not in target group)
            weight: float = 0.0
            try:
                weight = target_group.weight(vertex_index)
            except RuntimeError:
                pass

            # Add weights from source groups
            for source_group in source_groups:
                try:
                    weight += source_group.weight(vertex_index)
                except RuntimeError:
                    pass

            # Clamp weight if needed
            if maintain_total_weight and weight > 1.0:
                weight = 1.0

            vertex_weights[vertex_index] = weight

        return vertex_weights


class VertexGroupItem(PropertyGroup):
    """Source vertex group item"""

    name: StringProperty(name="Name", default="")
    use: BoolProperty(name="Use", default=False)


class MESH_UL_merge_source_groups(UIList):
    """Source vertex groups list UI"""

    def draw_item(
        self,
        context,
        layout,
        data,
        item,
        icon,
        active_data,
        active_propname,
        index: int,
    ) -> None:
        if self.layout_type not in {"DEFAULT", "COMPACT"}:
            layout.alignment = "CENTER"
            layout.prop(item, "use", text="")
            return

        # Default layout handling
        row = layout.row()
        is_checked: bool = item.use
        icon_value: str = "CHECKBOX_HLT" if is_checked else "CHECKBOX_DEHLT"
        row.prop(item, "use", text="", icon=icon_value, emboss=False)
        row.label(text=item.name)


# List selection handler
class MESH_OT_select_source_group_list_item(Operator):
    """Handle selection in the source group list"""

    bl_idname = "mesh.select_source_group_list_item"
    bl_label = "Select Source Group List Item"
    bl_options = {"REGISTER", "UNDO", "INTERNAL"}

    def execute(self, context) -> Set[str]:
        obj: Object = context.active_object
        settings = context.scene.vertex_group_merger

        # Get current selected item index
        index: int = settings.active_source_index

        if index < 0 or index >= len(settings.source_groups):
            return {"FINISHED"}

        selected_name: str = settings.source_groups[index].name

        # Find that group in standard list and make it active
        for i, vg in enumerate(obj.vertex_groups):
            if vg.name == selected_name:
                obj.vertex_groups.active_index = i
                break

        return {"FINISHED"}


# Callback when checkbox is changed to update standard list
def item_use_update(self, context) -> None:
    """Update standard list when checkbox is changed"""
    obj: Optional[Object] = context.active_object
    if not obj or obj.type != "MESH":
        return None

    # Make corresponding group active when checked
    if not self.use:
        return None

    for i, vg in enumerate(obj.vertex_groups):
        if vg.name == self.name:
            obj.vertex_groups.active_index = i
            break

    return None


class VertexGroupMergerSettings(PropertyGroup):
    """Vertex Group Merger Settings"""

    source_groups: CollectionProperty(type=VertexGroupItem)
    active_source_index: bpy.props.IntProperty(
        update=lambda self, context: bpy.ops.mesh.select_source_group_list_item()
    )

    target_group: StringProperty(
        name="Target Group",
        description="Selected groups will be merged into this group",
        default="",
    )

    maintain_total_weight: BoolProperty(
        name="Maintain Total Weight ≤ 1.0",
        description="Adjust merged weights so total does not exceed 1.0",
        default=False,
    )

    keep_source_groups: BoolProperty(
        name="Keep Source Groups",
        description="Keep source groups after merging (do not delete them)",
        default=False,
    )


def update_source_groups(self, context) -> None:
    """Update source groups list"""
    obj: Optional[Object] = context.active_object
    if not obj or obj.type != "MESH":
        return

    settings = context.scene.vertex_group_merger

    # Clear existing list
    settings.source_groups.clear()

    # Add all vertex groups except current target to the list
    for vg in obj.vertex_groups:
        if vg.name == settings.target_group:
            continue

        item = settings.source_groups.add()
        item.name = vg.name
        item.use = False


class VIEW3D_PT_vertex_group_merger(Panel):
    """Vertex Group Merger Panel"""

    bl_label = "Vertex Group Merger"
    bl_idname = "VIEW3D_PT_vertex_group_merger"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Edit"

    _prev_active_object: Optional[Object] = None

    @classmethod
    def poll(cls, context) -> bool:
        # Check if active object changed
        if cls._prev_active_object != context.active_object:
            cls._prev_active_object = context.active_object
            # Update vertex group list when active object changes
            if (
                context.active_object
                and context.active_object.type == "MESH"
                and hasattr(context.active_object, "vertex_groups")
            ):
                bpy.app.timers.register(
                    lambda: update_source_groups(cls, context), first_interval=0.1
                )

        return (
            context.object
            and context.object.type == "MESH"
            and len(context.object.vertex_groups) > 1
        )

    def draw(self, context) -> None:
        layout = self.layout
        settings = context.scene.vertex_group_merger
        obj: Object = context.active_object

        # Target group selection
        row = layout.row()
        row.prop_search(
            settings,
            "target_group",
            context.active_object,
            "vertex_groups",
            text="Target Group",
        )

        # Source groups list
        box = layout.box()
        box.label(text="Select Source Groups")

        row = box.row()

        # Draw UI list
        row.template_list(
            "MESH_UL_merge_source_groups",
            "",
            settings,
            "source_groups",
            settings,
            "active_source_index",
            rows=5,
        )

        # Options
        row = layout.row()
        row.prop(settings, "maintain_total_weight")

        row = layout.row()
        row.prop(settings, "keep_source_groups")

        # Merge button
        row = layout.row()
        row.scale_y = 1.5
        row.operator("mesh.merge_vertex_groups", text="Merge Selected Groups")
        row.enabled = bool(settings.target_group)

        # Toggle weight paint mode button
        if obj.mode == "WEIGHT_PAINT":
            return

        row = layout.row()
        row.operator("paint.weight_paint_toggle", text="Switch to Weight Paint Mode")


def target_group_update(self, context) -> None:
    """Update source list when target group changes"""
    update_source_groups(self, context)


# Class registration/unregistration
classes: List[Any] = [
    VertexGroupItem,
    MESH_UL_merge_source_groups,
    MESH_OT_select_source_group_list_item,
    VertexGroupMergerSettings,
    MESH_OT_merge_vertex_groups,
    VIEW3D_PT_vertex_group_merger,
]


def register() -> None:
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add callback for target group selection change
    VertexGroupMergerSettings.target_group = StringProperty(
        name="Target Group",
        description="Selected groups will be merged into this group",
        default="",
        update=target_group_update,
    )

    # Set callback for checkbox change
    VertexGroupItem.use = BoolProperty(
        name="Use",
        default=False,
        update=item_use_update,
    )

    bpy.types.Scene.vertex_group_merger = PointerProperty(
        type=VertexGroupMergerSettings
    )


def unregister() -> None:
    del bpy.types.Scene.vertex_group_merger

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
