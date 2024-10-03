import misc

tunnel = []
jets = misc.get_input(".\\inputs\\jet_pattern.txt")[0]
blocks = [[[0,0,1,1,1,1,0]],[[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0]],[[0,0,0,0,1,0,0],[0,0,0,0,1,0,0],[0,0,1,1,1,0,0]],[[0,0,1,0,0,0,0],[0,0,1,0,0,0,0],[0,0,1,0,0,0,0],[0,0,1,0,0,0,0]],[[0,0,1,1,0,0,0],[0,0,1,1,0,0,0]]]
rc = []
st,ri,ji = 0,0,0

pattern = [0] * 30
top = []

tp,talt,tri,loop_gain = None,None,None,None

pre_loop_l = 1000

n_rocks = 1000000000000
    
while ri < n_rocks:
    
    if tp == pattern and loop_gain == None and tunnel[-30:] == top:
        
        loop_duration = ri - pre_loop_l
        loop_gain = len(tunnel.copy()) - talt
        n_loops_remains = (n_rocks - ri) // loop_duration
        rocks_after_loop = (n_rocks - ri) % loop_duration
        height_in_loops = loop_gain * n_loops_remains
        
        n_rocks = rocks_after_loop 
        ri = ri%5
                
    if ri == pre_loop_l and talt == None:
        tp = pattern.copy()
        top = tunnel[-30:]
        talt = len(tunnel.copy())
        
    match st:
        
        case 0:
            
            pattern.append(ri%5)
            pattern.pop(0)
            
            rc = []            
            tunnel += [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
            
            for l in blocks[ri%5][::-1]:
                x = [i for i, x in enumerate(l) if x == 1]
                y = len(tunnel)
                rc += [(xs,y) for xs in x]
                tunnel += [[0,0,0,0,0,0,0]]
                
            st = 1
            
        case 1:
            
            limit = False
            j = jets[ji%len(jets)]
            pattern.pop(0)
            
            d = 1 if j == ">" else -1
            
            for r in rc:
                if r[0] == 0 and d == -1 or r[0] == 6 and d == 1 or tunnel[r[1]][r[0]+d] == 2:
                    limit = True
            
            if not limit:
            
                pattern.append(j)
                rc = [(r[0]+d,r[1]) for r in rc]
            
            else:
                pattern.append("/")
                
            st = 2
            ji += 1
            
        case 2:
            pattern.pop(0)
            base = False
            
            for c in rc:
                if tunnel[c[1]-1][c[0]] == 2 or c[1] == 0:
                    base = True
            
            if base:
            
                pattern.append("_")
                for c in rc:
                    tunnel[c[1]][c[0]] = 2
                
                while tunnel[-1] == [0,0,0,0,0,0,0]:
                    tunnel.pop(-1)
                
                ri += 1
                st = 0
                
            else:
                rc = [(r[0],r[1]-1) for r in rc]
                st = 1
            
                pattern.append("V")

print(len(tunnel) + height_in_loops)