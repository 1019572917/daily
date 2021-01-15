class Solution:
    def findTheDifference(self, s, t):
        answer = 0
        for i in s:
            answer ^= ord(i)
        for i in t:
            answer ^= ord(i)
        return chr(answer)
