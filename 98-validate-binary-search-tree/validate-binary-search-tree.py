# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recBST(self, node,arr):
        if not node:
            return
        self.recBST(node.left,arr)
        arr.append(node.val)
        self.recBST(node.right,arr)
        return

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr =[]

        self.recBST(root,arr)

        valid = True

        if len(arr) >=2:
        
            for i in range(1,len(arr)):
                if arr[i]<= arr[i-1]:
                    return False
        return True

