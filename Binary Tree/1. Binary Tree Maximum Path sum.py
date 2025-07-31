# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
#A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

#Input: root = [1,2,3]
#Output: 6
#Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

         -10
        /   \
       9    20
           /  \
          15   7
#核心思路：return是与上层调用者之间的联系，在单次调用内部写清楚内部最大值的操作

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]    #先储存根节点的值作为最初的result
        def search(node):
            if not node:    #如果后面都是null节点，返回0
                return 0
            l_node = max(search(node.left),0)  #l_node是node.left这一分节点进行递归的值，如果小于0的话直接返回0
            r_node = max(search(node.right),0) 
            res[0] = max(res[0],node.val + l_node + r_node) #对结果的最大值进行更新
          
            return node.val + max(l_node,r_node) #返回的到底是什么？返回的是上层引用到这个search时候的内容！
                                                 #例如node.left被node引用时，search(node.left)只能包含后续的一条分路线
        search(root)
        return res[0]
      
