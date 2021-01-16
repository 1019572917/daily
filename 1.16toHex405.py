class Solution:
    def toHex(self, num):
        answer = ""
        if num == 0:
            return "0"
        if num < 0:
            num =  (abs(num) ^ ((2 ** 32) - 1)) + 1
        while num > 0:
            a = num % 16
            if a > 9:
                a = chr(a+87)
            else:
                a = str(a)
            answer += a
            num >>= 4
        return answer[::-1]
