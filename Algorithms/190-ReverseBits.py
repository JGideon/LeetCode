#encoding=utf-8
#######################################################################
# Author: Acer                                                        #
# Created Time: 星期三  6/ 3 10:00:32 2015                            #
# File Name: 190-ReverseBits.py                                       #
# Description:                                                        #
#   无符号整型数字以二进制形式倒置，输出结果.                         #
# Solution:                                                           #
#   1.n从低位往高位取每一位的值，result每次加上改位的值并左移一位     #
#   2.保证n不丢位，当n < 2^31时，n取反                                # 
#######################################################################
class Solution:
    # @param: integer n 
    # @return: integer 
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) ^ (n & 1)
            n >>= 1
        assert n == 0 
        return result

    def reverseBits1(self, n):
        if n >= pow(2, 32):
            return None
        result = 0
        if n < pow(2, 31):
            n = ~n
            while n:
                result += n & 1
                n >>= 1
                result <<= 1
            return ~result
        else:
            while n:
                result += n & 1
                n >>= 1
                result <<= 1
            return result

s = Solution()
print(s.reverseBits(5))
