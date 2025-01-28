# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxer):
            if node is None:
                return 0
            res=1 if node.val>=maxer else 0
            maxer=max(node.val,maxer)

            res+=dfs(node.left,maxer)
            res+=dfs(node.right,maxer)

            return res
        
        return dfs(root,root.val)

