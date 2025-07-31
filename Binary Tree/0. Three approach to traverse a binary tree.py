#      -2
#     /   \
#    3     4

# preorder: -2 - 3 - 4
# root - left - right
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# inorder: 3 - -2 - 4
# left - root - right
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# postorder: 3 - 4 - -2
# left - right - root
def postorder(root):
    if not root:
        return []
    return postorder(left) + postorder(right) + [root.val]
