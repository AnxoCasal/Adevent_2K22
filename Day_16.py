def get_valves(path):

    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
    
    valves = []
    
    for line in lines:
        name = line[6:8]
        flow = int(line[line.find("=")+1:line.find(";")])
        conexions = [var.strip() for var in line[line.find(",")-2:].split(",")]
        
        valves.append({"name":name,"flow":flow,"conexions":conexions,"open":False})
        
        
    return valves

def get_conexions(actual,valves):
    
    childs = []
    
    for conexion in actual["conexions"]:
        for valve in valves:
            if conexion == valve["name"]:
                childs.append(valve)
                
    return childs

def get_path(path):

  actual = path.pop()
  actual_path = [actual["estado"]]

  while actual["padre"] != None:
    for estado in path:
      if estado["estado"] == actual["padre"]:
        actual = estado
        actual_path.append(actual["estado"])

  return actual_path[::-1]

def darFormato(estado, padre):

  estado_base = {"estado":None, "padre":None, "peso":0}
  new_estado = estado_base.copy()
  new_estado["estado"] = estado
  if padre:
    new_estado["padre"] = padre["estado"]
    new_estado["peso"] = padre["peso"]+1

  return new_estado

def dijkstra(actual, final, valves):
    
    actual = darFormato(actual,None)
    
    open_nodes = [actual]
    close_nodes = []
    obtener_peso = lambda estado: estado["peso"]
    
    while actual["estado"]["name"] != final["name"]:
        
        close_nodes.append(actual)
        conexions = get_conexions(actual["estado"],valves)
        conexions = [node for node in conexions if node["name"] not in [cerrado["estado"]["name"] for cerrado in close_nodes]]
        conexions = [darFormato(node,actual) for node in conexions]
        open_nodes += conexions
        actual = min(open_nodes, key=obtener_peso)
        open_nodes.remove(actual)
        
    close_nodes.append(actual)
        
    return len(get_path(close_nodes))

def descend(deepness):
    
    deepness -= 1
    
    if deepness:
    
        get_gain = lambda valve: valve["gain"]
                
        valve_aux = valve
        worth_valves_2 = worth_valves.copy()
        worth_valves_2.remove(valve_aux)
        minutes_2 = minutes -distancia
                
        for i in range(deepness):
                    
            valve_gains_2 = []
                    
            for valve_2 in worth_valves_2:
                
                distancia_2 = dijkstra(valve_aux,valve_2,valves)
                gain_2 = (minutes_2 - distancia_2) * valve_2["flow"]
                        
                if gain_2 > 0:
                    valve_gains_2.append({"valve":valve_2,"gain":gain_2})
                            
            if valve_gains_2:
                
                best = max(valve_gains_2, key=get_gain)
                gain += best["gain"]
    

def main(deepness = 0):
    
    valves = get_valves(".\\inputs\\valves_test.txt")
    get_gain = lambda valve: valve["gain"]
    actual = valves[0]
    minutes = 30
    total = 0
            
    worth_valves = [valve for valve in valves if valve["open"] == False and valve["flow"] != 0]
    
    while worth_valves:
            
        worth_valves = [valve for valve in valves if valve["open"] == False and valve["flow"] != 0]
        valve_gains = []
        
        for valve in worth_valves:
            
            distancia = dijkstra(actual,valve,valves)
            
            gain = (minutes - distancia) * valve["flow"]
            
            if minutes > 0:
                valve_gains.append({"valve":valve,"gain":gain})
        
        if valve_gains:
            
            best = max(valve_gains, key=get_gain)
            
            
            distancia = dijkstra(actual,best["valve"],valves)
                
            actual = best["valve"]
            print(actual)
            print(minutes)
            print(distancia)
            print(actual["flow"])
            gain = (minutes - distancia) * actual["flow"]
            minutes -= distancia
            total += gain
            actual["open"] = True
        
        else: 
            break
    
    print(total)
            
main(deepness=1)