# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        answer = []
        cur = head
        while cur:
            answer.append(cur.val)
            cur = cur.next
        return answer == answer[::-1]
