import unittest

from correct_Parentheses import Solution

class test_parenthese(unittest.TestCase):
    
    def setUp(self) -> None:
        self.sol = Solution()
    
    def test1_rip(self):
        self.assertEqual(self.sol.removeInvalidParentheses('()())()'), ["(())()","()()()"])
        self.assertEqual(self.sol.removeInvalidParentheses('(a)())()'), ["(a())()","(a)()()"])
        self.assertEqual(self.sol.removeInvalidParentheses(')('), [""])
        self.assertEqual(self.sol.removeInvalidParentheses('))()(('), ["()"])
    
if __name__=='__main__':
    unittest.main()