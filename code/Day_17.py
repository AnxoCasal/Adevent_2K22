import misc

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

def clean_tunnel(tunnel):
    
    if tunnel != []:
        while tunnel[-1] == [0,0,0,0,0,0,0]:
            tunnel.remove([0,0,0,0,0,0,0])
        
    return tunnel
        
def spawn_rock(tunnel, rocks, rock_index, rock_coords):
    
    rock_coords = []
    
    tunnel = clean_tunnel(tunnel)
    
    rock = rocks[rock_index]
    
    empty_line = [0,0,0,0,0,0,0]
    
    for i in range(3):
        tunnel.append(empty_line.copy())
        
    for line in rock[::-1]:
        
        tunnel.append(empty_line.copy())
        
        x = [i for i, x in enumerate(line) if x == 1]
        y = len(tunnel)-1
        for i in x:
            rock_coords.append((i+2,y))
    
    return tunnel,rock_coords

def fall_rock(tunnel, rock_coords):
    
    result, rock_coords = move_rock(tunnel, rock_coords)
    
    if result:
        tunnel = result
        
    else:
        
        for coord in rock_coords:
            
            x = coord[0]
            y = coord[1]
            tunnel[y][x] = 2
                
    return tunnel,bool(result),rock_coords

def move_rock(tunnel, rock_coords):
    
    new_coords = []
    
    for cords in rock_coords:
        
        x = cords[0]
        y = cords[1]
        
        if tunnel[y-1][x] == 2 or y-1 == -1:
            return False, rock_coords
        else:
            new_coords.append((x,y-1))
    
            
    return tunnel,new_coords

def jet_move(tunnel, direction, rock_coords):
    
    go_right = direction == ">"
    
    new_coords = []
    
    for cords in rock_coords[::-1]:
        
        x = cords[0]
        y = cords[1]
        
        if go_right: 
            move = +1 
        else: 
            move = -1
        
        if go_right and x == 6      or not go_right and x == 0      or tunnel[y][x+move] == 2:
            return tunnel, rock_coords
        
        else:
            new_coords.append((x+move,y))
    return tunnel,new_coords
            
def main(rock_cant, rocks, tunnel, jets):

    next_rock = True
    jet = False
    down = False
    rock_index = 0
    jet_index = 0
    
    rock_coords = False

    while True:
        
        if next_rock:
        
            if rock_index >= rock_cant: return tunnel
            
            next_rock = False
            jet = True            
            
            tunnel,rock_coords = spawn_rock(tunnel,rocks,rock_index%5,rock_coords)
            
            rock_index += 1
        
        elif jet:
            
            jet = False
            down = True
            
            tunnel,rock_coords = jet_move(tunnel, jets[jet_index%len(jets)], rock_coords)
            
            jet_index+=1
            
        elif down:
            down = False
            
            tunnel,bottom,rock_coords = fall_rock(tunnel,rock_coords)
            
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

tunnel = []
        
tunnel = main(2022, rocks, tunnel, jets)

print(len(clean_tunnel(tunnel)))