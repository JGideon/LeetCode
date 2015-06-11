#encoding=utf-8
"""
# Author: Acer
# Created Time: 五  5/29 11:39:49 2015
# File Name: 111-MinDepthOfBinTree.py
# Description:
# @param: TreeNode root
# @return: Integer 
"""
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        result = min(self.minDepth(root.left), self.minDepth(root.right)) 
        if result == 0:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return result + 1
