class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        farthest = 0
        upper_limit = 0
        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if farthest >= len(nums)-1:
                ans += 1
                break
            if i == upper_limit:
                ans += 1
                upper_limit = farthest
        return ans
    
#         ans = 0
#         end = 0
#         farthest = 0

#         # Implicit BFS
#         for i in range(len(nums) - 1):
#             farthest = max(farthest, i + nums[i])
#             if farthest >= len(nums) - 1:
#                 ans += 1
#                 break
#             if i == end:      # Visited all the items on the current level
#                 ans += 1        # Increment the level
#                 end = farthest  # Make the queue size for the next level

#         return ans