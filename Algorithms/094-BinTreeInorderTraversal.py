#encoding=utf-8
"""
# Author: Acer
# Created Time: 星期五  5/29 20:06:47 2015
# File Name: 94-BinTreeInorderTraversal.py
# Description:
# @param: 
# @return: 
"""
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
