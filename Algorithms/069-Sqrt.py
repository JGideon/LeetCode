class Solution: 
    def mySqrt(self, x):
        right = x / 2 + 1
        left = 0
        while left <= right:
            middle = (left + right) / 2
            result = middle * middle 
            if result < x:
                left = middle + 1
            elif result > x:
                right = middle - 1
            else:
                return middle
        return (left + right) / 2

s = Solution()
print(s.mySqrt(1))
print(s.mySqrt(3))
print(s.mySqrt(10000000000000000))
