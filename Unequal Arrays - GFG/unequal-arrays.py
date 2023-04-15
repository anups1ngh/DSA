from typing import List
from collections import defaultdict
class Solution:
    def solve(self, N: int, A: List[int], B: List[int]) -> int:
        ssum = sum(a - b for a, b in zip(A, B))
        ap = defaultdict(list)
        bp = defaultdict(list)
        for a, b in zip(A, B):
            ap[abs(a) % 2].append(a)
            bp[abs(b) % 2].append(b)
        
        if ssum != 0 or len(ap[0]) != len(bp[0]):
            return -1
        
        ans = 0
        for i in range(2):
            ap[i] = [x for x in sorted(ap[i])]
            bp[i] = [x for x in sorted(bp[i])]
            
            for j, (a, b) in enumerate(zip(ap[i], bp[i])):
                ans += abs(a - b) // 2
            
        return ans // 2
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends