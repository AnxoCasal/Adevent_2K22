with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\inv.txt') as file:
    lines = file.readlines()
    
elfs = []
elfs.append(0)
i = 0

for line in lines:
    
    line = line.strip()
    
    if line == "":
        i += 1
        elfs.append(0)
    else:
        elfs[i] += int(line)

elfs.sort()
print(elfs[len(elfs)-1]+elfs[len(elfs)-2]+elfs[len(elfs)-3])