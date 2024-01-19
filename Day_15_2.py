def getSensorsAndBeacons(path):
    with open(path) as file:
        lines = [[(int(obj.split(" ")[-2][2:-1]),int(obj.split(" ")[-1][2:])) for obj in line.strip().split(":")] for line in file.readlines()]
        
    sensors = [pair[0] for pair in lines]
    beacons = [pair[1] for pair in lines]
    
    return(sensors,beacons)

def haversineManhattan(coord1, coord2):
    
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def get_sensors_ranges(sensors,beacons):
    
    ranges = []
    
    for i in range(len(sensors)):
        ranges.append(haversineManhattan(sensors[i],beacons[i]))
        
    return ranges

def get_limits(sensor,range):
    
    return [(sensor[0]-range-1,sensor[1]),(sensor[0],sensor[1]-range-1),(sensor[0]+range+1,sensor[1]),(sensor[0],sensor[1]+range+1)]

def points_btw_diagonal(pointA,pointB,area):
        
    x_limits = area[0]
    y_limits = area[1]
    difference = abs(pointA[0] - pointB[0])
    diagonal = []
    
    if pointA[0] < pointB[0]:
        right = True
    else:
        right = False
    
    if pointA[1] < pointB[1]:
        down = True
    else:
        down = False
        
    for i in range(difference+1):
        new_point = pointA
        
        if right:
            new_point = (new_point[0]+i,new_point[1])
        else:
            new_point = (new_point[0]-i,new_point[1])
        
        if down:
            new_point = (new_point[0],new_point[1]+i)
        else:
            new_point = (new_point[0],new_point[1]-i)
            
        if new_point[0] >= x_limits[0] and new_point[0] <= x_limits[1] and new_point[1] >= y_limits[0] and new_point[1] <= y_limits[1]:
            diagonal.append(new_point)
        
    return diagonal

def get_perimetros(sensors,ranges,area):
    
    all_perimetros = []
        
    for i in range(len(sensors)) :
        
        limits = get_limits(sensors[i],ranges[i])
        perimetro = []
        
        for k in range(len(limits)):
            perimetro += points_btw_diagonal(limits[k],limits[k-1],area)
            
        all_perimetros += perimetro
        
    return all_perimetros

def isPoint(point, sensors, sensors_range):
    
    for i in range(len(sensors)):
        point_distance = haversineManhattan(sensors[i],point)
        if sensors_range[i] >= point_distance:
            return False
            
    return point

def main():
    
    sensors,beacons = getSensorsAndBeacons(".\\inputs\\sensors_and_beacons.txt")
    area = ((0,4000000000),(0,4000000000))
    ranges = get_sensors_ranges(sensors,beacons)
    perimetros = get_perimetros(sensors,ranges,area)
    
    for p in perimetros:
        res = isPoint(p,sensors,ranges)
        if res:
            print(res)
            break

import time

tiempo = time.time()
print(main())
print(time.time()-tiempo)