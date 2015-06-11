#encoding=utf-8
"""
# Author: Acer
# Created Time: 一  5/25 19:35:41 2015
# File Name: 029-DivideTwoNumbers.py
# Description:
# @param: integer dividend
# @param: integer divisor
# @return: integer 
"""
class Solution:
    # divide1时间复杂度为o(n)
    def divide1(self, dividend, divisor):
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return MAX_INT
        count = 0
        flag = 0
        if ((dividend <= 0) == (divisor <= 0)):
            flag = 0
        else:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            count += 1

        return -count if flag else count
    
    # divide时间复杂度为o(logn)
    def divide(self, dividend, divisor):
        pass

s = Solution()
print(s.divide(-100, -10))
