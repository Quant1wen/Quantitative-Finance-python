# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

         -10
        /   \
       9    20
           /  \
          15   7
      
# 分析问题：需要按照行进行分装，进行中-左右 的递归
      
         
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        res = [] # 结果矩阵初始化

        queue = [root] # 取出根节点
        while queue:
            level = [] #用于存放每一层单独的答案 最后进行res.append(level) 对应前面的初始化
            n = len(queue) # 针对这一层的queue中的每一个都要进行操作：怎么建立这一层与下一层的顺序？依次取出每一个节点，将其left/right放入下一个queue中
                           # 改进： 直接放到queue后，通过n已经选定了操作的节点个数
            for _ in range(n):
                node = queue.pop(0) # 取出第一个节点
                level.append(node.val)  # 在level中添加
                if node.left:       # 判断这个节点的left和right是否还有节点：有的话加入queue中
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level.copy()) # 这一层结束 加入result中
         return res

from collections import deque
# 时间复杂度为 O(n^2) 使用deque以及popleft()降低时间复杂度为O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        res = [] # 结果矩阵初始化

        q = deque([root]) #可以使用.popleft()直接提取出左侧第一个元素！

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(left)
                if node.right:
                    q.append(right)
            res.append(level)
        return res



