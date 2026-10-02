# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: TreeNode, cur: int) -> (int,int): 
            if root == None:
                return (0,0)
            if root.val >= cur:
                cur = root.val
                return ((1 + helper(root.left, cur)[0] + helper(root.right, cur)[0]), cur)
            else:
                return (helper(root.left, cur)[0] + helper(root.right, cur)[0], cur)
        x = helper(root, root.val)
        return x[0] 