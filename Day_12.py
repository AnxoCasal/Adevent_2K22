def getRawMap(file_path):
    with open(file_path) as file:
        raw = [_ for _ in file.read().strip().split()]
    
    return raw
        
def getValues(file_path):
    with open(file_path) as file:
        raw = [[ord(char)-96 if char != "S" and char != "E" else char for char in line] for line in file.read().strip().split()]

    coords = [[0 for _ in line] for line in raw]
    coord_bp = {"coords":None,"height":None,"father":None, "weight":None}

    for i in range(len(raw)):
        for j in range(len(raw[i])):
            coords[i][j] = coord_bp.copy()
            coords[i][j]["coords"] = (i,j)
            coords[i][j]["height"] = raw[i][j]
            coords[i][j]["weight"] = 0

            if coords[i][j]["height"] == "S":
                coords[i][j]["height"] = ord("a")-96
                start_node = coords[i][j]
            elif coords[i][j]["height"] == "E":
                coords[i][j]["height"] = ord("z")-96
                end_node = coords[i][j]
                
    return coords,start_node,end_node,coord_bp
                
def getChilds(father,coord_bp,coords):
    
    childs = [(father["coords"][0]+1,father["coords"][1]),
              (father["coords"][0]-1,father["coords"][1]),
              (father["coords"][0],father["coords"][1]+1),
              (father["coords"][0],father["coords"][1]-1)]
    
    child_nodes = []
        
    for child in childs:
        if child[0] >= 0 and child[1] >= 0 and child[0] < len(coords) and child[1] < len(coords[0]) and (coords[father["coords"][0]][father["coords"][1]]["height"]+1 >= coords[child[0]][child[1]]["height"]):
            new_child = coord_bp.copy()
            new_child["coords"] = child
            new_child["father"] = father["coords"]
            new_child["height"] = coords[child[0]][child[1]]["height"]
            new_child["weight"] = father["weight"]+1
            child_nodes.append(new_child)
    
    return child_nodes

def removeDuplicates(childs,closed,opened):
    
    closed_coords = [node["coords"] for node in closed]
    opened_coords = [node["coords"] for node in opened]
    clean_childs = []
    
    for child in childs:
        if child["coords"] not in closed_coords and child["coords"] not in opened_coords:
            clean_childs.append(child)
            
    return clean_childs

def printPath(file_path, last_node, visited_nodes):
    
    opt_path = []
    raw_map = getRawMap(file_path)

    while last_node["father"] != None:
        opt_path.append(last_node)

        for node in visited_nodes:
            if node["coords"] == last_node["father"]:
                last_node = node

    opt_path_coords = [node["coords"] for node in opt_path]

    for i in range(len(raw_map)):
        for j in range(len(raw_map[i])):
            if (i,j) in opt_path_coords:
                raw_map[i] = raw_map[i][:j] + "." + raw_map[i][j+1:]

    for line in raw_map:
        print(line)

def Dijkstra(file_path):

    coords,start_node,end_node,coord_bp = getValues(file_path)

    opened_nodes = []
    closed_nodes = []
    actual_node = start_node
    cercania_inicio = lambda target: target["weight"]

    while end_node["coords"] not in [node["coords"] for node in closed_nodes]:

        closed_nodes.append(actual_node)

        childs = getChilds(actual_node,coord_bp,coords)

        childs = removeDuplicates(childs, closed_nodes, opened_nodes)

        opened_nodes = opened_nodes + childs

        actual_node = min(opened_nodes, key=cercania_inicio)

        opened_nodes.remove(actual_node)

    print("Minimun steps to the top:", actual_node["weight"])

    printPath(file_path,actual_node,closed_nodes)
    
Dijkstra(".\\inputs\\hill.txt")