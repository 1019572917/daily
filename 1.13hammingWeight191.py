class Solution:
    def hammingWeight(self, n):
        count = 0
        for i in bin(n):
            print(i)
            if i == "1":
                count += 1
        return count
