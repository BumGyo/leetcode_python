class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        reversed_num = 0
        tmp = x

        while tmp != 0:
            digit = tmp % 10
            reversed_num = reversed_num * 10 + digit
            tmp //= 10
        
        return reversed_num == x