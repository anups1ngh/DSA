class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for key,value in zip(c.keys(),c.values()):
            if value == 1:
                ans = s.index(key)
                return ans
        return -1