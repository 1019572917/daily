class Solution:
    def letterCasePermutation(self, S):
        def recall(S,index):
            answer.append(''.join(S))
            for i in range(index,len(S)):
                if S[i].isupper():
                    S[i] = S[i].lower()
                    recall(S, i + 1)
                    S[i] = S[i].upper()
                elif S[i].islower():
                    S[i] = S[i].upper()
                    recall(S, i + 1)
                    S[i] = S[i].lower()
        index = 0
        answer = []
        S = list(S)
        recall(S,index)
        return answer
