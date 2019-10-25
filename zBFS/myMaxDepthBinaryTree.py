from Tree import ConstructBinaryTreeFromPreorderAndInorderTraversal

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
a = ConstructBinaryTreeFromPreorderAndInorderTraversal.Solution().buildTree(preorder, inorder)

def maxDepth(root):
    if not root:
        return 0
    else:
        maxLeftDepth = maxDepth(root.left)
        maxRightDepth = maxDepth(root.right)
        return max(maxLeftDepth, maxRightDepth) + 1

print(maxDepth(a))

