#encoding=utf-8
"""
# Author: Acer
# Created Time: 二  5/26 14:40:37 2015
# File Name: 147-InsertSortList.py
# Description:
# @param: ListNode head 
# @return: ListNode
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertSortList(self, head):
        if not head:
            return None
        dummyHead = ListNode(0)
        p = head
        
        while p:
            q = dummyHead.next
            preQ = dummyHead
            while q:
                if p.val > q.val:
                    preQ = q
                    q = q.next
                else:
                    afterP = p.next
                    p.next = q
                    preQ.next = p
                    p = afterP
                    break
            if q is None:
                afterP = p.next
                preQ.next = p
                p.next = None
                p = afterP

        return dummyHead.next

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(5)
n5 = ListNode(4)
n6 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

s = Solution()
sortedList = s.insertSortList(n1)
while sortedList:
    print(sortedList.val),
    sortedList = sortedList.next


