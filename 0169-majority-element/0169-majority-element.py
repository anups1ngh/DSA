class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]
        for i in range(1,len(nums)):
            if count == 0:
                majority = nums[i]
                count +=1
            elif nums[i] == majority:
                count+=1
            else:
                count-=1
        return majority