with open('.\\inputs\\inv.txt') as file:
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

max_cals = 0

for cals in elfs:
    if max_cals < cals:
        max_cals = cals

print(max_cals)