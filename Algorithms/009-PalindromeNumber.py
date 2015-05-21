class Solution:
    # @param integer x
    # @return boolean
    def isPalindrome(self, x):
        totalBits = 0
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            originX = x
            while x > 0:
                totalBits += 1
                x = x / 10
            i = 1
            j = totalBits
            while i < j:
                print((originX / pow(10, i-1)) % 10)
                print((originX / pow(10, j-1)) % 10)
                if (originX / pow(10, i-1)) % 10 is not (originX / pow(10, j-1)) % 10:
                    return False
                i += 1
                j -= 1
            return True

s = Solution()
print(s.isPalindrome(12321))
print(s.isPalindrome(123321))
print(s.isPalindrome(12345))
print(s.isPalindrome(-12345))
print(s.isPalindrome(0))
