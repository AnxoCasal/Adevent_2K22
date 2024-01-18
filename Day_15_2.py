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
    
    return {"E":(sensor[0]+range,sensor[1]),"W":(sensor[0]-range,sensor[1]),"N":(sensor[0],sensor[1]-range),"S":(sensor[0],sensor[1]+range),}

def main():
    
    sensors,beacons = getSensorsAndBeacons(".\\inputs\\sensors_and_beacons_test.txt")
    ranges = get_sensors_ranges(sensors,beacons)
    limits = get_limits(sensors[0],ranges[0])

    return limits

print(main())