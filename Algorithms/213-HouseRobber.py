
class Solution:
    # @param: {Integer[]} numbers
    # @return: {Integer}
    def robII(self, numbers):
        return max(self.rob(numbers, 0, len(numbers) - 1), self.rob(numbers, 1, len(numbers)))

    def rob(self, numbers, left, right):
        preBenefit, benefit = 0, 0

        for i in range(left, right):
            tmp = benefit
            benefit = max(benefit, preBenefit + numbers[i])
            preBenefit = tmp

        return benefit

s = Solution()
s.robII([2,1,5,4])
