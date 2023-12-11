with open("clock_program.txt") as file:
    lines = file.readlines()
    
cycle = 0
x = 1
mid_cycle = False
values = []
i = -1

while True:
    i+=1
    
    cycle+=1
    
    if mid_cycle:
        i-=1
        mid_cycle = False
    elif lines[i] != "noop\n":
        lines[i] = lines[i].replace("addx ","")
        x += int(lines[i])
        mid_cycle = True
        
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        print(cycle)
        values.append(cycle * x)
    
    if i == len(lines)-1: break
          
print(sum(values))

#17380 > ?
#15180 > ?