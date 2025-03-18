# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        maper=defaultdict(list)
        node=deque([(root,0,0)])
        while node:
            data,vlvl,lvl=node.popleft()
            maper[vlvl].append((lvl,data.val))

            if data.left:
                node.append((data.left,vlvl-1,lvl+1))
            if data.right:
                node.append((data.right,vlvl+1,lvl+1))

        res=[]
        for vlvl in sorted(maper.keys()):
            nodes=sorted(maper[vlvl])
            temp=[]
            for i , val in nodes:
                temp.append(val)
            res.append(temp)
        return res
        