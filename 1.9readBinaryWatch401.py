class Solution:
    def readBinaryWatch(self, num):
        answer = []
        def count1(num):
            count = 0
            while num != 0:
                num = num & (num - 1)
                count += 1
            return count

        for i in range(12):
            for j in range(60):
                if count1(i) + count1(j) == num:
                    if j < 10:
                        s = str(i) + ':' + '0' + str(j)
                    else:
                        s = str(i) + ':' + str(j)
                    answer.append(s)
        return answer
