# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        #given null tree/ base case if it is at leaf node
        if not root:
            return TreeNode(val)

        #use recursion to check if value is greater than/less than
        #than make the root.x equal to that where it belongs so
        #the call stack can point properly
        if val > root.val: 
            root.right = self.insertIntoBST(root.right, val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root