#Given an array of distinct integers candidates and a target integer target, 
#return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#The same number may be chosen from candidates an unlimited number of times. 
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#Example 1:
#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]

# Classical Wrong Answer:
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(comb,total=0):
            if total > target:
                return
            if total == target:
                res.append(comb)
            for i in range(len(candidates)):
                comb.append(candidates[i])
                dfs(comb,total+candidates[i])
            return res
        return dfs([],0)
# 在同一层循环里每次都从 0 开始枚举，导致：顺序被打乱，出现 [2,3,2] 与 [2,2,3] 这种“不同顺序的重复组合”
# 每次向下递归时，只能从当前的位置往后开始，例如2，3之后不能选择2，加入start指针

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(idx,comb,total=0):
            if total > target:
                return
            if total == target:
                res.append(comb.copy())
                #或者使用浅拷贝： comb[:] comb中的元素本为可变对象
                return
            for i in range(idx,len(candidates)):
                comb.append(candidates[i]) #选择
                dfs(i,comb,total+candidates[i]) #递归
                comb.pop()  #撤销选择
        dfs(0,[],0)
        return res
    

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
