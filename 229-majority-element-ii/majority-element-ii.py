class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1,el2=None,None
        cnt1,cnt2=0,0
        for i in range(len(nums)):
            if cnt1==0 and el2!=nums[i]:
                cnt1=1
                el1=nums[i]
            elif cnt2==0 and el1!=nums[i]:
                cnt2=1
                el2=nums[i]

            elif nums[i]==el1:
                cnt1+=1
            elif nums[i]==el2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=0
        cnt2=0
        for i in range(len(nums)):
            if el1==nums[i]:
                cnt1+=1
            if el2==nums[i]:
                cnt2+=1
        ls=[]
        miner=(len(nums)//3)+1
        if el1 is not None and cnt1>=miner:
            ls.append(el1)
        if el2 is not None and cnt2>=miner:
            ls.append(el2)

        return sorted(ls)