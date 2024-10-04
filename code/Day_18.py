import misc

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

blocks = misc.get_input(".\\inputs\\lava.txt")
blocks = [(b.split(",")) for b in blocks]
blocks = [[int(n) for n in b] for b in blocks]

limits = [0,0,0]

t_f = 0

for x, y, z in blocks:
    limits[0], limits[1], limits[2] = max(limits[0], x), max(limits[1], y), max(limits[2], z)

map = [[[0 for _ in range(limits[2] + 1)] for _ in range(limits[1] + 1)] for _ in range(limits[0] + 1)]

for x,y,z in blocks:
    map[x][y][z] = 1
    
for b in blocks:
    
    ng = get_ng(b)
    
    for n in ng:
        
        if is_outside(n,limits):
                t_f += 1
            
        elif map[n[0]][n[1]][n[2]] == 0:
                t_f += 1
            
    
print(t_f)