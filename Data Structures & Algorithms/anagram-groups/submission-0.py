class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for x in strs:
            org = x
            x = tuple(sorted(x))
            if x not in d:
                d[x]=[]
                d[x].append(org)
            else:
                d[x].append(org)
        return list(d.values())