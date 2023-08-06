class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) <= nums[-1]:
            return False
        elif nums[-1] != nums[-2] != len(nums)-1:
            return False
        elif len(nums) > nums[-1] + 1:
            return False
        for i in range(len(nums)-1):
            if nums[i] == i+1:
                continue
            else:
                return False
        return True