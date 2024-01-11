"""
Obtenemos los datos
Los alacenamos en una lista de pares
Recorremos la lista haciendo la siguiente comprobaciones:
    primeramente comprobamos si ambos contienen la misma cantidad de elementos
        en caso de que el primer elemento contenga mas que el primero despachamos el par
        
        el lado derecho tenga mas que el izquierdo despachamos el par y aumentamos el contador
        
        en caso de que contenga la misma cantidad proseguimos
            comprobamos elemento por elemento realizando este mismo proceso de forma recursiva
            
                cuando lleguemos al nivel de los integers debemos empezar a comparlos como numeros, si en algun momento X > Y, despachamos el par si X < Y, lo despachamos y aumentamos el contador 
                
                si las listas son identidas = ?
"""
def getPackages(path):

    with open(path) as file:
        packages = [par.split("\n") for par in file.read().strip().split("\n\n")]
        
    return packages

def unpack(pair):
    return pair[1:][::-1][1:][::-1]

def firs_element_type(element):
    
    if len(element) == 0:
        return "empty"
    elif element[0] == "[":
        return "list"
    else:
        return "number"

def get_elements(element):
    
    items = element.split(",")
    
    while True:
        for i in range(len(items)):
            if "[" in items[i] and "]" not in items[i]:
                items = concat_until_end(items,i)
                break
            
        if i == len(items)-1:
            break
                
    return(items)

def concat_until_end(items,i):
    
    cont = 1
    
    while cont > 0:
        items[i] = items[i] +","+ items.pop(i+1)
        cont = items[i].count("[") - items[i].count("]")
        
    return items

def compare(top,bot):
    
        for i in range(len(top)):
            
            if i >= len(top):
                return True
            elif i >= len(bot):
                return False
                
            print("top:",top[i])
            print("bot:",bot[i])
            
            if top[i].isnumeric() and bot[i].isnumeric():
                
                if int(top[i]) < int(bot[i]):
                    return True
                elif int(top[i]) > int(bot[i]):
                    return False
                
            elif top[i].isnumeric() and not bot[i].isnumeric():
                
                bitems = unpack(bot[i])
                aitems = get_elements(top[i])
                bitems = get_elements(bitems)
                
                return compare(aitems,bitems)
                
            elif not top[i].isnumeric() and bot[i].isnumeric():
                
                aitems = unpack(top[i])
                aitems = get_elements(aitems)
                bitems = get_elements(bot[i])
                
                return compare(aitems,bitems)
                
            elif not top[i].isnumeric() and not bot[i].isnumeric():
                
                aitems = unpack(top[i])
                bitems = unpack(bot[i])
                aitems = get_elements(aitems)
                bitems = get_elements(bitems)
                
                return compare(aitems,bitems)

packages = getPackages(".\\inputs\\distress_signal.txt")
cont = 0   
    
for index,pair in enumerate(packages):
    
    top = unpack(pair[0])
    bot = unpack(pair[1])
    
    top_elem = get_elements(top)
    bot_elem = get_elements(bot)
    
    print(top_elem,bot_elem)
    
    print(compare(top_elem,bot_elem))
    input()