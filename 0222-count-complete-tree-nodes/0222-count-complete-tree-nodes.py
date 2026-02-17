class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        if left_height == right_height:
            # left subtree is perfect
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # right subtree is perfect
            return (1 << right_height) + self.countNodes(root.left)
    
    def getHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
