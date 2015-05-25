#encoding=utf-8
"""
# Author: Acer
# Created Time: 一  5/25 22:47:58 2015
# File Name: 206-ReverseLinkedList.py
# Description:
# @param: ListNode head
# @return: ListNode
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 时间复杂度o(n^2)
    def reverseList1(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        while p.next:
            preLast, last = self.findLastNode(p)
            preLast.next = None
            last.next = p.next
            p.next = last 
            p = p.next
        return dummyHead.next

    def findLastNode(self, node):
        preLast, last = node, node.next
        while last.next:
            preLast = preLast.next
            last = last.next
        return preLast, last 

    # 思路：设置三个指针 prev：前指针，curr：当前指针，afte：后指针
    # 旋转，遍历整个链表，将curr指向prev即可
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
            head = prev
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
reverseList = s.reverseList(node1)
while reverseList:
    print(reverseList.val)
    reverseList = reverseList.next

