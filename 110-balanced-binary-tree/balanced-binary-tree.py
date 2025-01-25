# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:#dfs approach
        def dfs(curr) -> list:

            if curr is None:
                return [True,0]
            lh=dfs(curr.left)
            rh=dfs(curr.right)

            blcd= lh[0] and rh[0] and abs(lh[1] -rh[1])<=1 #bool value which check for the left and right subtree if there bool value is same or we can say its true or not if the left sub tree is not a balanced tree and for similar we check for the right subtree

            return [blcd,1+max(lh[1],rh[1])]

        return dfs(root) [0]
        