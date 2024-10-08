class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 #A
            j = half - i - 2        #B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # ��Ƽ���� ������
            if Aleft <= Bright and Bleft <= Aright :
                # Ȧ��
                if total % 2:
                    return min(Aright, Bright)
                # ¦��
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1