class Solution:
    def reverseBits(self, n):
        answer = 0
        count = 0
        while count < 32:
            answer <<= 1
            answer += (n & 1)
            n >>= 1
            count += 1
        return answer
