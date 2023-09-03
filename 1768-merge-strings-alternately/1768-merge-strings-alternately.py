class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i  = j = 0
        ans = ""
        while i < len(word1) and j< len(word2):
            ans+=word1[i]
            i+=1
            ans+=word2[j]
            j+=1
        if i<len(word1):
            ans+=word1[i:]
            i+=1
        if j<len(word2):
            ans+=word2[j:]
        return ans