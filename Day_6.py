with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\signal.txt') as file:
    lines = file.readlines()

signal = lines[0]

sample = signal[:4]
cont = 0

for char in signal:
    cont+=1
    repetitions = 0 
    sample = sample[1:] + char
    
    for char2 in sample:
        if sample.count(char2) > 1:
            repetitions += 1
    
    if repetitions == 0:
        break

print(cont)