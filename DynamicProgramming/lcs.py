def lcs(s1, s2, i=0,j=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    if i >= len(s1) or j >= len(s2):
        lookup[(i, j)] = 0  # Cache base case
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs(s1,s2,i+1,j+1,lookup)
    lookup[(i,j)] =  max(lcs(s1,s2,i+1,j,lookup), lcs(s1,s2,i,j+1,lookup))
    
    return lookup[(i,j)]
    
    
s1 = ""
s2 = ""
res = lcs(s1, s2)
print(res)
