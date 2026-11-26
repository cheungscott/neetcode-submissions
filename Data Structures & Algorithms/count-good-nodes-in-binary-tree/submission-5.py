# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(cur, maxVal):
            if not cur:
                return
            if cur.val >= maxVal:
                self.count += 1
                maxVal = cur.val
            left, right = dfs(cur.left, maxVal), dfs(cur.right, maxVal)
    
        dfs(root, root.val)
        return self.count
            