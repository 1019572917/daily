class Solution:
    def countPrimeSetBits(self, L, R):
        zhi = [2,3,5,7,11,13,17,19]
        answer = 0
        for i in range(L,R+1):
            n = bin(i).count("1")
            if n in zhi:
                answer += 1
        return answer
