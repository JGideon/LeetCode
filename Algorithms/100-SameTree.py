#encoding=utf-8
"""
# Author: Acer
# Created Time: 五  5/29 09:49:14 2015
# File Name: 100-SameTree.py
# Description:
# @param: TreeNode p
# @param: TreeNode q 
# @return: boolean 
"""
class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

