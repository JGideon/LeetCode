#encoding=utf-8

class Solution:
    '''
    @param integer[] nums
    @return integer
    '''
    # del nums[i] is o(n) 时间复杂度
    def removeDuplicates1(self, nums):
        i = 0
        while i < (len(nums) - 1):
            if nums[i] is nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
    
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        tail = 0
        for i in range(1, len(nums)):
            if nums[tail] != nums[i]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1

s = Solution()
print("Len of unduplicated nums is %d" %s.removeDuplicates([]))

                

