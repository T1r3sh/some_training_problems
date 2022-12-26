from collections import defaultdict

class Solution:
    def dfs(self, visited, distance_map, graph, node):
        if node not in visited:
            visited.add(node)
            # distance_map[node]+=distance_map[node-1]
            for neigbour in graph[node]:
                self.dfs(visited, distance_map, graph, neigbour)
    
    
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        #graph_ = defaultdict(list)
        graph_ = [[]*n]
        for val, neigbour in edges:
            graph_[val].append(neigbour)
            graph_[neigbour].append(val)
        distance_map = [[0]*n for _ in range(n)]
        
        for elem in range(n):
            visited = set()
            self.dfs(visited, distance_map, graph_, elem)
            # here processing for each node
            pass
            
        return 0
    
    
        """
        ok this wouldnt work so well. Ok. We can make visited as dict to write every distance in a row
        This will work well but time complexity is just anourmous. And recursion didnt make things better talking of sapce somplexity
        to make things right we need to memorize every distance between vertex of graph.
        so let me think 
        How can we memo?
        we cna realize bfs and traverse through tree using stack and knowing every distance length from top to bottom.is this enough?
        probably not. 
        
        
        Ok dfs first
        """