import unittest

from correct_Parentheses import Solution
from daily_temperatures import SolutionX

class test_parenthese(unittest.TestCase):
    
    def setUp(self) -> None:
        self.sol = Solution()
        self.daily = SolutionX()
    
    def test1_rip(self):
        self.assertEqual(self.sol.removeInvalidParentheses('()())()'), ["(())()","()()()"])
        self.assertEqual(self.sol.removeInvalidParentheses('(a)())()'), ["(a())()","(a)()()"])
        self.assertEqual(self.sol.removeInvalidParentheses(')('), [""])
        self.assertEqual(self.sol.removeInvalidParentheses('))()(('), ["()"])
        self.assertEqual(self.sol.removeInvalidParentheses_wide_search('))()(('), ["()"])
        self.assertEqual(self.sol.removeInvalidParentheses_wide_search('(a)())()'), ["(a())()","(a)()()"])
        self.assertEqual(self.sol.removeInvalidParentheses_wide_search(')('), [""])
        
    
#    def temp_test(self):
#        self.assertEqual(self.daily.better_realization([73,74,75,71,69,72,76,73]),[1,1,4,2,1,1,0,0])
#        self.assertEqual(self.daily.better_realization([30,40,50,60]),[1,1,1,0])
#        self.assertEqual(self.daily.better_realization([30,60,90]),[1,1,0])
#        self.assertEqual(self.daily.better_realization([11, 11, 11]),[1,1,0])

if __name__=='__main__':
    unittest.main()