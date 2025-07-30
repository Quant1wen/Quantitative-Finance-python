#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#Example 1:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

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
