#encoding=utf-8
"""
# Author: Acer
# Created Time: 星期五  5/29 19:46:36 2015
# File Name: 144-BinTreePreorderTravesal.py
# Description:
# @param: TreeNode root
# @return: Integer[]  
"""
class Solution:
    def preorderTraversal(self, root):
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop(0)
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        return result

    def preorderTraversal1(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal1(root.left) + self.preorderTraversal1(root.right)
