'''
@学到的东西：
1. 更加熟悉列表的切片；尤其是步长为负数的时候
2. nums[:] = newNums和nums = newNums的区别
'''
class Solution:
    '''
    @param integer [] nums
    @param integer k
    @return void
    '''
    def rotate(self, nums, k):
        nums[:] = (nums[len(nums)-k-1::-1] + nums[:len(nums)-k-1:-1])[::-1]
        print(nums)

s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 4)
