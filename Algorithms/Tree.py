
"""
# Author: Acer
# Created Time: 五  5/29 13:07:31 2015
# File Name: Tree.py
# Description:
# @param:
# @return:
"""
class Solution:
    def buildTree(self, numbers):
        if not numbers:
            return None
        i = 0
        while len(numbers):
            result = numbers.pop(0)
            if result == '#':
                return None
            root = TreeNode(result)


class TreeNode(object):

    """
    # Binary Tree Structure;
    """

    def __init__(self, left=None, right=None, x):
        """TODO: to be defined1.

        :left: TODO
        :right: TODO
        :x: TODO

        """
        self._left  = left
        self._right = right
        self._x     = x

