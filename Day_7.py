class directory:
    name = ""
    simple_size = 0
    real_size = 0
    sons = []
    
    def __init__(self, dirname):
        self.name = dirname
        self.sons = []
        
    def add_file(self, file_size):
        self.simple_size += file_size
        
    def add_children(self, children):
        self.sons.append(children)
        
def fixname(name, listdir):
    flag = True
    while flag:
        flag = False
        for aux in listdir:
            if aux.name == name:
                name = name + "+"
                flag = True
                break
    return(name)

def calc_dir_size(carpeta):
    size = carpeta.simple_size
    for next in carpeta.sons:
        size += calc_dir_size(next)
    return size
                

with open('directories.txt') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

directories = []
actual_directory = directory(lines[0][5:])
directories.append(actual_directory)


for line in lines[1:]:
    
    if line.startswith("$ cd") and not line.startswith("$ cd ."):
        n = len(directories)
        for i in range(len(directories)):
            n -= 1
            if directories[n].name.startswith(line[5:]):
                actual_directory = directories[n]
                break
    
    if line.startswith("dir"):
        nombre = fixname(line[4:], directories)
        new_dir = directory(nombre)
        directories.append(new_dir)
        actual_directory.add_children(new_dir)
        print(actual_directory.name)
        
    if line[0].isdigit():
        size = ""
        for char in line:
            if char.isdigit():
                size += char
            else:
                break
        actual_directory.add_file(int(size))
        
result = 0

for dire in directories:
    aux = calc_dir_size(dire)
    if aux <= 100000:
        result += aux
        
print(result)