# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.right != None and root.left != None:
            return max(self.diameterOfBinaryTree(root.left), self.maxDepth(root.right) + self.maxDepth(root.left), self.diameterOfBinaryTree(root.right) )
        if root.left != None: 
            return max(self.diameterOfBinaryTree(root.left), self.maxDepth(root.left))
        if root.right != None: 
            return max(self.diameterOfBinaryTree(root.right), self.maxDepth(root.right))
        else:
            return 0
