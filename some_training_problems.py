from itertools import combinations
from collections import Counter, defaultdict, deque

class Node():
    
    def __init__(self, val, parent = None) -> None:
        self.val = val
        self.parent = parent
        self.child = []
    
    def add_child(self, Node):
        self.child.append(Node)
        
        

class Tree():
    """
    Tree class with head in the top and branches
    """
    def __init__(self, head: Node = None) -> None:
        self.head = head
    
    def add_to(self, *val: tuple(int), place: Node = None):
        
        """
        Adding branches to tree method
        Warning! This will not check if head is exist ethier not

        Args:
            val (tuple(int)): tuple or value
            place (Node) = None: Node to place value at
        Return:
            list[Node]: list which will return nodes, to work with
            
        """
        if place is None:
            place = self.head
        node_adr = []
        for i in val:
            new_Node = Node(i, parent = place)
            place.add_child(new_Node)
    
    def fill_tree(self, *vals: tuple, place: Node = None, repeat:int = 3) ->None:
        """Filling tree in depth

        Args:
            place (Node, optional): place to check positions. Defaults to None.
            repeat (int, optional): depth. Defaults to 3.

        Returns:
            None
        """
        if place == None:
            place = self.head
        if repeat == 0:
            return None
        for i in vals:
            new_node = Node(i, place)
            place.add_child(new_node)
            tmp = vals[:]
            tmp.remove(i)
            self.fill_tree(tmp, place = new_node, repeat=repeat-1)
        
    def print_tree(self, curr_node: Node = None):
        if curr_node is None:
            curr_node  = self.head
        for child in curr_node.child:
            pass    
    
    def all_sum(self, curr_node:Node = None):
        if curr_node is None:
            curr_node  = self.head
        for child in curr_node.child:
            tmp = curr_node.val
            tmp += self.all_sum(child)
            yield tmp
            
            

class Solution(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_unique = set(nums)
        if target not in nums_unique:
            return -1
        iteration_values_nums = list(enumerate(nums))
        if target < nums[0]:
            iteration_values_nums = reversed(iteration_values_nums)
        for idx, val in iteration_values_nums:
            if target == val:
                return idx

    def find_min(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = -1
        step = -1
        if nums[0] < nums[-1]:
            return nums[0]
        current_element = new_element = nums[i]
        while current_element >= new_element:
            current_element = new_element
            i += step
            new_element = nums[i]
        return current_element

    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_open_valid = {'{': '}', '(': ')', '[': ']'}
        parentheses_close_valid = {'}': '{', ')': '(', ']': '['}
        if len(s) % 2 != 0:
            return False
        open_queue = deque()
        for i in s:
            if i in parentheses_open_valid.keys():
                open_queue.append(i)
                continue
            if len(open_queue) == 0:
                return False
            if open_queue.pop() != parentheses_close_valid[i]:
                return False
        if len(open_queue) !=0:
            return False
        return True
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_count = Counter(nums)
        key_vals = nums_count.keys
        
         
        sum_of_two = defaultdict(lambda:0)
        for idx, val in nums_count.items():
            tmp = dict(nums_count)
            tmp[idx]-=1
            if tmp[idx] == 0:
                tmp.pop(idx)
            for jdx, _ in tmp.items():
                sum_of_two[f'{idx} {jdx}'] = idx+jdx
        print(sum_of_two)               
            
            

sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
