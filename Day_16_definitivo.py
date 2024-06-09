def get_valves(path):

    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
    
    valves = []
    
    for line in lines:
        name = line[6:8]
        flow = int(line[line.find("=")+1:line.find(";")])
        conexions = [var.strip() for var in line[line.find(",")-2:].split(",")]
        
        valves.append({"name":name,"flow":flow,"conexions":conexions})
        
        
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
        
    return len(get_path(close_nodes))-1

def remove_useless(valves):
   
   return [valve for valve in valves if valve["flow"] != 0]

def get_paths(valves):

    paths = []
    clean_valves = remove_useless(valves)
    clean_valves.insert(0,valves[0])

    for valve in clean_valves:
        results = []

        for target in clean_valves:
          if target == valve: continue
          results.append((target["name"],dijkstra(valve,target,valves)))
        
        paths.append({"name":valve["name"],"flow":valve["flow"],"conexions":results})

    return paths

def try_valve(actual, target, minutes):
                   
    for con in target["conexions"]:
        if con[0] == actual["name"]:

            gain = target["flow"]*(minutes-(con[1]+1))
            best = target
            min = minutes-(con[1]+1)

    return best,gain,min

def go_best_next(actual,valves,minutes):
   
    gain = 0
    best = None
    min_lat = minutes
   
    for valve in valves:
        for con in valve["conexions"]:
            if con[0] == actual["name"]:
                if valve["flow"]*(minutes-(con[1]+1)) > gain:
                   gain = valve["flow"]*(minutes-(con[1]+1))
                   best = valve
                   min_lat = minutes-(con[1]+1)
                continue

    return best,gain,min_lat

def best_go_first(actual,valves):

    while valves:
        next,gain,minutes = go_best_next(actual,valves,minutes)
        total += gain
        path.append(next)
        valves.remove(next)


def try_and_go(valves, deepness = 1):

    actual = valves[0]
    valves = valves[1:]
   
    for i in range(deepness):
        minutes = 30
        
        for valve in valves:
           
            next,gain,minutes= try_valve(actual, valve, minutes)
       
           
            
   
    

valves = get_valves(".\\inputs\\valves_test.txt")
valves = get_paths(valves)

total = 0
path = []
minutes = 30

print(total)