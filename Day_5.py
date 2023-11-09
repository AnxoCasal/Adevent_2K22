with open('C:\\\\Users\\Anxo\\Documents\\python\\Adevent\\crates.txt') as file:
    lines = file.readlines()
    
crates = lines[:8]
orders = lines[11:]

for line in crates:
    print(line)

for line in orders:
    
    for char in line:
        if not char.isdigit():
            line = line.replace(char,"")
    
    if not len(line)>3:
        line = [int(line[0]),int(line[1]),int(line[2])]
    else:
        line = [int(line[0]+line[1]),int(line[2]),int(line[3])]