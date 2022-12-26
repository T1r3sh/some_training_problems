from collections import defaultdict

class Solution:
    def dfs(self, visited, maxsteps, node):
        if node not in visited:
            visited.add(node)
            for child in range(node, node+maxsteps[node]) if child <len(maxsteps):
                self.dfs(visited, maxsteps, child)
            
                
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)<=1: return True
        visited = set()
        
        
        
sol = Solution()
sol.canJump([3,2,1,0,4])
