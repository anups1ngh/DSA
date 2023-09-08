class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        jump_left = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            jump_left = max(jump_left,nums[i])
            if jump_left == 0:
                return False
            jump_left -=1
        return True