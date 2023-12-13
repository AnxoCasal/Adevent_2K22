with open('.\\inputs\\crates.txt') as file:
    lines = file.readlines()
    
crates = lines[:8]
orders = lines[10:]

containers = []
comands = []

for line in crates:
    
    i = 0      
      
    while i < (len(line)/4):
        if len(containers)-1 < i :
            containers.append("")
        
        if not line[(i*4)+1] == " ":
            containers[i] = containers[i] + line[(i*4)+1] 
            
        i += 1
        
for i in range (len(containers)):
    containers[i] = containers[i][::-1] 
        
for line in orders:
    
    for char in line:
        if not char.isdigit():
            line = line.replace(char,"")
    
    if not len(line)>3:
        comands.append([int(line[0]),int(line[1]),int(line[2])])
    else:
        comands.append([int(line[0]+line[1]),int(line[2]),int(line[3])])

for comand in comands:
    
    aux = len(containers[comand[2]-1])
    
    containers[comand[2]-1] = containers[comand[2]-1] + containers[comand[1]-1][len(containers[comand[1]-1])-comand[0]:][::-1]
    
    aux2 = len(containers[comand[2]-1])
    aux3 = aux2 - aux
    
    containers[comand[1]-1] = containers[comand[1]-1][:-aux3]
    
print(containers)