import string

with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\backpacks.txt') as file:
    lines = file.readlines()

score = 0
i = 0

while i < len(lines):
    
    for letra in lines[i]:
        if lines[i+1].find(letra) >= 0:
            if lines[i+2].find(letra) >= 0:
                if letra.islower():
                    score += string.ascii_lowercase.index(letra)+1
                else:
                    score += string.ascii_uppercase.index(letra)+27
                break
    
    print("\ni: "+str(i))
    print("letra: "+letra)
    print("score: "+str(score))
    
    i += 3

print(score)