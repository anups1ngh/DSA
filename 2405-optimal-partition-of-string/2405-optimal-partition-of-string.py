class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        sub_str = ''
        for i in range(len(s)):
            if len(sub_str) == 0:
                sub_str+=s[i]
            elif s[i] not in sub_str:
                sub_str+=s[i]
            else:
                sub_str = s[i]
                ans+=1
        return ans+1