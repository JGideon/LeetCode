#encoding=utf-8
"""
# Author: Acer
# Created Time: 星期五  5/29 16:10:46 2015
# File Name: 016-3SumClosest.py
# Description:
# @param: Integer[] nums
# @param: Integer target
# @return: Integer
"""
class Solution:
    def threeSumClosest(self, nums, target):
        minDiff = 9999999
        finalResult = 0
        i = 0
        while i < len(nums) - 2:
            result = nums[i] + nums[i + 1] + nums[i + 2]
            diff = abs(result - target)
            if diff < minDiff:
                minDiff = diff
                finalResult = result
                
        return finalResult
