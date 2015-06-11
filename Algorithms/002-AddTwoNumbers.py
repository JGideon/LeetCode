#encoding=utf-8
"""
# Author: Acer
# Created Time: 一  5/25 15:12:27 2015
# File Name: 002-AddTwoNumbers.py
# Description:
# @param: ListNode l1
# @param: ListNode l2
# @return: ListNode 
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        p, q = l1, l2
        dummyResult = ListNode(-1)
        result = dummyResult
        carry = 0

        while p or q or carry:
            res = (p.val if p else 0) + (q.val if q else 0) + carry
            result.next = ListNode(res % 10)
            result = result.next
            carry = int(res / 10)
            p = (p.next if p else None)
            q = (q.next if q else None)
        return dummyResult.next

s = Solution()
l1 = ListNode(5)
l2 = ListNode(5)
result = s.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
