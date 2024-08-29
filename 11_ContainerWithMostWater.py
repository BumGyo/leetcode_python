class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        TIME OUT CODE

        result = 0

        for i in range(len(height)) :
            for j in range(i + 1, len(height)) :
                area = (j - i) * min(height[i], height[j])
                result = max(area, result)

        return result
        """

        result = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(area, result)
        
            if height[l] < height[r]:
                l += 1
            else :
                r -= 1

        return result