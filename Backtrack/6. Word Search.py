# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

class Solution:
    def exist(self, board, word):
      
        m = len(board)       #记录面板大小
        n = len(board[0])
      
        def dfs(row,column,idx):
            if idx == len(word): # 如果已经搜索到了长度足够的结果，返回结果为True
                return True
            if row < 0 or row >= m or column < 0 or column >= n or board[row][column] != word[idx]: 
                return False  # 如果搜索的点超出边界或者搜索的点不符合条件
              
            temp = board[row][column]  # 为了防止回流搜索，在回溯的步骤中暂时将本次的点储存在temp中
            board[row][column] = ''    # 可以看出，回溯时的选择需要兼顾两点：1、对于当前状态的改变；2、如果在后续回溯中需要对前面的进行排除，在此处进行
           
            if dfs(row+1,column,idx+1) or dfs(row,column+1,idx+1) or dfs(row,column-1,idx+1) or dfs(row-1,column,idx+1):
                 return True #特殊的递归：重点是返回的布尔值，如果四个中有一个是True，就返回True
              
            board[row][column] = temp # 回溯取消时，需要同时对回溯选择和递归两个过程进行撤销
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True # 只要有一个期间通过检测，就可以返回True
        return False

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = 'ABCCEF'
print(sol.exist(board, word))
