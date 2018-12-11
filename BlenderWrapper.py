import bpy
import mathutils
import random

from aux.pypredef import bpy

'''
Command History:     Up/Down Arrow
Cursor:              Left/Right Home/End
Remove:              Backspace/Delete
Execute:             Enter
Autocomplete:        Ctrl-Space
Zoom:                Ctrl +/-, Ctrl-Wheel
Builtin Modules:     bpy, bpy.data, bpy.ops, bpy.props, bpy.types, bpy.context, bpy.utils, bgl, blf, mathutils
Convenience Imports: from mathutils import *; from math import *
Convenience Variables: C = bpy.context, D = bpy.data








import bpy
import os

# Use your own script name here:
filename = "/Users/marcleonard/Projects/Blender_Scripts/BlenderWrapper.py"

filepath = os.path.join(os.path.dirname(bpy.data.filepath), filename)
global_namespace = {"__file__": filepath, "__name__": "__main__"}
with open(filepath, 'rb') as file:
    exec(compile(file.read(), filepath, 'exec'), global_namespace)

'''

objs = []




# bpy.ops.wm.read_factory_settings(use_empty=True)

class BlenderWrapper():
    def __init__(self):
        self.clean_workspace()
        self.run_setup()

        # bpy.context.scene.frame_start = 1

        self.frames = 300

        # bpy.context.scene.frame_end = 1 + self.frames

        self._set_frames()

    def clean_workspace(self):

        for obj in bpy.context.scene.objects:
            obj.select = True

            # blender 2.8
            #  obj.select_set(True)

            bpy.ops.object.delete(use_global=True)

    def run_setup(self):

        bpy.ops.object.camera_add(view_align=False, enter_editmode=False, location=(0, -400, 100),
                                  rotation=(0.0, 0.0, 0.0))

        c = bpy.context.active_object
        c.name = 'MainCamera'
        c.data.name = 'MainCamera'

        bpy.data.cameras['MainCamera'].type = 'ORTHO'

        # bpy.context.object.data.type = 'ORTHO'
        # bpy.context.object.data.ortho_scale = 200

        scene = bpy.context.scene

        currentcam = bpy.context.scene.camera

        setcam = False

        for ob in scene.objects:
            if ob.type == 'CAMERA':
                if ob == currentcam:
                    setcam = True
                elif setcam:
                    bpy.context.scene.camera = ob
                    break

        if currentcam == bpy.context.scene.camera:
            for ob in scene.objects:
                if ob.type == 'CAMERA':
                    bpy.context.scene.camera = ob
                    break

        for x in range(40):
            size = random.randint(1, 10)
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            z = random.randint(-50, 50)

            cube = bpy.ops.mesh.primitive_circle_add(radius=size, view_align=False, enter_editmode=False,
                                                     location=(x, y, z))

            aname = bpy.context.active_object.name
            objs.append(bpy.context.active_object.name)

    def _set_frames(self):
        for frame_num in range(self.frames):
            self.frame()

            self._set_keyframes(frame_num)

            # move to frame 17
            # bpy.ops.anim.change_frame(frame=frame_num+1)

    def _set_keyframes(self, frame_num):
        bpy.context.scene.frame_set(frame_num)
        for obj in bpy.context.scene.objects:
            obj.keyframe_insert(data_path='location', index=-1)

    def frame(self):
        for object in objs:
            print('getting obj: {}'.format(object))
            obj = bpy.data.objects[object]



            vec = mathutils.Vector((1, 1, 0))

            loc = obj.location

            # obj.update()

            n_loc = loc + vec

            print('{}->{}'.format(loc, n_loc))

            obj.location = n_loc


BlenderWrapper()

# https://code.blender.org/2015/10/debugging-python-code-with-pycharm/

# /Users/marcleonard/Downloads/blender-2.80.0-git20181204.1b6a394d862-x86_64/blender.app/Contents/MacOS/blender --python BlenderWrapper.py