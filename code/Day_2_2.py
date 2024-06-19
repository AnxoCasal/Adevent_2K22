with open('.\\inputs\\cheats.txt') as file:
    lines = file.readlines()
    
score = 0
    
for line in lines:
    line = line.strip()
    
    match line[0]:
        case "A":
            match line[2]:
                case "X":
                    score += 3
                case "Y":
                    score += 4
                case "Z":
                    score += 8
        case "B":
            match line[2]:
                case "X":
                    score += 1
                case "Y":
                    score += 5
                case "Z":
                    score += 9
        case "C":
            match line[2]:
                case "X":
                    score += 2
                case "Y":
                    score += 6
                case "Z":
                    score += 7
                    
print(score)