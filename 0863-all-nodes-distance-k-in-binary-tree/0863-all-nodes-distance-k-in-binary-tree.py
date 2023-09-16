# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findTarget(root, target, path):
            if root is None:
                return False
            if root == target:
                path.append(root)
                return True
            if findTarget(root.left, target, path) or findTarget(root.right, target, path):
                path.append(root)
                return True
            return False
        
        def printkDistanceNodeDown(root, k, result):
            if root is None or k < 0:
                return
            if k == 0:
                result.append(root.val)
                return
            printkDistanceNodeDown(root.left, k - 1, result)
            printkDistanceNodeDown(root.right, k - 1, result)

        def distanceKHelper(root, target, k, result):
            path = []
            findTarget(root, target, path)
            
            for i, node in enumerate(path):
                if i == 0:
                    printkDistanceNodeDown(node, k, result)
                else:
                    # Calculate distance to target node
                    distance_to_target = k - i
                    if distance_to_target < 0:
                        break
                    if distance_to_target == 0:
                        result.append(node.val)
                    elif node.left == path[i - 1]:
                        printkDistanceNodeDown(node.right, distance_to_target - 1, result)
                    else:
                        printkDistanceNodeDown(node.left, distance_to_target - 1, result)
        
        result = []
        distanceKHelper(root, target, k, result)
        return result
