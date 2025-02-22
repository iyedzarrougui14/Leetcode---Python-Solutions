class Solution(object):
    def rootToLeafPathSum(self, root, targetSum, currentSum):
        # Base case: if the root is None, return False
        if root is None:
            return False
        
        # Update the current sum with the current node's value
        currentSum += root.val
        
        # Check if it's a leaf node
        if root.left is None and root.right is None:
            # If the current sum matches the target sum, return True
            if currentSum == targetSum:
                return True
        
        # Recursively check the left and right subtrees
        return self.rootToLeafPathSum(root.left, targetSum, currentSum) or self.rootToLeafPathSum(root.right, targetSum, currentSum)
    
    def hasPathSum(self, root, targetSum):
        # Initialize the current sum to 0
        currentSum = 0
        # Call the helper function
        return self.rootToLeafPathSum(root, targetSum, currentSum)