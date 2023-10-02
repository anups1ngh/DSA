class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == k:
            return k
        n = len(nums)
        searchQuery = []
        for i in range(k):
            searchQuery.append(i+1)
        for i in range(n-1,-1,-1):
            if nums[i] in searchQuery:
                searchQuery.remove(nums[i])
            if len(searchQuery) == 0:
                return n-i
        return n