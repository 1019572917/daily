class Solution:
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        l,n = len(haystack),len(needle)
        for start in range(l - n + 1):
            if haystack[start:start + n] == needle:
                return start
