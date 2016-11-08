import subprocess
import sys
import os
#testing
try:
    name = str(sys.argv[1])
    anim = str(sys.argv[2])
except:
    print('Usage: python render.py <name> <anim (0/1)>')
    sys.exit()

try:
    sampling = str(sys.argv[3])
except:
    sampling = str(300)

print(os.path.basename(os.path.splitext(name)[0]))
#print("""subprocess.run("blender -b \"" +name+"\" -o /renders/"+os.path.basename(name)+" -P RenderSettings.py")""")
os.system('blender-2.78a-linux-glibc211-x86_64/blender -b \"' +name+'\" -o //renders/'+os.path.basename(os.path.splitext(name)[0])+' -t 8 -P RenderSettings.py -- '+anim+' '+sampling)
