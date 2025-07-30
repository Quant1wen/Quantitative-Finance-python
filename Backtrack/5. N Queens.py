#The n-queens puzzle is the problem of placing n queens on an n x n chessboard
#such that no two queens attack each other.

#Given an integer n, return all distinct solutions to the n-queens puzzle.
#You may return the answer in any order.

#Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space, respectively.

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Create a digital board n*n
        board = [['.'] * n for _ in range(n)]
        res=[]
        # Three initialized boundary:if the position is occupied, set it to True.
        pos=[False]*n
        left = [False]*2*n
        right = [False]*2*n
        
        def dfs(row):
            # Boundary: if board is complete, adds it to the output  
            if row == n:
                res.append([''.join(row_str) for row_str in board])
                return
           
            for col in range(n):
                # 回溯：每一层都要对棋盘这一列中的所有点位进行试探，如果列，左右对角线有一个被占用(True)，就跳过
                if pos[col] or left[col+row] or right[col+n-row]:
                    continue
                # 这是一个可插入的新位置！暂时替换为Q，并且以此为节点进行分支的递归
                board[row][col] = 'Q'
                pos[col] = left[col + row] = right[col + n - row] = True
                # 进行下一个分支！这一个分支会一直延伸到最后的一个结果
                dfs(row+1)
              
                # 上面已经延伸了一个结果，这里是撤销回溯进行初始化，需要把第一步中所有的操作都进行还原
                board[row][col] = '.'
                pos[col] = left[col + row] = right[col + n - row] = False
              
        dfs(0)
        return res

sol=Solution()
n=4
print(sol.solveNQueens(4))
