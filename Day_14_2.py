def get_limits(xs, ys):

    max_x = max([max(line) for line in xs])
    max_y = max([max(line) for line in ys])
    
    return max_x,max_y

def showMap(mapa):
    
    with open(".\\outputs\\cave.txt","w") as file:
        for line in mapa:
            file.write("".join(line)+"\n")
            
def getAllValues(val1,val2):
    
    values = []
    
    if val1[0] != val2[0]:
        
        if val1[0] > val2[0]:
            for i in range((val1[0] - val2[0])+1):
                values.append((val2[0]+i,val1[1]))
        
        elif val1[0] < val2[0]:
            for i in range((val2[0] - val1[0])+1):
                values.append((val1[0]+i,val1[1]))
        
    elif val1[1] != val2[1]:
        
        if val1[1] > val2[1]:
            for i in range((val1[1] - val2[1])+1):
                values.append((val1[0],val2[1]+i))
        
        elif val1[1] < val2[1]:
            for i in range((val2[1] - val1[1])+1):
                values.append((val1[0],val1[1]+i))
        
    
    return values

def generateSand():
    
    if mapa[0][500] == "0":
        return "end"
    else:
        mapa[0][500] = "0"
    
def moveSand(y,x):
    
    assert mapa[y][x] == "0"
    
    if len(mapa) <= y+1:
        mapa[y][x] = "."
        return "end"
    
    else:
        if mapa[y+1][x] == ".":
            mapa[y][x] = "."
            mapa[y+1][x] = "0"
            return moveSand(y+1,x)

        elif mapa[y+1][x-1] == ".":
            mapa[y][x] = "."
            mapa[y+1][x-1] = "0"
            return moveSand(y+1,x-1)

        elif mapa[y+1][x+1] == ".":
            mapa[y][x] = "."
            mapa[y+1][x+1] = "0"
            return moveSand(y+1,x+1)

with open(".\\inputs\\cave.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    
x_coords = [[(int(coord.split(",")[0])) for coord in line.split(" -> ")] for line in lines]
y_coords = [[(int(coord.split(",")[1])) for coord in line.split(" -> ")] for line in lines]

max_x,max_y = get_limits(x_coords, y_coords)

mapa = [["." for _ in range(max_x*2)] for _ in range(max_y+1)]
mapa.append(["." for _ in range(max_x*2)])
mapa.append(["#" for _ in range(max_x*2)])

mapa[0][500] = "+"

for i in range(len(x_coords)):
    for j in range(len(x_coords[i])-1):
        
        rock_coords = getAllValues((y_coords[i][j],x_coords[i][j]),(y_coords[i][j+1],x_coords[i][j+1]))
        
        for cord in rock_coords:
            mapa[cord[0]][cord[1]] = "#"

response = None
cont = 0

while response != "end":
    response = generateSand()
    if response != "end":
        response = moveSand(0,500)
    if response != "end":
        cont += 1
    
print(cont)
showMap(mapa)