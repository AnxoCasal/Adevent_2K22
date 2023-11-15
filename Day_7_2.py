i=-1

def nuevo_dir():
    global i
    this_size = 0
    
    while i < len(lines)-1:
        i+=1
        if lines[i].startswith("$ cd .."):
            sizes.append(this_size)
            return this_size
        elif lines[i].startswith("$ cd"):
            var = nuevo_dir()
            this_size += var
        elif lines[i][0].isdigit():
            number = ""
            for char in lines[i]:
                if char.isdigit():
                    number+=char
            this_size += int(number)
    
    sizes.append(this_size)
    return this_size
    
     
with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\directories.txt') as file:
    lines = file.readlines()

sizes = []

nuevo_dir()

super_size=0

for size in sizes:
    if size > super_size:
        super_size = size
        
avalibles = []

for size in sizes:
    if size >= (30000000 - (70000000 - super_size)):
        avalibles.append(size)

print(avalibles)
avalibles.sort()
print(avalibles)
