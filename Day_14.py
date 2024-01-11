def get_limits(xs, ys):

    min_x = min([min(line) for line in xs])
    min_y = min([min(line) for line in ys])
    max_x = max([max(line) for line in xs])
    max_y = max([max(line) for line in ys])
    
    return min_x,min_y,max_x,max_y

def showMap(mapa):
    
    for line in mapa:
        print("".join(line))
    
with open(".\\inputs\\cave.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    
x_coords = [[(int(coord.split(",")[0])) for coord in line.split(" -> ")] for line in lines]
y_coords = [[(int(coord.split(",")[1])) for coord in line.split(" -> ")] for line in lines]

min_x,min_y,max_x,max_y = get_limits(x_coords, y_coords)

x_coords = [[num-min_x for num in line] for line in x_coords]
y_coords = [[num-min_y for num in line] for line in y_coords]

_,_,max_x,max_y = get_limits(x_coords, y_coords)

mapa = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]

mapa[0][500-min_x] = "+"

for i in range(len(x_coords)):
    for j in range(len(x_coords[i])-1):
                
        if x_coords[i][j] - x_coords[i][j+1] != 0:
            if x_coords[i][j] - x_coords[i][j+1] < 0:
                for k in range(x_coords[i][j] - x_coords[i][j+1],-1):
                    mapa[y_coords[i][j]][x_coords[i][j]+k] = "#"
                    
            else:
                range(x_coords[i][j] - x_coords[i][j+1])
                for k in range(x_coords[i][j] - x_coords[i][j+1]):
                    print(x_coords[i][j])
                    print(k)
                    mapa[y_coords[i][j]][x_coords[i][j]+k] = "#"
            
        else:
            
            if y_coords[i][j] - y_coords[i][j+1] < 0:
                for k in range(y_coords[i][j] - y_coords[i][j+1],-1):
                    mapa[y_coords[i][j]+k][x_coords[i][j]] = "#"
                    
            else:
                for k in range(y_coords[i][j] - y_coords[i][j+1]):
                    mapa[y_coords[i][j]+k][x_coords[i][j]] = "#"
        
showMap(mapa)