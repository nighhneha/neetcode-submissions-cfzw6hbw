class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for x in nums:
            if x==target:
                out = nums.index(x)
                break
            else:
                out = -1
        return out