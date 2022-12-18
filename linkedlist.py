class list_node(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class linked_list:
    def __init__(self, head = None):
        self.head = head
    
    def push(self, val):
        new_node = list_node(val)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, val):
        new_node = list_node(val)
        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
            
    def insertAfter(self, given_node, val):
        if given_node is None:
            print('it is not in list')
        else:
            new_node = list_node(val)
            new_node.next = given_node.next
            given_node.next = new_node
    
    def delete(self, pos):
        if self.head == None:
            print('List is empty')
            return
        idx = 0
        pointer = self.head
        while pointer.next and idx<pos:
            prev = pointer
            pointer = pointer.next
            idx+=1  
        if idx<pos:
            print('Out of range')
        elif idx==0:
            self.head = self.head.next
        else:
            prev.next = pointer.next
    
    def display(self):
        pointer = self.head
        print('[ ', end = '')
        while pointer.val:
            print(str(pointer.val)+', ', end='')
            pointer = pointer.next
        print(']')
        
    def length(self):
        pointer = self.head
        idx = 0
        while pointer.next:
            idx+=1
            pointer = pointer.next
        return idx + 1
    
    def reverse(self):
        pointer = self.head
        new_list = linked_list()
        while pointer.next is not None:
            new_list.push(pointer.val)
            pointer = pointer.next
        new_list.push(pointer.val)
        return new_list
    
    def __str__(self):
        pointer = self.head
        vlist = [self.head.val]
        while pointer.next:
            pointer = pointer.next
            vlist.append(pointer.val)
        return vlist.__str__()
    
        
        

class Solution:
    
    def mergeKLists(lists):
        vals = []
        for i in lists:
            head = i.head
            while head:
                vals.append(head.val)
                head = head.next
        new_list = linked_list()
        for i in sorted(vals):
            new_list.append(i)
        return new_list
            
    #casual method
    def reverseList( head):
        pointer = head
        list_vals = []
        while pointer.next:
            list_vals.append(pointer.val)
            pointer = pointer.next
        list_vals.reverse()
        new_head = list_node()
        pointer = new_head
        for i in list_vals:
            tmp = list_node(i)
            pointer.next = tmp
            pointer = pointer.next
        return new_head
    
    def hasCircle(head):
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    
    def addTwoNumbers(l1, l2):
        h1, h2 = l1.head, l2.head
        res = linked_list()
        tmp = 0
        print(l1, l2)
        while any([h1 is not None, h2 is not None]):
            if h1 is None:
                h1tv = 0
            else:
                h1tv = h1.val
                h1 = h1.next
            if h2 is None:
                h2tv = 0
            else:
                h2tv = h2.val
                h2 = h2.next
            val = h1tv+h2tv+tmp
            tmp = 0
            if val>=10:
                tmp = 1
            res.append(val%10)
        if tmp==1:
            res.append(1)
        return linked_list(res)
    
    def addTwoNumbersH(l1, l2):
        res = point = list_node()
        tmp = 0
        while any([l1 is not None, l2 is not None]):
            if l1 is None:
                l1tv = 0
            else:
                l1tv = l1.val
                l1 = l1.next
            if l2 is None:
                h2tv = 0
            else:
                h2tv = l2.val
                l2 = l2.next
            val = l1tv+h2tv+tmp
            tmp = 0
            if val>=10:
                tmp = 1
            point.next = list_node(val%10)
            point = point.next
        res = res.next
        if tmp==1:
            point.next = list_node(1)
        return res

        
            
            
            
             
    #using list i write earlier
    
    
from numpy.random import randint



a = linked_list()
b = linked_list()

[a.push(9) for _ in range(7)]
[b.push(9) for _ in range(4)]
#a.push(3)
#a.push(4)
#a.push(2)
#b.push(4)
#b.push(6)
#b.push(5)
print(linked_list(Solution.addTwoNumbersH(a.head, b.head)))

a = linked_list()
b = linked_list()
c = linked_list()
[a.push(randint(10)) for _ in range(4)]
[c.push(randint(10)) for _ in range(7)]
[b.push(randint(10)) for _ in range(2)]
lists = [a, b, c]
print(Solution.mergeKLists(lists))



