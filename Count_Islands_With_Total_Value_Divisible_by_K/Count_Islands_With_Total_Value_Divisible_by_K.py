class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j, curr_sum):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            
            if grid[i][j] == 0:
                return
            
            curr_sum[0] += grid[i][j]
            grid[i][j] = 0

            dfs(i-1, j, curr_sum)
            dfs(i+1, j, curr_sum)
            dfs(i, j-1, curr_sum)
            dfs(i, j+1, curr_sum)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    curr_sum = [0]
                    dfs(i, j, curr_sum)
                    if curr_sum[0] % k == 0:
                        count += 1
        
        return count

