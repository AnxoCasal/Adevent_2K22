def getPackages(path):

    with open(path) as file:
        packages = [par.split("\n") for par in file.read().strip().split("\n\n")]
        
    return packages

def unpack(pair):
    return pair[1:][::-1][1:][::-1]

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

def compare(top,bot):
      
        if checkEmpty(top,bot) != None:
            return checkEmpty(top,bot)
    
        for i in range(len(top)+1):
            
            if i >= len(top):
                return True
            elif i >= len(bot):
                return False
            
            if top[i].isnumeric() and bot[i].isnumeric():
                
                if int(top[i]) < int(bot[i]):
                    return True
                elif int(top[i]) > int(bot[i]):
                    return False
                
            elif top[i].isnumeric() and not bot[i].isnumeric():
                
                bot_items = unpack(bot[i])
                top_items = get_elements(top[i])
                bot_items = get_elements(bot_items)
                
                res = compare(top_items,bot_items)
                
                if res != None:
                    return res
                
            elif not top[i].isnumeric() and bot[i].isnumeric():
                
                top_items = unpack(top[i])
                top_items = get_elements(top_items)
                bot_items = get_elements(bot[i])
                
                res = compare(top_items,bot_items)
                
                if res != None:
                    return res
                
            elif not top[i].isnumeric() and not bot[i].isnumeric():
                
                top_items = unpack(top[i])
                bot_items = unpack(bot[i])
                top_items = get_elements(top_items)
                bot_items = get_elements(bot_items)
                
                res = compare(top_items,bot_items)
                
                if res != None:
                    return res

def checkEmpty(top,bot):
    
    if top[0] == "":
        return True
    elif bot[0] == "":
        return False    

packages = getPackages(".\\inputs\\distress_signal.txt")
cont = 0   
    
for index,pair in enumerate(packages[::-1]):
    
    top_elem = unpack(pair[0])
    bot_elem = unpack(pair[1])
    
    top_elem = get_elements(top_elem)
    bot_elem = get_elements(bot_elem)
    
    if compare(top_elem,bot_elem): 
        cont += (index+1)
        
print(cont)

#4875 < ? < 5539