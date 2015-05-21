class Solution():
    #@param String haystack
    #@param String needle
    #@return integer
    #@date 2015-05-21 9:52
    def strInStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        i = len(haystack) - 1
        j = len(needle) - 1
        
        while j != 0 and i != 0:
            while i != 0:
                if haystack[i] != needle[j]:
                    i -= 1
                break
            
    def strInStr1(self, haystack, needle):
        if not needle: 
            return 0
        if not haystack:
            return -1
        i = 0
        j = 0 
        start = 0

        while i < len(haystack):
            if haystack[i] is not needle[0]:
                i += 1
            break
        start = i
        while i < len(haystack) and j < len(needle):
            if haystack[i] is needle[j]:
                i += 1
                j += 1
            else:
                return -1
        if j < len(needle):
            return -1
        return start

haystack = 'abcdefg'
needle = 'bcde'
h1 = n1 = ''
h2 = 'a'
s = Solution()
print(s.strInStr(haystack, needle))
print(s.strInStr(h1, n1))
print(s.strInStr(h2, n1))
