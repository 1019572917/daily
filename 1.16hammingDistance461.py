class Solution:
    def hammingDistance(self, x, y):
        count = 0
        res = x ^ y
        while res>0:
            res &= (res- 1)
            count += 1
        return count
