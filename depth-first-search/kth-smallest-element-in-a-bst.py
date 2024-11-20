# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = [0, -1]

        self.inorder(root, k, result)

        return result[1]

    def inorder(self, root, k, result):

        if root is None or result[0] >= k:
            
            return

        self.inorder(root.left, k, result)

        result[0] += 1

        if result[0] == k:

            result[1] = root.val

            return

        self.inorder(root.right, k, result)
        