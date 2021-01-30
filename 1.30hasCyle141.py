# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        m = {}
        while(head):
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False
