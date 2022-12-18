class Solution:
    
    def add(self, b, a):
        return a+b
    
    def substruct(self, b, a):
        return a-b
    
    def multiply(self, b, a):
        return a*b
    
    def divide(self, b, a):
        return int(a/b)
    
    def evalRPN(self, tokens: list[str]) -> int:
        operation_dict = {'+':self.add, '-':self.substruct, '*':self.multiply, '/':self.divide}
        stack = []
        for i in tokens:
            if i.isnumeric() or len(i)>1:
                stack.append(int(i))
            else:
                stack.append(operation_dict[i](stack.pop(), stack.pop()))
        return stack.pop()
            



sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))