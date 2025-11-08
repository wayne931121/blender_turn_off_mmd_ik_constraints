import bpy
# Attribution 4.0 International
# Copyright (c) 2025 wayne931121
# Source https://github.com/wayne931121/blender_turn_off_mmd_ik_constraints
for name,pbone in bpy.context.selected_objects[0].pose.bones.items():
        for c in pbone.constraints:
            if c.type!="IK":
                pass
            else:
                c.enabled = 0
