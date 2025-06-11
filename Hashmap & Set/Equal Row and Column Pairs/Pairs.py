class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0]) 
        checker = defaultdict(int)
        count = 0
        
        for r in range(rows):
            checker[tuple(grid[r])] += 1

        for c in range(cols):
            column = tuple(grid[r][c] for r in range(rows))  
            count += checker[column]  

        return count