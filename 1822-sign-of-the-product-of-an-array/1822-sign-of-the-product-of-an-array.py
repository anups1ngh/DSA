class Solution:
    def signFunc(self,n):
        if n==0:
            return 0
        elif n>0:
            return 1
        elif n<0:
            return -1
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            ans*=i
        return self.signFunc(ans)