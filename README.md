# Vertex Group Merger
## Overview
This is a Blender addon for merging multiple vertex groups into a single target group. Weights are merged using an additive method, and there's an option to adjust the total weight to not exceed 1.0.  
You can quickly merge vertex groups without having to set up multiple Vertex Weight Mix modifiers.

## How to Use
1. Select a mesh object with vertex groups
2. Open the "Edit" tab in the 3D View side panel (press N to display)
3. Select the target vertex group in "Target Group"
4. Select the source vertex groups from the list
5. Set the "Maintain Total Weight ≤ 1.0" option if needed
6. Click the "Merge Selected Groups" button

## Note
- Source groups will be deleted after the merge process

## Requirements
Blender 3.6.0 or higher

## Installation
1. Open Blender's "Edit" → "Preferences" → "Add-ons"
2. Click the "Install" button
3. Select the downloaded `vertex_group_merger.zip`
4. Enable "Vertex Group Merger" in the addon list

## License
GPL v3 License (see LICENSE). Free for both personal and commercial use.