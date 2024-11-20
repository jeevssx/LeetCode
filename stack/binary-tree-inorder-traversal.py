# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        def inorderTraversalHelp(rooty):
                if not rooty:
                    return
                
                inorderTraversalHelp(rooty.left)
                arr.append(rooty.val)
                inorderTraversalHelp(rooty.right)

        inorderTraversalHelp(root)
        return arr
        