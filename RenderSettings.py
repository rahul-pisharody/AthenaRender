import bpy
import os,sys

argv = sys.argv
argv = argv[argv.index("--")+1:]
print (argv)
anim = argv[0]
sampling = int(argv[1])

out=bpy.path.basename(bpy.data.filepath)
print(out)
#changing scene name
Scenename = 'Scene'

#quality
bpy.data.scenes[Scenename].render.resolution_x = 1920
bpy.data.scenes[Scenename].render.resolution_x = 1080
bpy.data.scenes[Scenename].render.resolution_percentage = 100

#Cycles sampling
bpy.data.scenes[Scenename].cycles.samples = sampling

#output
#bpy.data.scenes[Scenename].render.filepath = '//renders/test'
bpy.data.scenes[Scenename].render.use_placeholder = True
bpy.data.scenes[Scenename].render.use_overwrite = False

#start render animation
if anim=='1':
    bpy.ops.render.render(animation=True,scene=Scenename)
else:
    bpy.ops.render.render(write_still=True)
