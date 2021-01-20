# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x, y):
        depth = {}
        parent = {}

        def find(node,par = None):
            if node:
                if par:
                    depth[node.val] = depth[par.val] + 1
                else:
                    depth[node.val] = 0
                parent[node.val] = par
                find(node.left,node)
                find(node.right,node)
        
        find(root)
        return depth[x] == depth[y] and parent[x] != parent[y]
