class Solution:
    '''
    @param string s
    @return boolean
    '''
    def doesClosingMatchOpening(self, closing, opening):
        if closing is ')':
            return opening is '('
        if closing is ']':
            return opening is '['
        if closing is '}':
            return opening is '{'

    def isValid(self, s):
        openParentheses = ['{', '(', '[']
        closeParentheses = ['}', ')', ']']

        openParenthesesInStr = []
        for i in range(len(s)):
            if s[i] in openParentheses:
                openParenthesesInStr.append(s[i])
            elif s[i] in closeParentheses:
                if len(openParenthesesInStr) == 0:
                    return False
                if self.doesClosingMatchOpening(s[i], openParenthesesInStr[-1]):
                    openParenthesesInStr.pop()
                else:
                    return False
        return len(openParenthesesInStr) == 0 

s = Solution()
print(s.isValid('()'))
