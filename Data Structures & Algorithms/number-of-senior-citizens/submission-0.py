class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num = 0
        for x in details:
            if int(x[11:13]) > 60:
                num += 1
        return num