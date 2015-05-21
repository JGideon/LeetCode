#coding=utf-8
'''
1.题目假设数组为已排序数组
'''
class Solution:
    # @param integer[] nums
    # @parem integer target
    # @return integer[]
    def twoSum(self, nums, target):
        lenNums = len(nums)
        for i in range(lenNums):
            j = (lenNums + i - 1) / 2
            while j > i and j < lenNums:
                if nums[j] + nums[i] == target:
                    return (i+1, j+1)
                elif nums[j] > target - nums[i]:
                    j = (i + j - 1) / 2
                else:
                    j = (j + lenNums) / 2
    def twoSum1(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] is target:
                    return (i+1, j+1)

s = Solution()
print(s.twoSum([1,2,3,4,5,6], 7))
