def get_limits(xs, ys):

    min_x = min([min(line) for line in xs])
    min_y = min([min(line) for line in ys])
    max_x = max([max(line) for line in xs])
    max_y = max([max(line) for line in ys])
    
    return min_x,min_y,max_x,max_y

def showMap(mapa):
    
    for line in mapa:
        print(line)
    
with open(".\\inputs\\cave.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    
x_coords = [[(int(coord.split(",")[0])) for coord in line.split(" -> ")] for line in lines]
y_coords = [[(int(coord.split(",")[1])) for coord in line.split(" -> ")] for line in lines]

min_x,min_y,max_x,max_y = get_limits(x_coords, y_coords)

x_coords = [[(int(coord.split(",")[0])-min_x) for coord in line.split(" -> ")] for line in lines]
y_coords = [[(int(coord.split(",")[1])-min_y) for coord in line.split(" -> ")] for line in lines]

min_x,min_y,max_x,max_y = get_limits(x_coords, y_coords)

mapa = [["." for _ in range(max_x)] for _ in range(max_y)]

for i in range(len(x_coords)):
    for j in range(len(x_coords[i])-1):
        
        if abs(x_coords[i][j]-1 - x_coords[i][j+1]-1) != 0:
            for k in range(abs(x_coords[i][j]-1 - x_coords[i][j+1]-1)+1):
                print(k)
                mapa[y_coords[i][j]-1][x_coords[i][j+k]-1] = "#"
        else:
            for k in range(abs(y_coords[i][j]-1 - y_coords[i][j+1]-1)+1):
                print(k)
                mapa[y_coords[i][j+k]-1][x_coords[i][j]-1] = "#"
        #mapa[y_coords[i][j]-1][x_coords[i][j]-1] = "#"
        
showMap(mapa)