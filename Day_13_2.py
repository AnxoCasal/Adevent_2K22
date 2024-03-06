def getPackages(path):

    packages = []

    with open(path) as file:
        for pairs in file.read().split('\n\n'):
            packages.extend(list(map(eval, pairs.splitlines())))
        
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

targets = [[[2]],[[6]]]
packages.extend(targets)
indexs = []
 
for t in targets:
    
    win_cont = 1
    for pack in packages:
        if compare(pack,t):
            win_cont+=1
    indexs.append(win_cont)
    
    print(f"Index of {t}:",win_cont)
    
print(f"Result: {indexs[0]*indexs[1]}")