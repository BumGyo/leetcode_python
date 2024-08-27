class Solution(object):
    def twoSum(self, nums, target):
        # 숫자를 인덱스에 매핑하는 해시 테이블 선언
        numToIndex = {}

        for i in range(len(nums)):
            # 만약 현재 숫자와 target의 차가 해시테이블에 있는 경우
            if target - nums[i] in numToIndex :
                # 해당 숫자와 차이가 되는 숫자의 인덱스 반환
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []