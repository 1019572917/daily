class Solution:
    def findComplement(self, num):
        temp = 1
        while(temp < num):
            temp <<= 1
            temp += 1
        return num^temp
