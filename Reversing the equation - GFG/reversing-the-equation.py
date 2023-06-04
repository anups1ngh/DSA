#User function Template for python3
class Solution:
    def reverseEqn(self, s):
        # code here
        stack = []
        temp = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                temp+=s[i]
            else:
                stack.append(temp)
                stack.append(s[i])
                temp=""
        stack.append(temp)
        ans = ""
        stack = stack[::-1]
        return "".join(stack)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends