#coding=utf-8
'''
1.题目假设数组为已排序数组
'''
class Solution:
    # @param integer[] nums
    # @parem integer target
    # @return integer[]
    def twoSum(self, nums, target):
        scanned = {}
        count = 0
        for j, item in enumerate(nums, 1):
            print(count)
            count += 1
            i = scanned.get(target - item, -1)
            if i > 0:
                return [i, j]
            scanned[item] = j
    def twoSum3(self, nums, target):
        for i in range(len(nums)):
            left = i
            right = len(nums) - 1
            middle = int((left + right) / 2) + 1
            while left < right: 
                if nums[middle] == target - nums[i]:
                    return (i+1, middle+1)
                elif nums[middle] > target - nums[i]:
                    right = middle - 1
                    middle = int((left + right) / 2)
                else:
                    left = middle + 1
                    middle = int((left + right) / 2)

        return None



    def twoSum2(self, nums, target):
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
# print(s.twoSum([1,2,3,4,5,6], 7))
print(s.twoSum([3,2,4], 6))
