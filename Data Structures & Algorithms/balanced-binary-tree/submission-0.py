# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0

            lh = dfs(curr.left)
            rh = dfs(curr.right)

            if lh == -1 or rh == -1:
                return -1

            if abs(lh-rh) > 1:
                return -1

            return 1 + max(lh, rh)

        res = dfs(root)
        return res != -1
