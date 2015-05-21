class Solution:
    '''
    '''
    def isBalanced(self, root):
        if root is None:
            return True
        leftHeight = self.deepth(root.left)
        rightHeigt = self.deepth(root.right)



    def deepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.deepth(root.left), self.deepth(root.right)) + 1

