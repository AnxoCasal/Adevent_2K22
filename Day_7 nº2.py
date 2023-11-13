with open('directories.txt') as file:
    lines = file.readlines()
    
total_dirs = []    

for line in lines:
    if line.startswith("$ cd .."):
    elif line.startswith("$ cd"):
        total_dirs.append(0)
    elif line.startswith("$ ls"):
    elif line.startswith("dir"):
    elif line[0].isdigit():

def calc_dir_size(carpeta):
    print(carpeta.name)
    size = carpeta.simple_size
    for next in carpeta.sons:
        size += calc_dir_size(next)
    return size