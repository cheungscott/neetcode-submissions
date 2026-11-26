# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur, depth):
            if not cur:
                return
            else:
                self.res = max(self.res, depth)
                left, right = dfs(cur.left, depth + 1), dfs(cur.right, depth + 1)
        dfs(root, 1)
        return self.res