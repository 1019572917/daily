class Solution:
    def countPrimeSetBits(self, L, R):
        count = 0
        for i in range(L,R+1):
            list1 = bin(i)
            num = list1.count("1")
            if num > 1:
                for j in range(2,num):
                    if num % j == 0:
                        break
                else:
                    count += 1
        return count
