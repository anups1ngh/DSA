# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def distanceHelper(root,target,k,out):
    if root is None:
        return -1
    if root == target:
        helper(root,k,out)
        return 0
    ld = distanceHelper(root.left,target,k,out)
    if ld == -1:
        rd = distanceHelper(root.right,target,k,out)
        if rd == -1:
            return -1
        elif rd+1 == k:
            out.append(root.val)
            return k
        else:
            helper(root.left,k-rd-2,out)
            return rd+1
    elif ld+1 == k:
        out.append(root.val)
        return k
    else:
        helper(root.right,k-ld-2,out)
        return ld+1
        
        
def helper(root,k,out):
    if root is None:
        return
    if k==0 and root is not None:
        out.append(root.val)
        return
    helper(root.left,k-1,out)
    helper(root.right,k-1,out)
    
class Solution:
    def distanceK(self, root, target, k):
        output = []
        distanceHelper(root,target,k,output)
        return output