#!/usr/bin/python
import os,sys
name = sys.argv[1]
usr = sys.argv[2]
passwd = sys.argv[3]
from_path = name
to_path = name
os.system('sshpass -p '+passwd+' scp '+name+' '+usr+'@192.168.40.99:'+to_path)
os.system('sshpass -p '+passwd+' ssh -o StrictHostKeyChecking=no '+usr+'@192.168.40.99 "screen -d -m -L nice python render.py '+to_path+' 0"')
