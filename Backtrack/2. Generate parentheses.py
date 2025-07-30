# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Example 1:
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res == []
        def dfs(left,right,comb):
            if len(comb) == 2*n:
                res.append(comb)

            #
            if left < n:
                dfs(left+1,right,comb+'(')
            if left > right:
                dfs(left,right+1,comb+')')
        dfs(0,0,'')


#      ((
# (    
#      ()
# Fist layer - second layer 在回溯的同时还需要考虑每一层的所有情况 即if语句中的操作是每一层深度搜索的操作，而if语句的并列代表了每一层所有情况的包含
