class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 아무것도 없으면 "" 리턴 
        if not strs :
            return ""
        
        # prefix를 첫 번째 문자(단어)로 
        prefix = strs[0]

        # 두번째 인덱스부터 반복해줌(prefix를 첫번째로 초기화했으므로)
        for string in strs[1:]:
            # 두번째 인덱스부터 prefix가 0이 아닐때까지(나올떄까지) 반복
            while string.find(prefix) != 0:
                # prefix(초기값 : 완전한 첫번째 문자)를 뒤에서 부터 한 문자씩 지움
                prefix = prefix[:-1]
                # prefix가 없어지면 못찾은 것이므로 "" 리턴
                if not prefix :
                    return ""

        return prefix