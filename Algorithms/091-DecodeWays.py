class Solution(object):
    def numDecoding(self, s):
        if not s:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        result = [0] * len(s)
        result[0] = 1

        result[1] = 1
        if s[1] == '0':
            if s[0] > '2':
                result[1] = 0
        else:
            if s[:2] <= '26':
                result[1] = 2

        for i in range(2, len(s)):
            if s[i] != '0':
                result[i] += result[i-1]

            if s[i-1: i+1] <= '26' and s[i-1: i+1] >= '1':
                result[i] += result[i-2]
        return result[len(s) - 1]

s1 = '1'
s2 = '110'
s3 = '101'
s4 = '001'
s5 = '100'
s6 = '27'
s = Solution()
print(s.numDecoding(s1))
print(s.numDecoding(s2))
print(s.numDecoding(s3))
print(s.numDecoding(s4))
print(s.numDecoding(s5))
print(s.numDecoding(s6))

