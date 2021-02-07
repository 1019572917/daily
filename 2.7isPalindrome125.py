class Solution:
    def isPalindrome(self, s):
        answer = []
        for i in s:
            if i.isdigit() or i.isalpha():
                answer.append(i.upper())
        return answer == answer[::-1]
