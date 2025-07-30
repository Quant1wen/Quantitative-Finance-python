#Given an array of distinct integers candidates and a target integer target, 
#return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#The same number may be chosen from candidates an unlimited number of times. 
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#Example 1:
#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        #idx: 用于索引candidates中的元素
        #comb: 储存暂时的数组
        #total: temporary counting machine.

        def calc(idx,comb,total):

            # boundary 1: if target is gettable, adds to the results and return
            if total == target:
                res.append(comb[:])
                return

            # boundary 2: if target is transcended, give up and return
            if total > target or idx >= len(candidates):
                return

            # 检测candidates[idx]：先在结果后加入candidates[idx]，并运行函数；之后回溯
            comb.append(candidates[idx])
            calc(idx,comb,total+candidates[idx])
            comb.pop()

            #
            calc(idx+1,comb,total)
            return res

        return calc(0,[],0)

sol=Solution()
candidates = [2,3,5,7]
target = 7
print(sol.combinationSum(candidates,target))
