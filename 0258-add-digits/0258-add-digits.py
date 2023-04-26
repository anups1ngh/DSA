class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        while temp > 9:
            t1 = temp
            add = 0
            while t1>0:
                add += t1%10
                t1 = t1//10
            temp = add
        return temp