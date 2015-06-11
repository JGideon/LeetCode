class Solution:
    '''
    '''
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.deepth(root.left) - self.deepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def deepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.deepth(root.left), self.deepth(root.right)) + 1

