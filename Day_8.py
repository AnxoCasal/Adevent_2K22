def get_trees(path):
    
    with open(path) as file:
        trees = [[tree for tree in line.strip()] for line in file.readlines()]

    return trees

def check_tree(point, trees):
    
    if check_south(point, trees) or check_north(point, trees) or check_east(point, trees) or check_west(point, trees):
        return True
    
def check_north(point, trees):
    
    y = point[0]
    x = point[1]
    
    for i in range(len(trees)):
        if i == y:
            return True
        elif trees[i][x] >= trees[y][x]:
            return False
    
def check_south(point, trees):
    
    y = point[0]
    x = point[1]
    
    for i in range(len(trees)-1,-1,-1):
        if i == y:
            return True
        elif trees[i][x] >= trees[y][x]:
            return False
        
def check_east(point, trees):
    
    y = point[0]
    x = point[1]
    
    for i in range(len(trees[y])):
        if i == x:
            return True
        elif trees[y][i] >= trees[y][x]:
            return False
        
def check_west(point, trees):
    
    y = point[0]
    x = point[1]
    
    for i in range(len(trees[y])-1,-1,-1):
        if i == x:
            return True
        elif trees[y][i] >= trees[y][x]:
            return False
            
def main():
    
    trees = get_trees(".\\inputs\\trees.txt")
    
    cont = 0
    
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if check_tree((i,j),trees):
                cont += 1
                
    print(cont)
    
main()