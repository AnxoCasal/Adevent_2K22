with open("clock_program.txt") as file:
    lines = file.readlines()
    
cycle = 0
x = 1
mid_cycle = False
values = []
i = 0
last_value = 0

while True:
    cycle += 1
    if not mid_cycle:
        i+=1
    
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        values.append(cycle * x)
    
    if mid_cycle:
        mid_cycle = False
        x += last_value
    elif lines[i].strip() != "noop":
        last_value = int(lines[i][4:].strip())
        mid_cycle = True
    
    if i == len(lines)-1: break
    
print(sum(values))