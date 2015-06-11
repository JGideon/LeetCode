#encoding=utf-8
"""
# Author: Acer
# Created Time: 星期二  6/ 2 23:20:05 2015
# File Name: 061-RotateList.py
# Description:
# @param: 
# @return: 
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def rotateList(self, head, k):
        if not head or k == 0:
            return head
        # 1.计算链表长度
        # 2.找到队尾指针
        p = head
        lenOfList = 0
        while p.next:
            lenOfList += 1
            p = p.next
        tail = p
        lenOfList += 1
        k %= lenOfList 
        
        if k == 0: 
            return head
        # 寻找新的首尾节点 
        newTail = head 
        for i in range(lenOfList - k - 1):
            newTail = newTail.next
        newHead = newTail.next
        # 旋转的节点指向空，队尾节点指向newHead
        tail.next = head
        newTail.next = None
        head = newHead
        return head 

n = ListNode(1)
n2 = ListNode(2)
n.next = n2
s = Solution()
print(s.rotateList(n, 1).val)
