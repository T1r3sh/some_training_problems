import unittest
from travel_distance import Solution

class testing(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
    def graph_traverse_test_1(self):
        self.assertEqual(self.solution.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]), [8,12,6,10,10,10])
        self.assertEqual(self.solution.sumOfDistancesInTree(1, []), [0])
        self.assertEqual(self.solution.sumOfDistancesInTree(2, [[1, 0]]), [1, 1])
        