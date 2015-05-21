"""
1.Int类型是32位的，范围为(-2^31, 2^31 - 1),得注意翻转后是否超出Int类型范围。
2.Int类型的List不能使用join函数
3.python里: ？三元运算符为(a > b) and a or b
"""
class Solution:
    def reverse(self, x):
        reverseList = []
        if x is 0:
            return 0
        elif x < 0:
            x = -x
            while x > 0:
                reverseList.append(str(x % 10))
                x = x / 10
            return -int(''.join(reverseList)) >= -2147483648 and -int(''.join(reverseList)) or 0
        elif x > 0:
            while x > 0:
                reverseList.append(str(x % 10))
                x = x / 10
        return int(''.join(reverseList)) < 2147483648 and int(''.join(reverseList)) or 0

s = Solution()
print(s.reverse(-134))
print(s.reverse(134))
