class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        res = 0

        for i in guards:
            grid[i[0]][i[1]] = 1

        for i in walls:
            grid[i[0]][i[1]] = 2

        def guard_marker(row,col):
            for r in range(row+1,m):
                if grid[r][col] in [1,2]:
                    break
                grid[r][col] = 3
            
            for r in reversed(range(0,row)):
                if grid[r][col] in [1,2]:
                    break
                grid[r][col] = 3

            for c in range(col+1,n):
                if grid[row][c] in [1,2]:
                    break
                grid[row][c] = 3
            
            for c in reversed(range(0,col)):
                if grid[row][c] in [1,2]:
                    break
                grid[row][c] = 3
            
            return grid
                
        for r,c in guards:
            guard_marker(r,c)
        

        for row in grid:
            for col in row:
                if col == 0:
                    res +=1
        
        return res