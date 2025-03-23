from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root): #next level code 
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        q=deque([[root,0]])#node,level
        prev=0
        curr=[]
        while q:
            
            node,lvl=q.popleft()
            if lvl>prev:
                
                res.append(curr)
                curr=[]
                prev=lvl
            if node:
                curr.append(node.val)
            if node and node.left is not None:
                q.append([node.left,lvl+1])
            if node and node.right is not None:
                q.append([node.right,lvl+1])
        res.append(curr)
        return res
        