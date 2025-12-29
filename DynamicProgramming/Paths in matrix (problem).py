def paths(matrix,i ,j, lookup):
    lookup = {} if lookup is None else lookup
    rows, cols = len(matrix), len(matrix[0])
    if (i,j) in lookup:
        return lookup[(i,j)]
    if i == rows-1 and j == cols-1:
        return 1
    if i == rows or j == cols or matrix[i][j] == 1:
        return 0
    lookup[(i, j)] = paths(matrix, i+1,j, lookup) + paths(matrix,i,j+1, lookup)
    return lookup[(i, j)]
    
    
    
matrix = [
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0]
]   
i,j = 0,0
value = paths(matrix, i=0, j=0, lookup={})
print(value)
