class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for c,d in zip(word1,word2):
            ans+=c
            ans+=d
        if len(word1) > len(word2):
            ans+=word1[len(word2):]
        else:
            ans+=word2[len(word1):]
        return ans