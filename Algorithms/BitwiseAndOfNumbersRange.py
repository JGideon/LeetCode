class Solution:
    # @param {integer} m
    # @param {interger} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        result = 2147483647
        if m > result or n >result or m > n:
            return -1
        for i in range(m, n+1):
            result &= i
        return result

s = Solution()
print(s.rangeBitwiseAnd(0, 2147483647))
