def get_trees(path):
    
    with open(path) as file:
        trees = [[tree for tree in line.strip()] for line in file.readlines()]

    return trees

def check_tree(point, trees):
    
    count = check_east(point, trees)
    count *= check_north(point, trees)
    count *= check_south(point, trees)
    count *= check_west(point, trees)
    
    return count
    
def check_north(point, trees):
    
    y = point[0]
    x = point[1]
    
    cont = 0
    
    for i in range(y-1, -1, -1):
        cont += 1
        if trees[i][x] >= trees[y][x]:
            return cont
    
    return cont
    
def check_south(point, trees):
    
    y = point[0]
    x = point[1]
    
    cont = 0
    
    for i in range(y+1, len(trees)):
        cont += 1
        if trees[i][x] >= trees[y][x]:
            return cont
        
    return cont
        
        
def check_east(point, trees):
    
    y = point[0]
    x = point[1]
    
    cont = 0
    
    for i in range(x-1, -1, -1):
        cont += 1
        if trees[y][i] >= trees[y][x]:
            return cont
    
    return cont
        
def check_west(point, trees):
    
    y = point[0]
    x = point[1]
    
    cont = 0
    
    for i in range(x+1, len(trees[y])):
        cont += 1
        if trees[y][i] >= trees[y][x]:
            return cont
    
    return cont
            
def main():
    
    trees = get_trees(".\\inputs\\trees.txt")
    
    max = 0
    
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if check_tree((i,j),trees) > max:
                max = check_tree((i,j),trees)
                
    print(max)
    
main()