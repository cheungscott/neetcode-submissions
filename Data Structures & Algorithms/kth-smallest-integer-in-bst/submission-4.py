# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []

        def dfs(cur):
            if not cur:
                return
            
            left = dfs(cur.left)
            self.res.append(cur.val)
            right = dfs(cur.right)
        dfs(root)
        return self.res[k-1] 

        