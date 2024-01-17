import time

tiempo = time.time()

lista = []

iteraciones = 1000000

for j in range(iteraciones):
        lista.append(j)
        
print(len(lista))

print(time.time() - tiempo)