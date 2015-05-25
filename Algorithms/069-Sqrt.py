class Solution: 
    def mySqrt(self, x):
        right = x / 2 
        left = 0
        while left <= right:
            middle = (left + right) / 2 + 1
            result = middle * middle 
            if result < x:
                left = middle + 1
            elif result > x:
                right = middle - 1
            else:
                return middle

s = Solution()
print(s.mySqrt(1))
