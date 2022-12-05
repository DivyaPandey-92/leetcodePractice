# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        values=[]

        def dfs(root, values):

            if not root:
                return None

            left=dfs(root.left, values)
            values.append(root.val)
            right=dfs(root.right, values)
            return values

        inorder=dfs(root, values)
        return inorder[k-1]