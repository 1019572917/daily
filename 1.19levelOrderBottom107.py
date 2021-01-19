# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        answer = []
        def add(root,depth):
            if not root:
                return []
            if len(answer) < depth + 1:
                answer.append([])
            answer[depth].append(root.val)
            add(root.left,depth + 1)
            add(root.right,depth + 1)
        add(root,0)
        return answer[::-1]
