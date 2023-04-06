class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        d1 = Counter(m)
        for char in r:
            if char in d1 and d1[char] > 0:
                d1[char] -= 1
                continue
            else:
                return False
        return True