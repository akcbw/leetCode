from Tree import ConstructBinaryTreeFromPreorderAndInorderTraversal

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
a = ConstructBinaryTreeFromPreorderAndInorderTraversal.Solution().buildTree(preorder, inorder)
b = ConstructBinaryTreeFromPreorderAndInorderTraversal.Solution().buildTree(preorder, inorder)


def isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

print(isSameTree(a, b))

