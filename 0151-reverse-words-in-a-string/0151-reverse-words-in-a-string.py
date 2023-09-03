class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]
        ans = ""
        for w in s:
            if len(w) > 0:
                if len(ans) > 0:
                    ans+= " "
                ans = ans+ w
        return ans