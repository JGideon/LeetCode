class Solution:
    # @param string str
    # @return integer
    def myAtoi(self, string):
        isPositive = True
        intValueList = []
        intValue = 0
        if string[0] is '-':
            isPositive = False
            for i in range(1, len(string)):
                intValueList.append(string[i] - '0')
        else:
            isPositive = True
            for i in range(len(string)):
                intValueList.append(string[i] - '0')
        
