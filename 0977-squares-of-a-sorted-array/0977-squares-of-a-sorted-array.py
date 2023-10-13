class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [int(x*x) for x in nums]
        return sorted(sq)