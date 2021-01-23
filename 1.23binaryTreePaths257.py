# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        def findPath(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:#叶子节点
                    answer.append(path)
                else:
                    path += "->" 
                    findPath(root.left,path)
                    findPath(root.right,path)
        answer = []
        findPath(root,"")
        return answer
