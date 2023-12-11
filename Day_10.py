with open("clock_program.txt") as file:
    lines = file.readlines()
    
cycle = 0
x = 0
mid_cycle = False
values = []
    
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    
    cycle+=1
    
    if mid_cycle:
        mid_cycle = False
    elif lines[i] != "noop":
        lines[i] = lines[i].replace("addx ","")
        x += int(lines[i])
        mid_cycle = True
        
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        print(cycle)
        values.append(cycle * x)        
                
print(sum(values))

#17380 > ?

### NO ME ESTOY PARANDO CUANDO HAY CICLOS EXTRAS