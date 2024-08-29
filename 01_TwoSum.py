class Solution(object):
    def twoSum(self, nums, target):
        # ���ڸ� �ε����� �����ϴ� �ؽ� ���̺� ����
        numToIndex = {}

        for i in range(len(nums)):
            # ���� ���� ���ڿ� target�� ���� �ؽ����̺� �ִ� ���
            if target - nums[i] in numToIndex :
                # �ش� ���ڿ� ���̰� �Ǵ� ������ �ε��� ��ȯ
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []