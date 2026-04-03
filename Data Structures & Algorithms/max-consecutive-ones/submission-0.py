class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,res=0,0
        for i in nums:
            if i==1:
                count += 1
                res = max(res,count)
            else:
                count = 0
        return res