class Solution:
    def isLongPressedName(self, name, typed):
        if name == typed:
            return True
        if name[0] != typed[0]:
            return False
        lenname,lentyped = len(name),len(typed)
        i = j = 0
        while j < lentyped:
            if i < lenname and name[i] == typed[j]:
                i += 1
            elif typed[j] != typed[j - 1]:
                return False
            j += 1
        return i == lenname
