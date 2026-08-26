# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        def dfs(root, maxVal):
            if not root:
                return 0
            
            if root.val >= maxVal:
                self.goodNodes += 1
                maxVal = root.val
            
            left, right = dfs(root.left, maxVal), dfs(root.right, maxVal)
        dfs(root, root.val)
        return self.goodNodes