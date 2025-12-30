def dist(word1, word2,i=0,j=0, lookup = None):
    lookup = {} if lookup is None else lookup
    
    if (i,j) in lookup: return lookup[(i,j)]
    if i == len(word1): return len(word2) - j
    if j == len(word2): return len(word1) - i
    

    if word1[i] == word2[j]: return dist(word1, word2,i+1,j+1, lookup)
    lookup[(i,j)] =  1 + min(dist(word1, word2,i+1,j, lookup),dist(word1, word2,i,j+1, lookup), dist(word1, word2,i+1,j+1, lookup))
    
    return lookup[(i,j)]

word1 = "inside"
word2 = "index"
res = dist(word1, word2)
print(res)
