# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr):
            if not curr:
                return

            if curr.val == p.val or curr.val == q.val:
                return curr

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left or right:
                if left and right:
                    return curr
                elif left:
                    return left
                else:
                    return right

        return dfs(root)

            