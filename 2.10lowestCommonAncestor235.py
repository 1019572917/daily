# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ans = root 
        while True:
            if p.val > ans.val and q.val > ans.val:
                ans = ans.right
            if p.val < ans.val and q.val < ans.val:
                ans = ans.left
            else:
                break
        return ans
