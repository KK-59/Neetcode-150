# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        def fun(root, cur, target):
            cur += root.val
            if cur == target and root.right == None and root.left == None:
                return True
            if root.left != None and root.right != None:
                return fun(root.left, cur, target) or fun(root.right, cur, target)
            elif root.left != None: 
                return fun(root.left, cur, target)
            elif root.right != None: 
                return fun(root.right, cur, target)
            else:
                return False
        return fun(root, 0, targetSum)