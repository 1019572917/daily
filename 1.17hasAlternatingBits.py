class Solution:
    def hasAlternatingBits(self, n):
        length = len(bin(n))
        list1 = list(bin(n))
        for i in range(2,length - 1):
            if list1[i] == list1[i + 1]:
                return False
        return True
