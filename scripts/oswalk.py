import os
import subprocess 

src = 'C:/Users/jhoov'
dest = 'C:/Users/jhoov/backup'
tasks = []

files = os.walk(src,topdown=True)

def rsync_call(source, destination):
    return ['rsync','-arq',source,destination]

directories = []
files = []
for root, _dirs, _files in os.walk(src,topdown=True):        
    for name in _files:
        source = os.path.join(root,name)
        destination = os.path.join(root.replace(src,dest),name)
        files.append(rsync_call(source,destination))

    for name in _dirs:
        source = os.path.join(root,name)
        destination = os.path.join(root.replace(src,dest),name)
        procs.append(rsync_call(source,destination))

print(len(files))

for proc in procs:
    subprocess.call(proc)


    #task = subprocess.call(proc)
    #tasks.append(task)
    print (f[1], proc)
    if i > 10:
        break


