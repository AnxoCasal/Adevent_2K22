class directory:
    name = ""
    simple_size = 0
    real_size = 0
    children = []
    
    def __init__(self, name):
        self.name = name
        
    def add_file(self, size):
        self.simple_size += size
        
    def add_children(self, children):
        self.children.append(children)
        
with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\directories.txt') as file:
    lines = file.readlines()

actual_directory = directory(lines[0][5:])
directories = [actual_directory]

for line in lines[1:]:
    print(lines.index(line))
    line = line.strip()
    
    if line.startswith("$ cd"):
        for aux in directories:
            if aux.name == line[5:]:
                actual_directory = aux
            
        
    if line.startswith("dir"):
        new_dir = directory(line[4:])
        directories.append(new_dir)
        actual_directory.add_children(new_dir)
        
    if line[0].isdigit():
        size = ""
        for char in line:
            if char.isdigit():
                size += char
            else:
                break
        actual_directory.add_file(int(size))
        
#for directory in directories:
#    print(len(directory.children))