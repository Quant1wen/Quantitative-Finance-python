# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Example 1:
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def dfs(left,right,comb):

            # 边界条件：如果括号已经满足
            if left == n and right == n:
                res.append(comb)
                return

            # 与下一层递归的嵌套关系：从头开始，本来是(0,0)，如何同时伸展到(1,0)/(0,1)?需要先到(1,0)，
            #再到(0,1)：(0,0)满足left<=n到(1,0)，然后right<left，到(0,1)，每一层都通过折线的方式到下一层的两个分支
            if left <= n:
                dfs(left+1, right,comb+'(')
            if right < left:
                dfs(left, right+1,comb+')')
        dfs(0,0,'')
        return res
#      ((
# (    
#      ()
# Fist layer - second layer 在回溯的同时还需要考虑每一层的所有情况 
# 即if语句中的操作是每一层深度搜索的操作，而if语句的并列代表了每一层所有情况的包含

Sol=Solution()
n=3
print(Sol.generateParenthesis(n))
