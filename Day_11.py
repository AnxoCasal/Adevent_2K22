with open (".\\inputs\\monkey_business.txt") as file:
    lines = file.readlines()

monkeys = []
monkey_bp = {"code":None , "inventory":[] , "operation":None , "test":None , "iftrue":None , "iffalse":None, "counter":0}

for i in range(len(lines)):
    lines[i] = lines[i].strip()

for i in range(7,len(lines)+7,7):
    monkeys.append(lines[i-7:i-1])
    
for i in range(len(monkeys)):
    aux = monkey_bp.copy()
    
    aux["code"] = int(monkeys[i][0][-2])
    aux["inventory"] = [int(i) for i in monkeys[i][1][16:].replace(",","").split(" ")]
    aux["operation"] = monkeys[i][2][21:]
    aux["test"] = int(monkeys[i][3][19:])
    aux["iftrue"] = int(monkeys[i][4][-1])
    aux["iffalse"] = int(monkeys[i][5][-1])
    
    monkeys[i] = aux
    
for i in range(20):        
    for monke in monkeys:
                
        for item in monke["inventory"]:
            monke["counter"] += 1
            aux = item
            
            if monke["operation"][0] == "+":
                if monke["operation"][2:] == "old":
                    aux = aux + aux
                else:
                    aux = aux + int(monke["operation"][2:])
            elif monke["operation"][0] == "*":
                if monke["operation"][2:] == "old":
                    aux = aux * aux
                else:
                    aux = aux * int(monke["operation"][2:])
            
            aux = aux//3
            
            if aux%monke["test"] == 0:
                monkeys[monke["iftrue"]]["inventory"].append(aux)
            else:
                monkeys[monke["iffalse"]]["inventory"].append(aux)
                
        monke["inventory"].clear()
            
counters = []
    
for monke in monkeys:
    counters.append(monke["counter"])
    
counters = sorted(counters, reverse=True)

print(counters[0] * counters[1])