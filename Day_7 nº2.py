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

with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\directories.txt') as file:
    lines = file.readlines()

directories = []
actual_directory = directory(lines[0][5:])
directories.append(actual_directory)

for line in lines[1:]:
    
    if line.startswith("$ cd") and not line.startswith("$ cd ."):
        for i in directories:
            if i.name == line[5:]:
                actual_directory = i
    
    if line.startswith("dir"):
        new_dir = directory(line[4:])