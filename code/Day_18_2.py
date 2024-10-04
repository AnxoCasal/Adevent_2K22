import misc
import os

def get_ng(t):
    
    directions = [[+1,0,0],[-1,0,0],[0,+1,0],[0,-1,0],[0,0,+1],[0,0,-1]]
    ng = [[x + y for x, y in zip(t, d)] for d in directions]
    
    return ng

def is_outside(t,limits):
    
    if t[0] < 0 or t[0] > limits[0]:
        return True
    
    if t[1] < 0 or t[1] > limits[1]:
        return True
    
    if t[2] < 0 or t[2] > limits[2]:
        return True
    
    return False

def is_external(t,limits,mapa):
                
    seen = []
    childs = []
    queu = [x for x in get_ng(t) if not is_outside(x,limits) and mapa[x[0]][x[1]][x[2]] == 0]
        
    while queu:
        queu = list(map(list, set(map(tuple, queu))))
        
        child = queu.pop(0)
        seen.append(child)
        
        if is_outside(child,limits):
            return True,seen+queu+t
        
        elif mapa[child[0]][child[1]][child[2]] == 0:
            childs = get_ng(child)
            
            for ng in childs:
                if is_outside(ng,limits):
                    return True,seen+t+queu
                
                elif mapa[ng[0]][ng[1]][ng[2]] == 0 and ng not in seen:
                    queu.append(ng)
    
    return False,seen+queu+t

blocks = misc.get_input(".\\inputs\\lava.txt")
blocks = [(b.split(",")) for b in blocks]
blocks = [[int(n) for n in b] for b in blocks]

limits = [0,0,0]

t_f = 0

for x, y, z in blocks:
    limits[0], limits[1], limits[2] = max(limits[0], x), max(limits[1], y), max(limits[2], z)

mapa = [[[0 for _ in range(limits[2] + 1)] for _ in range(limits[1] + 1)] for _ in range(limits[0] + 1)]
externals = []
internals = []

for x,y,z in blocks:
    mapa[x][y][z] = 1
                
for b in blocks:
    
    ngs = get_ng(b)
    
    for x,y,z in ngs:
        
        if is_outside([x,y,z], limits) or [x,y,z] in externals:
            t_f += 1
        
        elif mapa[x][y][z] == 0 and [x,y,z] not in internals:
            external,explored =  is_external([x,y,z],limits,mapa)
        
            if external:
                externals += explored
                t_f += 1
            else:
                internals += explored     
    
print(t_f)