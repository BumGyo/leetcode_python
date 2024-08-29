class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        result = 0

        # 우선 인접한 두 수 중에 작은 수가 먼저 나오게 될 경우 다음 나오는 큰수에서 작은 수를 빼야함
        # 따라서 result에서 -=하면 됨
        # 큰 수가 먼저 나오게 될 경우 그냥 +=하면 됨

        for i in range(len(s)) :
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]] :
                result -= roman[s[i]]
            else :
                result += roman[s[i]]

        return result