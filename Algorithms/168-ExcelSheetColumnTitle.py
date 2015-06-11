#encoding=utf-8
#######################################################################
# Author: Acer                                                        #
# Created Time: 星期三  6/ 3 23:05:05 2015                            #
# File Name: 168-ExcelSheetColumnTitle.py                             #
# Description:                                                        #
# Solution:                                                           #
#######################################################################
class Solution:
    # @param: 
    # @return: 
    def convertToTitle(self, n):
        result = ''
        while n:
            result = chr(n % 26 + 64) + result
            n /= 26

        return result


