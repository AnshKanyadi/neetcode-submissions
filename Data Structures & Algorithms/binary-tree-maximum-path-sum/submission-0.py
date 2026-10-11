# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        maxsum = float('-inf')



        def dfs(node):
            nonlocal maxsum

            if node == None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0



            maxsum = max(maxsum, left + right + node.val)
        


            return node.val + max(left, right)


        dfs(root)

        return maxsum

            
        

   
        

        