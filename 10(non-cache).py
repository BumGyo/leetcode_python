class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def dfs(i, j) :
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
                return (dfs(i, j + 2) or             # *�� �ǳ� �ٱ� ���ؼ�
                        (match and dfs(i + 1, j)))   # match�� ������ �¾����� *�� ���
            # ���� ���ڰ� ���� ��� ���� ���ڷ�
            if match :
                return dfs(i + 1, j + 1)
            return False

        return dfs(0, 0)
        