#encoding=utf-8
###########################################################
# Author: Acer                                            #
# Created Time: 星期三  6/ 3 09:34:52 2015                #
# File Name: 191-NumbersOfOneBits.py                      #
# Description:                                            #
# Aim:                                                    # 
#   一个数字以二进制表示的时候计算其中1的位数             #
# Solution:                                             　#
#   每次和求与&,然后左移一位，直到n为0                    #
###########################################################
class Solution:
    # @param integer n: 
    # @return integer: 
    def hammingWeight(self, n):
        result = 0
        while n:
            result += n % 2
            n /= 2
        return result
