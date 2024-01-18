import random
import time

def getSensorsAndBeacons(path):
    with open(path) as file:
        lines = [[(int(obj.split(" ")[-2][2:-1]),int(obj.split(" ")[-1][2:])) for obj in line.strip().split(":")] for line in file.readlines()]
        
    sensors = [pair[0] for pair in lines]
    beacons = [pair[1] for pair in lines]
    
    return(sensors,beacons)

def haversineManhattan(coord1, coord2):
    
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def pointSituation(point, sensors, sensors_range):
    
    cercania_a_limites = []
    
    for i in range(len(sensors)):
        point_distance = haversineManhattan(sensors[i],point)
        diferencia = sensors_range[i] - point_distance
        if diferencia >= 0:
            cercania_a_limites.append(diferencia)
            
    return cercania_a_limites

def Gachapon(orientation,sensors,sensors_range,limits):
    
    formato = {"Punto":None,"D_Escape":None}
    
    min_x = limits[0][0]
    mid_x = limits[0][0] + (limits[0][1] - (limits[0][0]))//2
    max_x = limits[0][1]
    
    min_y = limits[1][0]
    mid_y = limits[1][0] + (limits[1][1] - (limits[1][0]))//2
    max_y = limits[1][1]
    
    
    p_rnd_A = (14,11)
    p_rnd_B = (14,11)
    
    while p_rnd_A == (14,11) or p_rnd_B == (14,11):
        if orientation == 0:
            p_rnd_A = (random.randrange(min_x,max_x+1),random.randrange(min_y,mid_y+1))
            p_rnd_B = (random.randrange(min_x,max_x+1),random.randrange(mid_y,max_y+1))

        elif orientation == 1:
            p_rnd_A = (random.randrange(min_x,mid_x+1),random.randrange(min_y,max_y+1))
            p_rnd_B = (random.randrange(mid_x,max_x+1),random.randrange(min_y,max_y+1))
    
    new_punto_A = formato.copy()
    new_punto_A["Punto"] = p_rnd_A
    new_punto_A["D_Escape"] = max(pointSituation(p_rnd_A,sensors,sensors_range))
    
    new_punto_B = formato.copy()
    new_punto_B["Punto"] = p_rnd_B
    new_punto_B["D_Escape"] = max(pointSituation(p_rnd_B,sensors,sensors_range))
        
    if new_punto_A["D_Escape"] > new_punto_B["D_Escape"]:
        
        return "GrupoB"
    
    elif new_punto_A["D_Escape"] < new_punto_B["D_Escape"]:
    
        return "GrupoA"
    
    elif new_punto_A["D_Escape"] == new_punto_B["D_Escape"]:
    
        return "Even"

def limites(limits,orientation,group):
    
    min_x = limits[0][0]
    mid_x = limits[0][0] + (limits[0][1] - (limits[0][0]))//2
    max_x = limits[0][1]
    
    min_y = limits[1][0]
    mid_y = limits[1][0] + (limits[1][1] - (limits[1][0]))//2
    max_y = limits[1][1]
    
    if orientation == 0:
        if group =="A":
            return ((min_x,max_x),(min_y,mid_y))
        elif group =="B":
            return ((min_x,max_x),(mid_y,max_y))
        
    elif orientation == 1:
        if group =="A":
            return ((min_x,mid_x),(min_y,max_y))
        elif group =="B":
            return ((mid_x,max_x),(min_y,max_y))
        
def comprobarZona(zone,sensors,sensors_range):
    
    min_x = zone[0][0]
    max_x = zone[0][1]
    min_y = zone[1][0]
    max_y = zone[1][1]
    
    tiempo = time.time()
    
    for x in range(min_x,max_x+1,1):
        for y in range(min_y,max_y+1,1):
            if len(pointSituation((x,y),sensors,sensors_range)) == 0:
                return (x,y)
        #print((time.time()-tiempo)*(max_x-min_x)/60)
        #break
            
def get_sensors_range(sensors,beacons):
    
    sensors_range = []
    
    for i in range(len(sensors)):
        sensors_range.append(haversineManhattan(sensors[i],beacons[i]))
        
    return sensors_range
    
def main():
    resTest = []
    
    sensors,beacons = getSensorsAndBeacons(".\\inputs\\sensors_and_beacons_test.txt")
    sensors_range = get_sensors_range(sensors,beacons)
    
    for _ in range(3):
        zone = ((0,20),(0,20))
        for i in range(3):
            resTest = []

            for j in range(10000):
                resTest.append(Gachapon(i%2,sensors,sensors_range,zone))

            if resTest.count("GrupoA") > resTest.count("GrupoB"):
                winnerGroup = "A"
            elif resTest.count("GrupoA") < resTest.count("GrupoB"):
                winnerGroup = "B"
            else:
                print("ERROR")

            zone = limites(zone,i%2,winnerGroup)
        
            print(zone)
        print(comprobarZona(zone,sensors,sensors_range))

main()

## 14,11

## Haciendo 2 grupos de puntos aleatorios, A estando mas lejos del P y B estando mas cerca, con mi H
## El grupo B acierta un 44%, el grupo A acierta un 26% y hay un total de empates de 28%
## Por lo que si lo hago suficientes veces y voy centrando en los grupos que acierten me puedo acercar