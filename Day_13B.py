def getPackages(path):

    with open(path) as file:
        packages = [par.split("\n") for par in file.read().strip().split("\n\n")]
        
    return packages

def unpack(pair):
    return pair[1:][::-1][1:][::-1]

def has_empties(left,right):
    
    if len(left) == 0:
        return True
    elif len(right) == 0:
        return False

def get_elements(element):
    
    items = element.split(",")
    
    while True:
        for i in range(len(items)):
            cont = items[i].count("[") - items[i].count("]")
            if cont > 0:
                items = concat_until_end(items,i)
                break
            
        if i == len(items)-1:
            break
                
    return(items)

def concat_until_end(items,i):
    
    cont = items[i].count("[") - items[i].count("]")
    
    while cont > 0:
        items[i] = items[i] +","+ items.pop(i+1)
        cont = items[i].count("[") - items[i].count("]")
        
    return items

def compare(left,right):
    
    print(left)
    print(right)
    
    if has_empties(left,right) != None:
        return has_empties(left,right)
    
    left = get_elements(left)
    right = get_elements(right)
    
    for l_ele, r_ele in zip(left,right):
    
        print("a",l_ele)
        print("a",r_ele)
        
        if l_ele.isnumeric() and r_ele.isnumeric():
            
            if int(l_ele) < int(r_ele):
                print("Le")
                return True
            elif int(l_ele) > int(r_ele):
                return False
            
        elif not l_ele.isnumeric() and not r_ele.isnumeric():
            
            res = (compare(unpack(l_ele),unpack(r_ele)))
            if res != None:
                return res
                        
        elif not l_ele.isnumeric() and r_ele.isnumeric():
            
            res = compare(unpack(l_ele),r_ele)
            if res != None:
                return res
            
        elif l_ele.isnumeric() and not r_ele.isnumeric():
            
            res = compare(l_ele,unpack(r_ele))
            if res != None:
                return res
        
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    
packages = getPackages(".\\inputs\\distress_signal.txt")

cont = 0

for index,pack in enumerate(packages):
    
    left = unpack(pack[0])
    right = unpack(pack[1])
    
    #if compare(pack[0],pack[1]):
    #    cont += index+1
    
    input(compare(left,right))

print(cont)