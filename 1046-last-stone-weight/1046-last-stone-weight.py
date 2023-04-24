class Solution:
    def lastStoneWeight(self, A: List[int]) -> int:
        a = [-x for x in A]
        heapq.heapify(a)
        while len(a) > 1 and a[0] != 0:
            heapq.heappush(a, heapq.heappop(a) - heapq.heappop(a))
        return -a[0]