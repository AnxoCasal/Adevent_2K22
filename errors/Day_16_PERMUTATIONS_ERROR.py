from itertools import permutations

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
        
    return get_path(close_nodes)

def get_conexions(actual,valves):
    
    childs = []
    
    for conexion in actual["conexions"]:
        for valve in valves:
            if conexion == valve["name"]:
                childs.append(valve)
                
    return childs

def tryPath(path,valves,conexions):

    actual = valves[0]
    minutes = 30
    result = 0
    
    while path:
            
        new_step = path.pop()
        
        for conexion in conexions:
            if conexion[0]["name"] == actual["name"] and conexion[-1]["name"] == new_step["name"]:
                distancia = len(conexion)
                
        actual = new_step
        minutes -= distancia
        gain = minutes*actual["flow"]
        result += gain
        actual["open"] = True
    
    return result

def generate_conexiones(valves, all_valves):
    
    conexiones = []
    
    for v1 in valves:
        for v2 in valves:
                conexiones.append(dijkstra(v1,v2,all_valves))
                
    return conexiones

#Obtener las valvulas

#Buscar desde origen, cual es la válvula a abrir mas óptima
#Coger los minutos restantes (30) y restarle los movimientos necesarios para llegar a esa valvula, mas 1 por abrirla
#En caso de que los minutos restantes sean < 1, coger el siguiente movimiento mas optimo, en caso que ninguno cumpla esta restriccion, cerrar el bucle
#Coger el flow de la nueva valvula, multiplicarlo por los minutos restantes y sumar el resultado al total
#Repetir este proceso hasta que no queden valvulas por abrir, o que al hacer la resta de los minutos restantes estos den < 1

#Eh entendido el problema, solo plantear la optimizacion del siguiente movimiento, no tiene en cuenta los proximos, por lo que lo
# que puede parecer un movimiento optimo no puede dejar en una situacion que a la larga nos de peores resultados

#Para arreglar esto solo se me ocurre hacer una busqueda en profundidad haciendo todas las combinaciones posibles

def main():
    
    valves = get_valves(".\\inputs\\valves_test.txt")
    worth_valves = [valve for valve in valves if valve["open"] == False and valve["flow"] != 0]
    worth_valves.append(valves[0])
    conexiones = generate_conexiones(worth_valves, valves)
    paths = permutations(worth_valves)
    
    max = 0
    
    for path in paths:
        
        path = list(path)
        
        new = tryPath(path, valves, conexiones)
            
        if new > max:
            max = new
            
    print(max)
    
    
main()