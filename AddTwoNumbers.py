class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class ListNode:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def __str__(self):
        if not self.head:
            return "Null"
        else:
            temp = self.head
            result = []
            while temp:
                result.append(str(temp.val))
                temp = temp.next
            return "->".join(result)
        
class Solution:
    def addTwoNumbers(self,l1,l2):
         pass 