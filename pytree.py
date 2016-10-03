#!/usr/bin/env python3
import os

rootdir = os.getcwd()


for root, dirs, files in os.walk("."):
    path = root.split('/')
    for file in dirs[:-1]:
    	print("|", (len(path) - 1) * '|  ', '├──',os.path.basename(root))
    for file in dirs[-1:]:
    	print("|", (len(path) - 1) * '|  ', '└──',os.path.basename(root))
    # print("|", (len(path) - 1) * '|  ', '└──',os.path.basename(root))
    for file in files[:-1]:
    	print("|", len(path) * '|  ', '├──',file)  
    for file in files[-1:]:
    	print("|", len(path) * '|  ', '└──',file)     			
