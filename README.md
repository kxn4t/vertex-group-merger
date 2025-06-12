# Vertex Group Merger
## Overview
This is a Blender addon for merging multiple vertex groups into a single target group. Weights can be merged using additive or subtractive methods, and there are options to adjust the total weight and preserve source groups.  
You can quickly merge vertex groups without having to set up multiple Vertex Weight Mix modifiers.

## Features
- **Additive Mode**: Add weights from source groups to the target group
- **Subtractive Mode**: Subtract weights from source groups from the target group
- **Weight Control**: Option to maintain total weight ≤ 1.0
- **Group Preservation**: Option to keep source groups after merging
- **Range Selection Mode**: Efficiently select multiple vertex groups using range selection

## How to Use
1. Select a mesh object with vertex groups
2. Open the "Edit" tab in the 3D View side panel (press N to display)
3. Select the target vertex group in "Target Group"
4. Choose the operation mode (Add or Subtract) using the radio buttons
5. Select the source vertex groups from the list
6. Set the "Maintain Total Weight ≤ 1.0" option if needed
7. Set the "Keep Source Groups" option if you want to preserve the source groups
8. Click the "Merge Selected Groups" button

## Operation Modes
- **Add**: Source group weights are added to the target group weights (default behavior)
- **Subtract**: Source group weights are subtracted from the target group weights
  - Vertices with resulting zero weight will be automatically removed from the target group

## Options
- **Maintain Total Weight ≤ 1.0**: Ensures the final vertex weights don't exceed 1.0
- **Keep Source Groups**: Preserves source groups after the merge operation (they won't be deleted)

## Range Selection Mode
Range Selection Mode allows you to efficiently select multiple vertex groups at once.

### How to Use
1. **Enable Range Selection Mode**: Check the "Range Selection Mode" checkbox above the source groups list
2. **Select Start Point**: Click the checkbox of the first vertex group in your desired range
3. **Select End Point**: Click the checkbox of the last vertex group in your desired range
4. **Result**: All vertex groups between the start and end points will be set to the same state (ON/OFF) as the last clicked checkbox

### Examples
- **To turn ON a range**: Click Group_01 (OFF→ON), then click Group_05 (OFF→ON). Result: Group_01 through Group_05 will all be turned ON
- **To turn OFF a range**: Click Group_03 (ON→OFF), then click Group_07 (ON→OFF). Result: Group_03 through Group_07 will all be turned OFF

### Auto-Reset Features
- **Object Change**: Range Selection Mode is automatically disabled when you select a different object
- **After Merge**: Range Selection Mode is automatically disabled after completing a merge operation

## Requirements
Blender 3.6.0 or higher

## Installation
1. Open Blender's "Edit" → "Preferences" → "Add-ons"
2. Click the "Install" button
3. Select the downloaded `vertex_group_merger.zip`
4. Enable "Vertex Group Merger" in the addon list

## License
GPL v3 License (see LICENSE). Free for both personal and commercial use.