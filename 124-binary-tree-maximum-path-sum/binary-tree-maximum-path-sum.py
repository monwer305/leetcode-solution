# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rexMaxPathSum(self,root):
        if not root:
            return 0,-1001

        left,maxL = self.rexMaxPathSum(root.left)
        right,maxR = self.rexMaxPathSum(root.right)

        curMax= max(left+root.val,right+root.val,root.val)
        maxN = max (maxL,maxR,curMax,left+right+root.val)

        return curMax,maxN
    


    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        _,maxN = self.rexMaxPathSum(root)

        return maxN

        