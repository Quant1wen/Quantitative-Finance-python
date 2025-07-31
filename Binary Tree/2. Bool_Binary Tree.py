# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#    The left subtree of a node contains only nodes with keys strictly less than the node's key.
#    The right subtree of a node contains only nodes with keys strictly greater than the node's key.
#    Both the left and right subtrees must also be binary search trees.

          1
        /   \
       0     4
           /  \
          3    5
# 确定为中序遍历，左-根-右：判断为失败的情况有：如果左边节点内部失败，或者左边节点没有小于当前节点，则失败；左-中-右的搜索过程中，需要一个variable来时刻更新目前最大值并进行比较
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float ['-inf']
        def dfs(node):
            if not node: return True     # 如果后续没有节点，那么是满足条件的，因此返回True
            if not (dfs(node.left) and prev < node.val): return False  # 如果左边已经失败了，或者左边大于这个根节点：失败
            prev = node.val     #更新prev的值
            return dfs(node.right)  #返回右侧；node与node.left的判断方式是通过prev<node.val来进行的
        return dfs(root)

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
          1
        /   \
       2     2
      / \   /  \
     4   3  3   4
# 对称的问题，无论哪种遍历都无法很好的检验
# 可以将树进行拆分
class Solution:
    def isSym(self, p: Optional[TreeNode],q: Optional[TreeNode]) -> bool:

        # 如果p或q中有一个为空，需要检查两者是否相等，例如左右对称的两个左侧为空的子树是不镜像对称的
        if not p or not q: return p is q
        # 返回：如果两个根节点的值相等，并且下面的镜像子节点也相等，返回True
        return p.val == q.val and self.isSym(p.left, q.right) and self.isSym(p.right, q.left)
      
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSym(root.left, root.right)
    
      
