#User function Template for python3

def reverseWord(s):
    ans = ""
    for i in range(1,len(s)+1):
        ans+=s[-i]
    return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends