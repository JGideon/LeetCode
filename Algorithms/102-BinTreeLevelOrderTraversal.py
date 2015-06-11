#encoding=utf-8
"""
# Author: Acer
# Created Time: 三  5/27 16:35:56 2015
# File Name: 102-BinaryTreeLevelOrderTraversal.py
# Description:
# @param: TreeNode root 
# @return: integer[][] 
"""
class Solution:
    def leverlOrder(self, root):
        levels = [[root]]
        result = []
        while levels:
            currLevel = levels.pop()
            nextLevel, currVal = [], []
            # 注意处理空值
            for node in currLevel:
                if node:
                    nextLevel += [node.left, node.right]
                    currVal.append(node.val)
            if currVal:
                result.append(currVal)
            if nextLevel:
                levels.append(nextLevel)
        
        return result
