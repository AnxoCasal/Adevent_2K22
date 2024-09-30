import misc
import os
import copy

def paint(tunnel):
    
    for y in tunnel[::-1]:
        floor = ""
        
        for x in y:
            if x == 1:
                floor += "@"
            elif x == 2:
                floor += "#"
            else:
                floor += "."
        
        print(floor)
        
def clean_tunnel(tunnel, force = False):
    
    if force:
    
        for l in range(len(tunnel)):
            if not 2 in tunnel[l]:
                return tunnel[:l]
    
    for l in range(len(tunnel)):
        if tunnel[l] == [0,0,0,0,0,0,0]:
            return tunnel[:l]
    
    return tunnel
        
def spawn_rock(tunnel, rocks, rock_index):
    
    tunnel = clean_tunnel(tunnel)
    
    rock = rocks[rock_index]
    
    empty_line = [0,0,0,0,0,0,0]
    
    for i in range(3):
        tunnel.append(empty_line.copy())
        
    for line in rock[::-1]:
        
        new_line = empty_line.copy()
        
        for i in range(len(line)):
            new_line[i+2] = line[i]
        
        tunnel.append(new_line)    
    
    return tunnel

def fall_rock(tunnel):
    
    result = move_rock(tunnel)
    
    if result:
        tunnel = result
    else:
        for line in tunnel:
            if 1 in line:
                for l in line:
                    if l == 1:
                        line[line.index(1)] = 2
                
    return tunnel,bool(result)

def move_rock(tunnel):
    
    new_tunnel = copy.deepcopy(tunnel)
    
    for l in range(len(new_tunnel)):
        
        if 1 in new_tunnel[l]:
            
            below = new_tunnel[l-1]
            indexs = [i for i, x in enumerate(new_tunnel[l]) if x == 1]
            
            for i in indexs:
                if below[i] == 2:
                    return False
                else:
                    below[i] = 1
                    new_tunnel[l][i] = 0
            
    return new_tunnel

def jet_move(tunnel, direction):
    
    go_right = direction == ">"
    
    new_tunnel = copy.deepcopy(tunnel)
        
    for l in range(len(new_tunnel)):
        
        if 1 in new_tunnel[l]:
            
            indexs_1 = [i for i, x in enumerate(new_tunnel[l]) if x == 1]
            indexs_2 = [i for i, x in enumerate(new_tunnel[l]) if x == 2]
            
            if 6 in indexs_1 and go_right or 0 in indexs_1 and not go_right:
                return tunnel
            
            else:
                if go_right:
                    
                    for i in indexs_1[::-1]:
                        for j in indexs_2:
                            if i == j-1:
                                return tunnel
                        
                        new_tunnel[l][i] = 0    
                        new_tunnel[l][i+1] = 1    
                    
                else:
                    
                    for i in indexs_1:
                        for j in indexs_2:
                            if i == j+1:
                                return tunnel
                        
                        new_tunnel[l][i] = 0    
                        new_tunnel[l][i-1] = 1    
            
                    
    return new_tunnel
            
def main(rock_cant, rocks, tunnel, jets):

    next_rock = True
    jet = False
    down = False
    rock_index = 0
    jet_index = 0

    while True:
        
        if next_rock:
            
            if rock_index >= rock_cant: return tunnel
            
            next_rock = False
            jet = True
            
            tunnel = spawn_rock(tunnel,rocks,rock_index%5)
            
            rock_index += 1
        
        elif jet:
            
            jet = False
            down = True
            
            tunnel = jet_move(tunnel, jets[jet_index%len(jets)])
            
            jet_index+=1
            
        elif down:
            down = False
            
            tunnel,bottom = fall_rock(tunnel)
            
            next_rock = not bottom
            jet = bottom

jets = misc.get_input(".\\inputs\\jet_pattern.txt")[0]
    
rocks=[
    [[1,1,1,1]],
    [[0,1,0],[1,1,1],[0,1,0]],
    [[0,0,1],[0,0,1],[1,1,1]],
    [[1],[1],[1],[1]],
    [[1,1],[1,1]]
]

tunnel = [[2,2,2,2,2,2,2]]
        
tunnel = main(2022, rocks, tunnel, jets)

print(len(clean_tunnel(tunnel,True))-1)