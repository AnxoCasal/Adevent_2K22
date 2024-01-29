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
        
    return len(get_path(close_nodes))

def move_cost(flow,moves):
    
    return flow/(moves+1)

def main():
    mejor_movimiento = lambda move : move[2]
    
    valves = get_valves(".\\inputs\\valves_test.txt")
    actual = valves[0]
    valves.remove(actual)
    working = 0
    steam_minute = 0
    total = 0

    for minutes in range(30):
        
        total += steam_minute
        
        if not working:
            
            worth_valves = [valve for valve in valves if valve["open"] == False and valve["flow"] != 0]
            moves = [(valve,dijkstra(actual,valve,valves)) for valve in worth_valves]
            move_costs = [(move[0],move[1]+1,move_cost(move[0]["flow"],move[1])) for move in moves]
            valves.append(actual)
            actual,working,_ = max(move_costs, key=mejor_movimiento)
            steam_minute += actual["flow"]
            actual["open"] = True
            valves.remove(actual)
        
        else: 
            
            working -= 1
            
    print(total)
    print(working)
            
main()