with open('.\\inputs\\camps.txt') as file:
    lines = file.readlines()
    
cont = 0
    
for line in lines:
    line = line.strip()
    pair = line.split(",")
    
    camp_4_elf = []
    
    for elf in pair:
        camp_4_elf.append(elf.split("-"))
        
    for element in camp_4_elf:
        element[0] = int(element[0])
        element[1] = int(element[1])
        
    if camp_4_elf[0][0] <= camp_4_elf[1][0] and camp_4_elf[0][1] >= camp_4_elf[1][1]:
        cont += 1
    elif camp_4_elf[0][0] >= camp_4_elf[1][0] and camp_4_elf[0][1] <= camp_4_elf[1][1]:
        cont += 1
        
print (cont)