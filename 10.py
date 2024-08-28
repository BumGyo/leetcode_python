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
            
            # s�� �� ���ھ� Ȯ���ϴ� i�� p�� �ѹ��ھ� Ȯ���ϴ� j�� 
            # ���� �� ���̸� �ʰ��ߴٴ� ���� match�ƴٴ� ��
            if i >= len(s) and j >= len(p) :
                return True
            # j�� ���̸� �ʰ��ߴٴ� ���� s�� match�� �����ߴٴ� ��
            if j >= len(p) :
                return False

            # i�� s�� ���̺��� �۰� s�� p�� �ѹ��ڰ� ���� ��ġ�ϰų� p�� .�� ���(.�� ��� ���� ����)
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # j�� ���� ���ڰ� ���� ���
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or             # *�� �ǳ� �ٱ� ���ؼ�
                        (match and dfs(i + 1, j)))   # match�� ������ �¾����� *�� ���
                return cache[(i, j)]
            # ���� ���ڰ� ���� ��� ���� ���ڷ�
            if match :
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)