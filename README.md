# blender_turn_off_mmd_ik_constraints
Attribution 4.0 International,  Copyright (c) 2025 wayne931121.

```py
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
```
<img alt="image" src="https://github.com/user-attachments/assets/d4e72319-c4df-43a1-8007-d89a4049950b" />
<img alt="image" src="https://github.com/user-attachments/assets/f366747d-7971-4323-a3d0-5c96aa5e0c3c" />

About Me:

Hi, I'am a student currect study in National Yunlin University of Science and Technology.

https://www.youtube.com/@%E5%B0%8F%E8%BE%B0%E7%9A%84%E7%AD%86%E8%A8%98%E6%9C%AC

https://open.spotify.com/artist/02lg6jqWmoc4BOTW2WGMzv?si=jwpzOggpSQ6Qq4VVa2io3A


