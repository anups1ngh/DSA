class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            temp=""
            l = len(w)
            for j in range(l):
                if w[j] == separator and len(temp) > 0:
                    ans.append(temp)
                    temp = ""
                elif w[j] == separator:
                    continue
                else:
                    temp+=w[j]
            if len(temp)>0:
                ans.append(temp)
        return ans