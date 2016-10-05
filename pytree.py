#!/usr/bin/env python3
import os
import re
import sys

# rootdir = os.getcwd()


# for root, dirs, files in os.walk("."):
#     path = root.split('/')
#     files = [f for f in files if not f[0] == '.']
#     dirs[:] = [d for d in dirs if not d[0] == '.']
#     for dir in dirs[:-1]:
#     	print( (len(path) - 1) * '   ', '├──',os.path.basename(root))
#     for dir in dirs[-1:]:      
#         print( (len(path) - 1) * '   ', '└──',os.path.basename(root))
#     for file in files[:-1]:  
#         print( len(path) * '   ', '├──',file)  
#     for file in files[-1:]:      
#         print( len(path) * '   ', '└──',file)  

numDir = 0
numFile = 0


def sort(file):
    return re.sub('[^A-Za-z0-9]+', '', file).lower()


def sortedfiles_without_hidden(root):
	dir = []
	for i in os.listdir(root):
		if not i.startswith("."):
			dir.append(i)
	return sorted(dir, key=sort)


def tree(root, prefix=""):
	files = sortedfiles_without_hidden(root)
	for i in range(len(files)):
		subdir = root + "/" + files[i]
		global numDir 
		global numFile
		if i != len(files) -1:
			print(prefix + "├── " + files[i])
		else:
			print(prefix + "└── " + files[i])
		if os.path.isdir(subdir):
			numDir += 1
			if i != len(files) -1:
				tree(subdir, prefix + "|   ")
			else:
				tree(subdir, prefix + "    ")
		else:
			numFile+= 1



if len(sys.argv) == 1:
    cwd = os.getcwd()
    print(".")
else:
    cwd = sys.argv[1]
    print(cwd)
count = tree(cwd)
print(str(numDir) + " directories, " + str(numDir) + " files")














