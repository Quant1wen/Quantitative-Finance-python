# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

#Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#Output: [3,9,20,null,null,15,7]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque (preorder)
        # 原理： preorder中的每个节点放到右边都可以将inorder分成左右两部分
        def build (preorder,inorder):
            if inorder: # 如果inorder不为空
                idx = inorder.index(preorder.popleft())  #较为复杂的操作：使用.popleft提取出了preorder中的第一个元素(root)，并锁定在inorder中的index
                root = TreeNode(inorder[idx])    #以此点为根节点
                root.left = build(preorder,inorder[:idx])  #因为preorder是从左到右的，因此先建立左边的树
                root.right = build(preorder,inorder[idx+1:])
                return root
        return build(preorder, inorder)


#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#Input: nums = [-10,-3,0,5,9]
#Output: [0,-3,9,-10,null,5]

#发现规律：input的中间数要作为节点分开左右

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def spLit(left,right):
            if left > right: return #边界条件：直接返回
            mid = (left + right)/2  #选取中间节点
            root = TreeNode(nums[mid]) #以中间节点作为根节点
            root.left = spLit(left,mid-1) #左侧进行递归
            root.right = spLit(mid+1,right) #右侧进行递归
            return root
        return spLit(0,len(num)-1)
