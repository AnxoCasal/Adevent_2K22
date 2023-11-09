with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\camps.txt') as file:
    lines = file.readlines()
    
cont = 0
    
for line in lines:
    line = line.strip()
    pair = line.split(",")
    
    camp_4_elf = []
    
    for elf in pair:
        camp_4_elf.append(elf.split("-"))
        camp_4_elf
        
    for element in camp_4_elf:
        element[0] = int(element[0])
        element[1] = int(element[1])
        
    i = range(camp_4_elf[0][0],camp_4_elf[0][1]+1)
    k = range(camp_4_elf[1][0],camp_4_elf[1][1]+1)

    if len(list(set(i) & set(k))) > 0:
        cont += 1    
    
print (cont)