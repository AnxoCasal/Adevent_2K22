i=-1

def nuevo_dir():
    global i
    this_size = 0
    
    while i < len(lines)-1:
        i+=1
        print(i)
        if lines[i].startswith("$ cd .."):
            sizes.append(this_size)
            return this_size
        elif lines[i].startswith("$ cd"):
            this_size += nuevo_dir()
        elif lines[i][0].isdigit():
            number = ""
            for char in lines[i]:
                if char.isdigit():
                    number+=char
            this_size += int(number)
     
with open('directories.txt') as file:
    lines = file.readlines()

sizes = []

nuevo_dir()

super_size=0

for size in sizes:
    if size <= 100000:
        super_size += size
        
print(super_size)