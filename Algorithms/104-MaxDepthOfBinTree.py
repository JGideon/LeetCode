#encoding=utf-8
"""
# Author: Acer
# Created Time: 五  5/29 11:00:01 2015
# File Name: 104-MaxDepthOfBinTree.py
# Description:
# @param: TreeNode root
# @return: Integer 
"""
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
