def getSensorsAndBeacons(path):
    with open(path) as file:
        lines = [[(int(obj.split(" ")[-2][2:-1]),int(obj.split(" ")[-1][2:])) for obj in line.strip().split(":")] for line in file.readlines()]
        
    sensors = [pair[0] for pair in lines]
    beacons = [pair[1] for pair in lines]
    
    return(sensors,beacons)

def haversineManhattan(coord1, coord2):
    
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def getNeighbors(points):
    
    neighbors = []
    
    for point in points:
        neighbors += [(point[0]-1,point[1]),(point[0]+1,point[1]),(point[0],point[1]-1),(point[0],point[1]+1)]
        
    return list(set(neighbors))

def getAreaCovered(sensor, radio_area):
    
    area = []
    area += getNeighbors(sensor)
    
    for i in range(radio_area-1):
        
        area += getNeighbors(area)
        
    return list(set(area))

def getScannedArea(sensors, beacons):
    
    areas = []

    for i in range(len(sensors)):

        radio_area = haversineManhattan(sensors[i],beacons[i])
        areas += getAreaCovered([sensors[i]], radio_area)
        
    return areas

def main():
    
    sensors,beacons = getSensorsAndBeacons(".\\inputs\\sensors_and_beacons_test.txt")
    scannedArea = getScannedArea(sensors,beacons)

    taregetLine = []

    for point in scannedArea:

        if point[1] == 10:
            taregetLine.append(point)

    print(sorted(taregetLine))
    print(len(taregetLine))
        
print()

main()
    
print()