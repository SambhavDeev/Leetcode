# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):
        if root is None:
            return 
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)

        return arr
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        arr=[]
        self.inorder(root,arr)
        return arr[k-1]

        