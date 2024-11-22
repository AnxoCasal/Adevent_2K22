import misc
import re
from itertools import product

def test(bp, order):
    
    mins = 24
    ro = 1
    rc,rob,rg,o,c,ob,g = 0,0,0,0,0,0,0
    cro, crc, crob, crg = False,False,False,False
    idx = 0
    
    for _ in range(mins):
        
        if idx >= len(order):
            if o >= bp["geode"][0] and ob >= bp["geode"][1]:
                o -= bp["geode"][0]
                ob -= bp["geode"][1]
                crg = True
                idx += 1
            
        elif order[idx] == "1":
            if o >= bp["ore"]:
                o -= bp["ore"]
                cro = True
                idx += 1
                
        elif order[idx] == "2":
            if o >= bp["clay"]:
                o -= bp["clay"]
                crc = True
                idx += 1
        
        elif order[idx] == "3":
            if o >= bp["obsidian"][0] and c >= bp["obsidian"][1]:
                o -= bp["obsidian"][0]
                c -= bp["obsidian"][1]
                crob = True
                idx += 1
        
        else:
            if o >= bp["geode"][0] and ob >= bp["geode"][1]:
                o -= bp["geode"][0]
                ob -= bp["geode"][1]
                crg = True
                idx += 1
        
        o += ro
        c += rc
        ob += rob
        g += rg
        
        if cro: 
            cro = False
            ro += 1
        
        if crc: 
            crc = False
            rc += 1
        
        if crob: 
            crob = False
            rob += 1
        
        if crg: 
            crg = False
            rg += 1
    
    return g*bp["id"]

bps = misc.get_input(".\\inputs\\blueprints.txt")

numeros = ['1', '2', '3', '4']

tot = 0

for i in range(1):
    
    id = int(re.findall(r'\d+', bps[i].split(":")[0])[0])
    ore = int(re.findall(r'\d+', bps[i].split(".")[0])[1])
    clay = int(re.findall(r'\d+', bps[i].split(".")[1])[0])
    obsidian = [int(num) for num in re.findall(r'\d+', bps[i].split(".")[2])]
    geode = [int(num) for num in re.findall(r'\d+', bps[i].split(".")[3])]
    
    bps[i] = {"id":id,"ore":ore,"clay":clay,"obsidian":obsidian,"geode":geode}
    best = 0
    
    for n in range(8,12):
        combinaciones = product(numeros, repeat=n)
        for combinacion in combinaciones:
            new = test(bps[i],str(''.join(combinacion)))
            if new > best:
                best = new
                
    tot += best
 
print(tot)