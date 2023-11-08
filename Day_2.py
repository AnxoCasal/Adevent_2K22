with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\cheats.txt') as file:
    lines = file.readlines()
    
score = 0
    
for line in lines:
    
    line = line.strip()
    line = line.replace(" ","")
    
    match line:
        case "AX":
            score += 4
        case "AY":
            score += 8
        case "AZ":
            score += 3
        case "BX":
            score += 1
        case "BY":
            score += 5
        case "BZ":
            score += 9
        case "CX":
            score += 7
        case "CY":
            score += 2
        case "CZ":
            score += 6

print(score)