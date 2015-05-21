class Solution:
    def largestNumber(self, nums):
        singleNums = []
        for num in nums:
            if num < 10:
                singleNums.append(str(num))
            else:
                while num != 0:
                    singleNums.append(str(num % 10))
                    num /= 10
        singleNums.sort(reverse=True)
        print(''.join(singleNums))

s = Solution()
s.largestNumber([1,0])
