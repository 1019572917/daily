class Solution:
    def diStringMatch(self, S):
        length = len(S) + 1
        end = length - 1
        start = 0
        answer = []
        for i in range(length):
            if i == length - 1:
                answer.append(start)
            elif S[i] == "I":
                answer.append(start)
                start += 1
            elif S[i] == "D":
                answer.append(end)
                end -= 1
        return answer
