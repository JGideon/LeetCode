#encoding=utf-8
class Solution():
    '''
    @param integer[] nums
    @param integer val
    @return integer
    @date 2015-5-20 10:44 am
    '''
    def removeElementF(self, nums, val):
        j = len(nums)
        for num in nums:
            if num is val:
                j -= 1
        newLen = j
        for i in range(j):
            if num is val:
                num = nums[j]
                j += 1
        print(nums)
        return newLen
    
    def removeElement(self, nums, val):
        tail = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[tail] = nums[i]
                tail += 1
        print(nums)
        return tail 

s = Solution()
nums = [1,2,3,4,4,5,6,7]
print(s.removeElement(nums, 4))
