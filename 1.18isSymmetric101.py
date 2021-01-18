# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def ismirror(root1,root2):
            if ((not root1) and (not root2)):
                return True
            if not(root1 and root2):
                return False
            if root1.val == root2.val:
                return ismirror(root1.left,root2.right) and ismirror(root1.right,root2.left)
                
        return ismirror(root.left,root.right)
