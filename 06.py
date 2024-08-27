class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 열의 수가 1이거나 열의 수가 문자의 길이보다 길 경우 문자 return
        if numRows == 1 or numRows >= len(s) :
            return s

        rows = [[] for _ in range(numRows)]
        index = 0
        step = 1
        
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)