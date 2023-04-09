class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        d = {'(':')','[':']','{':'}'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif not stack or d[stack.pop()] != c:
                return False
        if not stack:
            return True
        return False