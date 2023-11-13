class directory:
    name = ""
    simple_size = 0
    real_size = 0
    sons = []
    
    def __init__(self, name):
        self.name = name
        self.sons = self.sons.copy()
        
    def add_file(self, size):
        self.simple_size += size
        
    def add_children(self, children):
        self.sons.append(children)

def calc_dir_size(carpeta):
    size = carpeta.simple_size
    for next in carpeta.sons:
        size += calc_dir_size(next)
    print(size)
    return size

def serch_name(nombre):
    for box in directories:
        if box.name == nombre:
            nombre += "."
            serch_name(nombre)
        
    return nombre
        
    
        
with open('directories.txt') as file:
    lines = file.readlines()

actual_directory = directory((lines[0][5:]).strip())
directories = [actual_directory]

for line in lines[1:]:
    line = line.strip()
    
    if line.startswith("$ cd"):
        for aux in directories:
            if aux.name == line[5:]:
                actual_directory = aux
            
        
    if line.startswith("dir"):
        new_dir = directory(serch_name(line[4:]))
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
        
super_size = 0

for dire in directories:
    aux = calc_dir_size(dire)
    if aux <= 10000:
        super_size += aux
        
print(aux)

# 209116 is low