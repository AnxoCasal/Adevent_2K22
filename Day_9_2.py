def update_tail(h,t):
    
    if h[0] > t[0]+1 and h[1] > t[1] or h[0] > t[0] and h[1] > t[1]+1:
        t[0] += 1
        t[1] += 1
    elif h[0] < t[0] and h[1] > t[1]+1 or h[0] < t[0]-1 and h[1] > t[1]:
        t[0] -= 1
        t[1] += 1
    elif h[0] > t[0]+1 and h[1] < t[1] or h[0] > t[0] and h[1] < t[1]-1:
        t[0] += 1
        t[1] -= 1
    elif h[0] < t[0]-1 and h[1] < t[1] or h[0] < t[0] and h[1] < t[1]-1:
        t[0] -= 1
        t[1] -= 1 
    elif h[0] > t[0]+1:
        t[0] += 1
    elif h[0] < t[0]-1:
        t[0] -= 1
    if h[1] > t[1]+1:
        t[1] += 1
    elif h[1] < t[1]-1:
        t[1] -= 1
        
    return t

def check_history(t,history):
    
    if t in history:
        return history
    else:
        history.append(t.copy())
        return history
    

with open('rope.txt') as file:
    lines = file.readlines()
    
history = [[0,0]]
head_coord = [0,0]
tails_coord = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for l in lines:
    lines[lines.index(l)] = l.strip()
    
for l in lines:
    
    direction = l[0]
    distance = int(l[2:])
    
    match direction:
        case "U":
            x_or_y = 1
            fw_bw = 1
        case "R":
            x_or_y = 0
            fw_bw = 1
        case "D":
            x_or_y = 1
            fw_bw = -1
        case "L":
            x_or_y = 0
            fw_bw = -1
                
    for i in range(1,distance+1):
        head_coord[x_or_y] += fw_bw
        tails_coord[0] = update_tail(head_coord,tails_coord[0])
        
        for i in range(1,len(tails_coord)):
            tails_coord[i] = update_tail(tails_coord[i-1],tails_coord[i])
            
        history = check_history(tails_coord[len(tails_coord)-1],history)


print(f"HistoryL:{len(history)}")