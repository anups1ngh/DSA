class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maxi = cur = 0
        for i,c in enumerate(s):
            if i>=k and s[i-k] in vowels:
                cur-=1
            if c in vowels:
                cur+=1
            maxi=max(maxi,cur)
        return maxi