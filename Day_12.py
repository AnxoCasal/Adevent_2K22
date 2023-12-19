def getHijosAccesibles(padre, valores):
    hijos = [
            (padre[0]-1,padre[1]-1),
            (padre[0]+1,padre[1]-1),
            (padre[0],padre[1]-1),
            (padre[0]+1,padre[1]),
            (padre[0]-1,padre[1]),
            (padre[0]-1,padre[1]+1),
            (padre[0]+1,padre[1]+1),
            (padre[0],padre[1]+1)
            ]
    
    hijos_accesibles = []
    
    for hijo in hijos:
                        
        if hijo[0] >= 0 and hijo[1] >= 0 and hijo[0] <= len(valores)-1 and hijo[1] <= len(valores[0])-1 and valores[padre[0]][padre[1]]+1 >= valores[hijo[0]][hijo[1]]:
            hijos_accesibles.append(hijo)
    
    return hijos_accesibles

def tratarRepetidos(hijos, cerrados, abiertos):
    
    hijos_clean = []
    
    for hijo in hijos:
        if hijo not in cerrados and hijo not in abiertos:
            hijos_clean.append(hijo)
            
    return hijos_clean

##############################

with open(".\\inputs\\hill.txt") as file:
    lines = file.readlines()
    
lines = [aux.strip() for aux in lines]

for i in range(len(lines)):
    if "E" in lines[i] and "S" in lines[i]:
        final_position = (lines.index(lines[i]),lines[i].index("E"))
        current_position = (lines.index(lines[i]),lines[i].index("S"))
        lines[i] = lines[i].replace("E","{")
        lines[i] = lines[i].replace("S","a")
    elif "E" in lines[i]:
        final_position = (lines.index(lines[i]),lines[i].index("E"))
        lines[i] = lines[i].replace("E","{")
    elif "S" in lines[i]:
        current_position = (lines.index(lines[i]),lines[i].index("S"))
        lines[i] = lines[i].replace("S","a")
        
values = [[ord(char)-96 for char in line] for line in lines]

nodos_cerrados = []
nodos_abiertos = []

while True:
    
    nodos_cerrados.append(current_position)
    
    hijos = getHijosAccesibles(current_position,values)
            
    hijos = tratarRepetidos(hijos,nodos_cerrados,nodos_abiertos)
    
    for hijo in hijos:
        nodos_abiertos.append(hijo)
        
    current_position = nodos_abiertos.pop(0)
    
    if current_position == final_position:
        print("LLEGUE!!")
        break