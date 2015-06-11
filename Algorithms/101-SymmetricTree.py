#encoding=utf-8
"""
# Author: Acer
# Created Time: 三  5/27 10:17:50 2015
# File Name: 101-SymmetricTree.py
# Description:
# @param TreeNode root: 
# @return boolean: 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.checkNodes(root.left, root.right)

    def checkNodes(self, a, b):
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        return self.checkNodes(a.left, b.right) and checkNodes(a.right, b.left)

    def serializeTree(self, nums, index):
        if index >= len(nums):
            return None
        val = nums[index]
        index += 1
        if val == '#':
            return None
        root = TreeNode(val)
        root.left = self.serializeTree(nums, index)
        root.right = self.serializeTree(nums, index)
        return root

s = Solution()
nums = [1, 2, 3, '#', 5, 6, 7]
root = s.serializeTree(nums, 0)
print(root.val)
print(root.left.val)
print(root.right.val)

