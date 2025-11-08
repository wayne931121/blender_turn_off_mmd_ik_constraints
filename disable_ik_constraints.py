"""
    Disable IK Constraints in Blender
    Copyright (c) 2025 wayne931121

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
"""
For More Infomation, Please Visit:
    Source https://github.com/wayne931121/blender_turn_off_mmd_ik_constraints

About Me:
    Hi, I'am a student currect study in National Yunlin University of Science and Technology.
"""
import bpy

for name,pbone in bpy.context.selected_objects[0].pose.bones.items():
        for c in pbone.constraints:
            if c.type!="IK":
                pass
            else:
                c.enabled = 0
