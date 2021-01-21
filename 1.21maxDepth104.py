# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if not root: return 0

        ans = 0
        if not root.left and not root.right: 	# 叶子节点
            ans = 1
        elif root.left and root.right:  # 左右子树均不为空
            ans = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        elif root.left:		# 左子树不为空 & 右子树为空
            ans = self.maxDepth(root.left) + 1
        else:			# 左子树为空 & 右子树不为空
            ans = self.maxDepth(root.right) + 1
        return ans
