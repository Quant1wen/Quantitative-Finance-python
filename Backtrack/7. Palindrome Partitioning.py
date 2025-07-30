#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

#Example 1:
#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        def isPalindrome(s,start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(idx,path = []):
            if idx == len(s): #参数的参考：需要一个boundary停止参数，这里是操作到的字符的顺序，如果操作到最后一个了就i停止
                res.append(path.copy())
            for i in range(idx,len(s)):
                if isPalindrome(s,idx,i):
                    #核心的回溯三部曲：从idx到i是回文后，递归的下一步从i+1开始，并且在之后要对path进行回溯撤销
                    path.append(s[idx:i+1]) #理解：参考word search中的对board[i][j]的暂时储存，第一部的作用是从后面逆推的
                                            #在上一个问题中，为了防止后面对前面进行重复检索；这一问题中，是为了防止回文重复
                    dfs(i+1,path)
                    path.pop()
        dfs(0)
        return res

sol = Solution()
print(sol.partition('ababb'))
