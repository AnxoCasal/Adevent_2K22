def visibility_counter(target,side):
    i = 0
    for tree in side:
        i+= 1
        if tree >= target:
            print(i)
            return i
    return i

with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\trees.txt') as file:
    lines = file.readlines()
    
yaxis = []
xaxis = []
max_visibility = 0
        
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
            
for i in range(len(xaxis[0])):
    for j in range(len(xaxis[0])):
        target = xaxis[i][j]
        
        sides = []
        visibilities = []
        
        sides.append(xaxis[i][:j])
        sides.append(xaxis[i][j+1:][::-1])
        sides.append(yaxis[j][:i])
        sides.append(yaxis[j][i+1:][::-1])
        
        for side in sides:
            visibilities.append(visibility_counter(target,side))
        
        visibility = visibilities[0]*visibilities[1]*visibilities[2]*visibilities[3]  
            
        if visibility > max_visibility:
            max_visibility = visibility  
            
#2780520