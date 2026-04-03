class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub =[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                if words[i] in words[j]:
                    sub.append(words[i])
                    break
        return sub