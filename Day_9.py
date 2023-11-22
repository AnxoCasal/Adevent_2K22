with open('rope.txt') as file:
    lines = file.readlines()
    
history = [0,0]
head_coord = [0,0]
tail_coord = [0,0]

for l in lines:
    lines[lines.index(l)] = l.strip()
    
for l in lines:
    
    direction = l[0]
    distance = int(l[2:])
    
    match direction:
        case "U":
            head_coord[1] += distance
        case "R":
            head_coord[0] += distance
        case "D":
            head_coord[1] -= distance
        case "L":
            head_coord[0] -= distance