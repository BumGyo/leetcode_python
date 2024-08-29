class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        cache = {}

        def dfs(i, j) :
            if (i, j) in cache:
                return cache[(i, j)]
            
            # s를 한 문자씩 확인하는 i와 p를 한문자씩 확인하는 j가 
            # 서로 그 길이를 초과했다는 말은 match됐다는 것
            if i >= len(s) and j >= len(p) :
                return True
            # j만 길이를 초과했다는 말은 s와 match가 실패했다는 것
            if j >= len(p) :
                return False

            # i가 s의 길이보다 작고 s와 p의 한문자가 서로 일치하거나 p가 .일 경우(.은 모든 문자 가능)
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # j의 다음 문자가 별일 경우
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or             # *를 건너 뛰기 위해서
                        (match and dfs(i + 1, j)))   # match가 조건이 맞았으면 *를 사용
                return cache[(i, j)]
            # 서로 문자가 같을 경우 다음 문자로
            if match :
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)