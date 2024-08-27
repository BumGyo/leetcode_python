class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sign = 1
        i = 0
        length = len(s)

        while i < length and s[i] == ' ':
            i += 1

        if i < length and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
    
        while i < length and s[i].isdigit():
            num = num * 10 + int(s[i])
            if num * sign <= -2 ** 31:
                return -2 ** 31
            if num * sign >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            i += 1

        return num * sign