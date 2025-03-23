# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        q=deque([[root,1,0]])#[node,idx,level]
        previdx=1
        prevlvl=0
        while q:
            miner=q[0][1]
            node,idx,lvl=q.popleft()
            if lvl>prevlvl:
                prevlvl=lvl
                previdx=idx
            res=max(res,idx-previdx+1)
            if node.left:
                q.append([node.left,2*(idx-previdx),lvl+1])

            if node.right:
                q.append([node.right,2*(idx-previdx)+1,lvl+1])

        return res

        