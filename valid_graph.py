from collections import defaultdict

class Solution:
    def dfs(self, visited, graph, node):
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                self.dfs(visited, graph, child)
            
        
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        nodes = defaultdict(list)
        for parent_node, child_node in edges:
            nodes[parent_node].append(child_node)
            nodes[child_node].append(parent_node)
        print(nodes)
        visited = set()
        self.dfs(visited, nodes, source)
        return True if destination in visited else False
    
sol = Solution()
res = sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)# [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9)
print(res)