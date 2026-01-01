def ways(n, jumps, lookup=None):
    if n == 0:
        return 1
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
        
    else:
        nb = 0
        for jump in jumps:
            if (n-jump) >= 0:
                nb += ways(n-jump, jumps, lookup)
        lookup[n] = nb
        return lookup[n]
        
n = 10
jumps = [2, 4, 5, 8]
  
res = ways(n, jumps)  
print(res)
