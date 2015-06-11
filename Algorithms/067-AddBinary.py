#encoding=utf-8
"""
# Author: Acer
# Created Time: 一  5/25 14:31:28 2015
# File Name: 067-AddBinary.py
# Description:
# @param: string a
# @param: string b
# @return: string
"""
class Solution:
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        result = ''
        flag = 0
        while i >= 0 and j >= 0:
            res = int(a[i]) + int(b[j]) + flag
            if res >= 2:
               result = repr(res % 2) + result
               flag = 1
            else:
                result = repr(res) + result
                flag = 0
            i -= 1
            j -= 1
        while i >= 0:
            res = int(a[i]) + flag
            if res >= 2:
               result = repr(res % 2) + result
               flag = 1
            else:
                result = repr(res) + result
                flag = 0
            i -= 1
        while j >= 0:
            res = int(b[j]) + flag
            if res >= 2:
               result = repr(res % 2) + result
               flag = 1
            else:
                result = repr(res) + result
                flag = 0
            j -= 1
        if flag == 1:
            return '1' + result

        return result


s = Solution()
print(s.addBinary('1011', '1010'))
print(s.addBinary('100', '110010'))
