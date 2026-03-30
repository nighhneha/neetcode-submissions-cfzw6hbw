class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for x in t:
            if i<len(s) and x == s[i]:
                i+=1
        if i==len(s) or s==' ':
            return True
        return False