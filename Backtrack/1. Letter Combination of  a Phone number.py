# the basic knowledge about backtrack and recursion

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

      # if no input
      if not digits:
        return []

      # using a dictionary to perform the phone number
      phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

      def backtrack(combination,next_digits):

        # Boundary condition: if the length is enough, adds it to output
                  if len(next_digits) == 0:
                      output.append(combination)
                    
        # The first layer: first digits (e.g. 2)
        # Then adds each letter in digits[1] to digits[0] continue until the boundary(len(next_digits)==0)
                  else:
                      for letter in phone_map[next_digits[0]]:
                          backtrack(combination + letter, next_digits[1:])
              output = []
              backtrack("",digits)
              return output

      #d - boundary
#a    #e - boundary
      #f - boundary

      #d - boundary
#b    #e - boundary 
      #f - boundary

      #d - boundary
# c   #e - boundary
      #f - boundary

map = ['','','abc','def','ghi','jkl']
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n = len(digits)

        # 提前存储好path的路径
        path = [''] * n
        res = []
        
        if not digits: return []
            
        def dfs(i):

            # path是可变对象，每次dfs只是原地修改path[i]，而列表本身地址不变。
            if i == n:
                res.append(''.join(path))
                return

            # 对digit[i]中的字母进行循环，
            for j in map[int(digits[i])]:

                # path的第i的元素设定为digit[i]中的j 第一层循环
                path[i] = j

                #嵌套第二层，进行下一层循环，两层之间连接
                dfs(i+1)
        dfs(0)
        return res
            
