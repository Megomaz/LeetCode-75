class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        visited.add((entrance[0],entrance[1]))
        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        rows,cols = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0],entrance[1]))

        near = float('inf')
        iteration = 1

        while q:
            size = len(q)

            for _ in range(size):
                row, col = q.popleft()

                for dr,dc in directions:
                    nr, nc = dr + row, dc + col

                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and maze[nr][nc] == '.':
                        visited.add((nr,nc))
                        maze[nr][nc] = iteration
                        q.append((nr,nc))
            iteration += 1

        for i in range(cols):
            if isinstance(maze[0][i], int) and maze[0][i] < near:
                near = maze[0][i]

            if isinstance(maze[rows - 1][i], int) and maze[rows - 1][i] < near:
                near = maze[rows - 1][i]

        # Left and right columns (excluding corners to avoid duplicates)
        for i in range(1, rows - 1):
            if isinstance(maze[i][0], int) and maze[i][0] < near:
                near = maze[i][0]

            if isinstance(maze[i][cols - 1], int) and maze[i][cols - 1] < near:
                near = maze[i][cols - 1]

        return near if near != float('inf') else -1

# Better Solution (not mine)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cells = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        rows, cols = len(maze), len(maze[0])
        while cells:
            r, c, steps = cells.popleft()
            check = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for i,j in check:
                if i >= 0 and j >= 0 and i < rows and j < cols and maze[i][j] == ".":
                    if i == 0 or j == 0 or i == rows - 1 or j == cols -1:
                        return steps + 1
                    cells.append((i, j, steps + 1))
                    maze[i][j] = "+"
        return -1
            

        

