"""
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.

    The sum of elements of the 0-th(upper) row is given as upper.
    The sum of elements of the 1-st(lower) row is given as lower.
    The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.

Your task is to reconstruct the matrix with upper, lower and colsum.

    Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

    If no valid solution exists, return an empty 2-D array.

 

Example 1:

    Input: upper = 2, lower = 1, colsum = [1,1,1]
    Output: [[1,1,0],[0,0,1]]
    Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
  Example 2:

    Input: upper = 2, lower = 3, colsum = [2,2,1,1]
    Output: []
Example 3:

    Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
    Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 

Constraints:

    1 <= colsum.length <= 10^5
    0 <= upper, lower <= colsum.length
    0 <= colsum[i] <= 2
"""

def reconstructMatrix(upper,lower,colsum):
  # add list with value of 0 -> [0,0,0,....]
  upper_list = [0 for _ in range(len(colsum))] 
  lower_list = [0 for _ in range(len(colsum))]

  # loop index and value from colsum
  for index, value in enumerate(colsum):
    #print(index)
    if value == 1:
      # If upper > lower, then change upper_list
      if upper > lower:
        upper_list[index] = 1
        # Decrease the upper value
        upper -= 1
      # If not, then change lower_list
      else:
        lower_list[index] = 1
        # Decrease the lower value
        lower -= 1

    elif value == 2:
      upper_list[index] = lower_list[index] = 1
      upper, lower = upper - 1, lower - 1

  if upper == 0 and lower == 0:
    return [upper_list, lower_list]
  else:
    return []

print(reconstructMatrix(2, 1, [1,1,1]))

print(reconstructMatrix(2, 3, [2,2,1,1]))

print(reconstructMatrix(5, 5, [2,1,2,0,1,0,1,2,0,1]))