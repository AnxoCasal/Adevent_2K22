import string

with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\backpacks.txt') as file:
    lines = file.readlines()

score = 0

for line in lines:
    
    line = line.strip()
    size = len(line)//2
    
    part1 = line[:size]
    part2 = line[size:]
    
    for letra in part1:
        if part2.find(letra) >= 0:
            if letra.islower():
                score += string.ascii_lowercase.index(letra)+1
            else:
                score += string.ascii_uppercase.index(letra)+27
            break
        
print(score)