class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        iterations = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q:
            size = len(q)
            for _ in range(size):
                row,col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 'T'
                        q.append((nr,nc))

            iterations += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                   return -1

        return iterations - 1 if iterations - 1 >= 0 else 0
            