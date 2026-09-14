# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if subRoot == None:
            return True
        if root == None:
            return False
        if root.val == subRoot.val:
            return (self.isSameTree(root.right, subRoot.right) and self.isSameTree(root.left, subRoot.left)) or (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
