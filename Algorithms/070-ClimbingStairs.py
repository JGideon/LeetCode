#encoding=utf-8
"""
# Author: Acer
# Created Time: 星期二  6/ 2 23:07:33 2015
# File Name: 070-ClimbingStairs.py
# Description:
# @param: 
# @return: 
"""
class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 0

        prev, curr = 0, 1
        for i in range(n):
            tmp = curr
            curr += prev
            prev = tmp
        return curr

        
