def visibility_checker(tree,side):
    i=0
    
    for num in side:
        i+=1
        if num >= tree:
            return i
    
    return i

with open('trees.txt') as file:
    lines = file.readlines()
    
yaxis = []
xaxis = []
cont = 0
        
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    
for i in range(len(lines[0])):
    yaxis.append([])
    for line in lines:
        yaxis[i].append(int(line[i]))
    
for i in range(len(yaxis[0])):
    xaxis.append([])
    for line in yaxis:
        xaxis[i].append(int(line[i]))

max_vision = 0

for i in range(len(xaxis[0])):
    for j in range(len(xaxis[0])):
        target = xaxis[i][j]
        vision = 1
        
        sides = []
        
        sides.append(xaxis[i][:j])
        sides.append(xaxis[i][j+1:])
        sides.append(yaxis[j][:i])
        sides.append(yaxis[j][i+1:])
        
        for side in sides:
            vision *= visibility_checker(target,side)
            
        if max_vision<vision:
            max_vision = vision
            print(sides)
            print(vision)
            print(max_vision)
            print(target)
            input("\n\n\n")

print(max_vision)

#2711268>
#2889216>