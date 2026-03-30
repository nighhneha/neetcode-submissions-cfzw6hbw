class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for x in range(len(s)-1):
            '''n1 = ord(s[x])
            n2 = ord(s[x+1])'''
            total = total + abs(ord(s[x])-ord(s[x+1]))
        return total
        