class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 2 ** 31 -1
        MIN = -2 ** 31
        
        if x >= MAX or x <= MIN:    
            return 0

        else :
            str_x = str(x)

            if x >= 0 :
                rev_x = str_x[::-1]

            else :
                tmp = str_x[1:]     # ù��° �ε����� '-'����
                tmp2 = tmp[::-1]    # �������� ����
                rev_x = '-' + tmp2  # �ٽ� '-'�߰�

            if int(rev_x) >= MAX or int(rev_x) <= MIN : 
                return 0
                
            else : 
                return int(rev_x)