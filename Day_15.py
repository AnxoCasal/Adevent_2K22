def getSensorsAndBeacons(path):
    with open(path) as file:
        lines = [[(int(obj.split(" ")[-2][2:-1]),int(obj.split(" ")[-1][2:])) for obj in line.strip().split(":")] for line in file.readlines()]
        
    sensors = [pair[0] for pair in lines]
    beacons = [pair[1] for pair in lines]
    
    return(sensors,beacons)

def haversineManhattan(coord1, coord2):
    
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def getAreaCovered(sensor, target_line, radio_area):

    distance = abs(sensor[1] - target_line)
    target_line_cover = radio_area - distance
    
    area_covered = []
    
    if target_line_cover > -1:
        
        area_covered += [(sensor[0],target_line)]
    
        for i in range(target_line_cover+1):
            
            area_covered += [(sensor[0]+i,target_line),(sensor[0]-i,target_line)]
            
    return area_covered

def getScannedArea(sensors, beacons, target_line):
    
    areas = []

    for i in range(len(sensors)):

        radio_area = haversineManhattan(sensors[i],beacons[i])
        areas += getAreaCovered(sensors[i], target_line, radio_area)
        
    return set(areas)

def clean_from_beacons(scanned_area, beacons):
    
    for beac in beacons:
        if beac in scanned_area:
            scanned_area.remove(beac)
            
    return scanned_area

def main(target):
    
    sensors,beacons = getSensorsAndBeacons(".\\inputs\\sensors_and_beacons.txt")
    scannedArea = getScannedArea(sensors,beacons,target)

    return len(clean_from_beacons(scannedArea,beacons))

print(main(2000000))