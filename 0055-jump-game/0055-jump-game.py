class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if len(nums) < 2:
        #     return True
        # jump_left = 0
        # for i in range(len(nums)):
        #     if i == len(nums) - 1:
        #         return True
        #     jump_left = max(jump_left,nums[i])
        #     if jump_left == 0:
        #         return False
        #     jump_left -=1
        # return True
        curr = nums[0]
        for i in range(1,len(nums)):
            if curr == 0:
                return False
            curr-=1
            curr = max(curr,nums[i])
        return True