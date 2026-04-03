class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sub =[]
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    sub.append(words[i])
                    break
        return sub