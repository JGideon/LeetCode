#encoding=utf-8
"""
# Author: Acer
# Created Time: 星期五  5/29 21:26:01 2015
# File Name: 173-BinSearchTreeIterator.py
# Description:
# @param: 
# @return: 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.root = root

    def hasNext(self):
