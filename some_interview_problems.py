from collections import defaultdict

class Solution:
    
    def dfs(self, visited, graph, node):
        if node not in visited:
            visited.add(node)
        for neigbour in graph[node]:
            if neigbour in visited:
                continue
            self.dfs(visited, graph, neigbour)
    
    
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        room_graph = defaultdict(list)
        for idx, elem in enumerate(rooms):
            room_graph[idx].extend(elem)
        visited = set()
        self.dfs(visited, room_graph, 0)
        return len(visited)==len(rooms)


sol = Solution()
print(sol.canVisitAllRooms( [[1,3],[3,0,1],[2],[0]]))
