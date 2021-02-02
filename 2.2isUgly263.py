class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        while(True):
            if(num % 2 == 0):
                num /= 2
            elif(num % 3 == 0):
                num /= 3
            elif(num % 5 == 0):
                num /= 5
            elif(num == 1):
                return True
            else:
                return False
