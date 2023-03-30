class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,val in enumerate(nums):
            if target-nums[i] in d:
                return [i,d[target-nums[i]]]
            d[nums[i]] = i