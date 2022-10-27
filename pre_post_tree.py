# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        def recur(preorder, postorder):    
            if len(preorder) == 1:
                return TreeNode(postorder.pop())
        
            cur_node = TreeNode(postorder.pop())
            # return preorder's index of the value at postorder[-1]
            index = preorder.index(postorder[-1]) 
        
            cur_node.right = recur(preorder[index:], postorder)
            cur_node.left = recur(preorder[1:index], postorder)

            return cur_node

        return recur(preorder, postorder)
