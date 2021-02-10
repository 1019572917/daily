class Solution:
    def reverseVowels(self, s):
        length = len(s)
        l = 0
        r = length - 1
        yuanyin = ["a","e","i","o","u","A","E","I","O","U"]
        s = list(s)
        while(l < r):
            if s[l] not in yuanyin:
                l += 1
            if s[r] not in yuanyin:
                r -= 1
            if s[l] in yuanyin and s[r] in yuanyin:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
        return ''.join(s)
