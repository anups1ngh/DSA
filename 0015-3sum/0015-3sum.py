class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                add = nums[i]+nums[j]+nums[k]
                if add == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    k-=1
                    j+=1
                elif add<0:
                    j+=1
                else:
                    k-=1
        return list(ans)