# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root: return 0

        ans = 0
        if not root.left and not root.right: 	# 叶子节点
            ans = 1
        elif root.left and root.right:  # 左右子树均不为空
            ans = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:		# 左子树不为空 & 右子树为空
            ans = self.minDepth(root.left) + 1
        else:			# 左子树为空 & 右子树不为空
            ans = self.minDepth(root.right) + 1
        return ans
