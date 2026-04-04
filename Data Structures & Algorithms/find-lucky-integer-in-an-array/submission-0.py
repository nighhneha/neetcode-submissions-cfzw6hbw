class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = []
        for num in arr:
            if arr.count(num) == num:
                lucky.append(num)
        if lucky != []:
            return max(lucky)
        else:
            return -1