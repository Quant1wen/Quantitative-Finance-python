# the basic knowledge about backtrack and recursion

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

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
      
