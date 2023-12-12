with open("clock_program.txt") as file:
    lines = file.readlines()
    
cycle = 0
x = 1
mid_cycle = False
screen = [[] for _ in range(6)]
i = -1
    
if cycle-(40*(cycle//40)) == x or cycle-(40*(cycle//40)) == (x+1) or cycle-(40*(cycle//40)) == (x-1):
    screen[cycle//40].append("#") 
else:
    screen[cycle//40].append(".")

while True:
    i+=1
    cycle+=1
    
    if i == len(lines)-1: break
    
    if cycle-(40*(cycle//40)) == x or cycle-(40*(cycle//40)) == (x+1) or cycle-(40*(cycle//40)) == (x-1):
        screen[cycle//40].append("#") 
    else:
        screen[cycle//40].append(".")
    
    if mid_cycle:
        i-=1
        mid_cycle = False
    elif lines[i] != "noop\n":
        lines[i] = lines[i].replace("addx ","")
        x += int(lines[i])
        mid_cycle = True
    
    
for line in screen:
    print(line)