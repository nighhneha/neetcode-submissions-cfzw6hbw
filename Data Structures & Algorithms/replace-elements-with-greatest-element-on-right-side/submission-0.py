class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        out =[]
        for i in range(len(arr)-1,-1,-1):
            out.append(maxi)
            maxi = max(arr[i],maxi)
        return out[::-1]