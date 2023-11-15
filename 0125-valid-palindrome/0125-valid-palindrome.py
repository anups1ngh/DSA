class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(i for i in s.lower() if i.isalnum())
        mid = len(temp)//2
        l = len(temp)
        if l%2 != 0:
            return temp[:mid] == temp[mid+1:][::-1]
        else:
            return temp[:mid] == temp[mid:][::-1]