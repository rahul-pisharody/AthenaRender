import sys, os
#testing_alpha

#Change Current Working directory to Path of Script
to_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(to_dir)
current_dir = os.getcwd()

#Find the Blender executable
list_dir = [d for d in os.listdir('.') if ((os.path.isdir(d)) and (not d.startswith('.')))]
print (list_dir)

for directory in list_dir:
    if ('blender' in os.listdir(directory)):
        to_dir = directory
        break
else:
    print('Blender executable not found')
    sys.exit()

#Check for Arguments
try:
    name = str(sys.argv[1])
    anim = str(sys.argv[2])
except:
    print('Usage: python render.py <name> <anim (0/1)>')
    sys.exit()

#Set Cycles Sampling
try:
    sampling = str(sys.argv[3])
except:
    sampling = str(300)

os.system(to_dir+'/blender -b \"' +name+'\" -o //renders/'+os.path.basename(os.path.splitext(name)[0])+' -P RenderSettings.py -- '+anim+' '+sampling)
