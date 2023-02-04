# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = nums[len(nums) // 2]
        rootNode = TreeNode()
        rootNode.val = mid
        rootNode.left = self.sortedArrayToBST(nums[0:mid])
        rootNode.right = self.sortedArrayToBST(nums[mid+1:])
        return rootNode

