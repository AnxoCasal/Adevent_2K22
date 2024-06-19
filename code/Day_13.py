def getPackages(path):

    packages = []

    with open(path) as file:
        for pairs in file.read().split('\n\n'):
            packages.append(list(map(eval, pairs.splitlines())))
        
    return packages

def compare(left,right):
    
    for li, ri in zip(left,right):
        
        if type(li) == int and type(ri) == int:
            
            if li < ri:
                return True
            elif li > ri:
                return False
        
        else:
            res = compare([li] if type(li) == int else li, [ri] if type(ri) is int else ri)
            if res != None: return res
        
    if len(left) > len(right):
        return False
    elif len(left) < len(right):
        return True
    
packages = getPackages(".\\inputs\\distress_signal.txt")

cont = 0
 
for index,pack in enumerate(packages, start=1):
    
    if compare(pack[0],pack[1]):
       cont += index

print(f"Result: {cont}")