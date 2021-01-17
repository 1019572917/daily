class Solution:
    def findComplement(self, num):
        length = len(bin(num))
        return 2 ** (length - 2) - num - 1
