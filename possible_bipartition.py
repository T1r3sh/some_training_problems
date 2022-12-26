from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        dis_graph = [[] for _ in range(n)]
        for a, b in dislikes:
            dis_graph[a - 1].append(b - 1)
            dis_graph[b - 1].append(a - 1)
        color_map = [0] * n
        for start in range(n):
            if color_map[start] == 0:
                queue = deque([start])
                color_map[start] = 1
                while queue:
                    vertex = queue.popleft()
                    for neighbor in dis_graph[vertex]:
                        if color_map[neighbor] == 0:
                            color_map[neighbor] = 3 - color_map[vertex]
                            queue.append(neighbor)
                        elif color_map[neighbor] == color_map[vertex]:
                            return False
        return True
