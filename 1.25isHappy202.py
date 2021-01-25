class Solution:
    def isHappy(self, n):
        list1 = [1]
        while n not in list1:
            list1.append(n)
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum
        return n == 1
