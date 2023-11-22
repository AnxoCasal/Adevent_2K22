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
tail_coord = [0,0]

for l in lines:
    lines[lines.index(l)] = l.strip()
    
for l in lines:
    
    direction = l[0]
    distance = int(l[2:])
    
    match direction:
        case "U":
            for i in range(1,distance+1):
                print(f"Head:{head_coord} Tails:{tail_coord} Direction:{direction} Distance:{distance} HistoryL:{len(history)}")
                head_coord[1] += 1
                tail_coord = update_tail(head_coord,tail_coord)
                history = check_history(tail_coord,history)
        case "R":
            for i in range(1,distance+1):
                print(f"Head:{head_coord} Tails:{tail_coord} Direction:{direction} Distance:{distance} HistoryL:{len(history)}")
                head_coord[0] += 1
                tail_coord = update_tail(head_coord,tail_coord)
                history = check_history(tail_coord,history)
        case "D":
            for i in range(1,distance+1):
                print(f"Head:{head_coord} Tails:{tail_coord} Direction:{direction} Distance:{distance} HistoryL:{len(history)}")
                head_coord[1] -= 1
                tail_coord = update_tail(head_coord,tail_coord)
                history = check_history(tail_coord,history)
        case "L":
            for i in range(1,distance+1):
                print(f"Head:{head_coord} Tails:{tail_coord} Direction:{direction} Distance:{distance} HistoryL:{len(history)}")
                head_coord[0] -= 1
                tail_coord = update_tail(head_coord,tail_coord)
                history = check_history(tail_coord,history)


print(f"Head:{head_coord} Tails:{tail_coord} Direction:{direction} Distance:{distance} HistoryL:{len(history)}")