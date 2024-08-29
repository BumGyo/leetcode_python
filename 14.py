class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # �ƹ��͵� ������ "" ���� 
        if not strs :
            return ""
        
        # prefix�� ù ��° ����(�ܾ�)�� 
        prefix = strs[0]

        # �ι�° �ε������� �ݺ�����(prefix�� ù��°�� �ʱ�ȭ�����Ƿ�)
        for string in strs[1:]:
            # �ι�° �ε������� prefix�� 0�� �ƴҶ�����(���Ë�����) �ݺ�
            while string.find(prefix) != 0:
                # prefix(�ʱⰪ : ������ ù��° ����)�� �ڿ��� ���� �� ���ھ� ����
                prefix = prefix[:-1]
                # prefix�� �������� ��ã�� ���̹Ƿ� "" ����
                if not prefix :
                    return ""

        return prefix