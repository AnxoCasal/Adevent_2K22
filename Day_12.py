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
        if hijo[0] >= 0 and hijo[1] >= 0 and hijo[0] <= len(valores)-1 and hijo[1] <= len(valores[0])-1 and valores[hijo[0]][hijo[1]] <= valores[padre[0]][padre[1]]+1:
            hijos_accesibles.append(hijo)
            
    return hijos_accesibles



##############################

with open(".\\inputs\\hill.txt") as file:
    lines = file.readlines()
    
lines = [aux.strip() for aux in lines]

for line in lines:
    if "E" in line:
        final_position = (line.index("E"),lines.index(line))
        line.replace("E","{")
    if "S" in line:
        current_position = (line.index("S"),lines.index(line))
        line.replace("S","a")
        

values = [[ord(char)-96 for char in line] for line in lines]
nodos_cerrados = []
nodos_abiertos = []

while True:
    
    nodos_cerrados.append(current_position)
    
    for hijo in getHijosAccesibles(current_position,values):
        nodos_abiertos.append(hijo)
        
    
        
    

print(nodos_abiertos)