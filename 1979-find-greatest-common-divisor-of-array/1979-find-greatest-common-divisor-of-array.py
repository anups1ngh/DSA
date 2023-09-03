class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        for i in range(mini,0,-1):
            if mini%i==0 and maxi%i == 0:
                return i