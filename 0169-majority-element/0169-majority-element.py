class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]
        for n in nums[1:]:
            if n == majority:
                count+=1
            elif count < 1:
                majority = n
                count+=1
            elif n != majority:
                count-=1
        return majority                