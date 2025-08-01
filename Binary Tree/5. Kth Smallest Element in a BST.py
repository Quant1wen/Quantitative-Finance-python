# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

    3
   / \
  1   4
   \
    2

# 发现从小到大的规律： 是左中右形式
# 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = [] 
        # 创建一个栈，用于存储中间节点
        current = root # 检索节点，向下排除
        while current or stack: # 如果中间节点和未检索节点中有非空
          
              # 当current空的时候，stack刚好是current上面的节点，这个节点只有右分支，右分支一定更大，这意味着这可以从最小序列开始加
            while current:
              current = current.left
              stack.append(current)  # 先把中间节点的左-中提取出来
            current = stack.pop()  # 选取最后一个节点 左边为空：这是最小的！那么他的右边是第二小的
            n += 1
            if n == k: return current.val
            current = current.right #选取第二小的
            # 一直到最右侧的无后续节点的情啊坤哥 这时候返回前面的节点重新进行检索 从stack中


#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

#According to the definition of LCA on Wikipedia: 
#“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
#  (where we allow a node to be a descendant of itself).”

class Solution:
    def lowestCommonAncestor(self,
                             root: 'TreeNode',
                             p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q: return root
          #如果没节点了就返回空 如果是p/q直接返回 因为意味着另外一个点要么在这个下面 要么在另外一个分支 而在上面是没找到的
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root # 如果左右都找到了各一个 返回root
        return left if left else right # 如果只有左/右找到 说明在一边 返回即可
