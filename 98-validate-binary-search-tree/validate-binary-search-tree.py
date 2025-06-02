# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,low,node,high):
        if not node:
            return True
        if not (low<node.val<high):
            return False
        return self.dfs(low,node.left,node.val) and self.dfs(node.val,node.right,high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float("-inf"),root,float('inf'))
        
