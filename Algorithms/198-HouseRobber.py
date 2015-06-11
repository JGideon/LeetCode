class Solution:
    # @param: {Integer []} nums
    # @return: {integer}
    def rob(self, nums):
        size = len(nums)
        result = [0] * (size + 1)

        if size:
            result[1] = nums[0]

        for i in range(2, size + 1):
            result[i] = max(result[i-2] + nums[i-1], result[i-1])

        return result[size]


s = Solution()
print( s.rob([1,2,3]) )
