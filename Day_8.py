def visibility_checker(tree,side):
    for num in side:
        if num >= tree:
            return False
    
    return True

with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\trees.txt') as file:
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
        
##visibility_map =[]
    
for i in range(len(xaxis[0])):
##    visibility_map.append("")
    for j in range(len(xaxis[0])):
        target = xaxis[i][j]
        visible = False
        
        sides = []
        
        sides.append(xaxis[i][:j])
        sides.append(xaxis[i][j+1:])
        sides.append(yaxis[j][:i])
        sides.append(yaxis[j][i+1:])
        
        for side in sides:
            visible = visibility_checker(target,side)
            if visible:
                break
        
        if visible:
            cont+=1
##            visibility_map[len(visibility_map)-1] += "1"
##        else:
##            visibility_map[len(visibility_map)-1] += "0"
##
##for line in visibility_map:
    print(line)

print(cont)