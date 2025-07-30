#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# 回溯总体步骤： 确定边界条件；确定搜索路径
# 回溯三部曲：对当前步骤做出选择；进行递归（联系下一步）；回溯取消
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        n=len(nums)
        def dfs(comb,newnums):
            if len(comb) == len(nums):
                res.append(comb.copy())
            for i in range(len(newnums)):
                comb.append(newnums[i])
                dfs(comb,newnums[:i]+newnums[i+1:])
                comb.pop()
        dfs([],nums)
        return res

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def permutation(num, perm):
            if not num:
                res.append(perm)   # 保存当前排列
                return
            for i in range(len(num)):
                # 取出当前数字
                curr = num[i]
                # 把剩余列表传给下一层
                permutation(num[:i] + num[i+1:], perm + [curr])

        permutation(nums, [])
        return res

sop = Solution()
nums=[1,2,3]
print(sop.permute(nums))
