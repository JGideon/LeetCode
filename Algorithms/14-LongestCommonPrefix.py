class Solution:
    """
    @param String[] strs
    @return String
    """
    def longestCommonPrefix(self, strs):
        minLen = 99999
        commonPrefix = ''
        if not strs:
            return ''
#         if len(strs) is 1:
#             return strs[0]
#         for string in strs:
#             if string is '':
#                 return ''
#             minLen = min(len(string), minLen)
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1:
                    return commonPrefix
                if strs[0][i] != strs[j][i]:
                    return commonPrefix
            commonPrefix += strs[0][i]
        return commonPrefix


s = Solution()
strs = ['abcde', 'abcde', 'abc']
strs2= ["",""]
print(s.longestCommonPrefix(strs))
print("The Result: %s!" %s.longestCommonPrefix(strs2))
                
