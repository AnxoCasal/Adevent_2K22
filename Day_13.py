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
def unpack(element):
    
    return element[1:][::-1][1:][::-1]

def readElements(left,right):
    
    while True:
        if left[0] == "[" and right[0] == "[":
            left = unpack(left)
            right = unpack(right)
        else:
            break
        print(left)
        print(right)
        input()

with open(".\\inputs\\distress_signal.txt") as file:
    packages = [par.split("\n") for par in file.read().strip().split("\n\n")]
    
for index,pair in enumerate(packages):
    print(index)
    readElements(pair[0],pair[1])