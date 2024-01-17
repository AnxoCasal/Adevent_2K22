def getSensorsAndBeacons(path):
    with open(path) as file:
        lines = [[(int(obj.split(" ")[-2][2:-1]),int(obj.split(" ")[-1][2:])) for obj in line.strip().split(":")] for line in file.readlines()]
        
    sensors = [pair[0] for pair in lines]
    beacons = [pair[1] for pair in lines]
    
    return(sensors,beacons)

def getScannedArea(sensors, beacons):
    
    extremos = []

    for i in range(len(sensors)):

        radio_area = haversineManhattan(sensors[i],beacons[i])
        extremos.append(getExtremes(sensors[i], radio_area))
        
    return extremos

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

def clean_from_beacons(scanned_area, beacons):
    
    for beac in beacons:
        if beac in scanned_area:
            scanned_area.remove(beac)
            
    return scanned_area

def getExtremes(sensor, radio):
    
    return [[(sensor[0]+radio,sensor[1]),(sensor[0]-radio,sensor[1]),(sensor[0],sensor[1]+radio),(sensor[0],sensor[1]-radio)]]
    
def main():
    
    sensors,beacons = getSensorsAndBeacons(".\\inputs\\sensors_and_beacons_test.txt")
    print(len(combinarSensores(sensors)))


def combinarSensores(sensores):
    
    combinations = []
    
    sensores_og = sensores.copy()
    
    for i in range(len(sensores)):
        
        sensores = sensores_og.copy()
        sensores = sensores.remove(sensores[i])
        
        for j in range(len(sensores)):
            for l in range(len(sensores)):
                for k in range(len(sensores)):
                     if [sensores[i],sensores[j],sensores[l],sensores[k]] not in combinations:
                         combinations.append([sensores[i],sensores[j],sensores[l],sensores[k]])
                         
    return combinations
            
main()


"""_summary_
haciendo combinaciones de los sensores busco el punto centrico entre ellos
luego midiendo sus radios miro si alguno de ellos llega, si ninguno llega, ese es el punto
"""
