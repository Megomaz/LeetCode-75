class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(index):
            if index in visited:
                return

            visited.add(index)

            for num in rooms[index]:
                dfs(num)
            

        dfs(0)
        return len(visited) == len(rooms)