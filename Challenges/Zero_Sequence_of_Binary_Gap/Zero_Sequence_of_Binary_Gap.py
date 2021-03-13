"""
A `binary gap` within a `positive integer N` is `any maximal sequence` of `consecutive zeros` that is `surrounded by ones` at `both ends` in the `binary representation` of N.

For example, `number 9` has `binary` representation `1001` and `contains` a `binary gap` of length `2`. The `number 529` has `binary` representation `1000010001` and `contains` two `binary` gaps: one of `length 4` and one of `length 3`. 

The `number 20` has `binary` representation `10100` and `contains` one `binary gap` of length 1. The `number 15` has `binary` representation `1111` and has `no binary gaps`. The `number 32` has `binary` representation `100000` and has `no binary gaps`.

Write a function:

    def solution(N)

that, given `a positive integer N`, `returns the length` of its `longest binary gap`. The function should `return 0` if N `doesn't contain a binary gap`.

For example, given `N = 1041` the `function` should `return 5`, because N has `binary` representation `10000010001` and so its `longest binary gap is of length 5`. Given `N = 32` the `function` should `return 0`, because `N` has `binary` representation `'100000'` and `thus no binary gaps`.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].


** TASK :**

Find longest sequence of zeros in binary representation of an integer.

"""

def solution(N):
  binary = f'{N:b}' # this is string data type
  print(binary)
  zero_sequence_len = []
  
  if binary.count('0') != 0:
    # looping through index of binary (string)
    for index in range(0, len(binary)):
      # if binary is 1, then
      if binary[index] == '1':
        # if not found the same value, will return -1
        # if found the same value, will return the index of the value that we search 
        next_val_index = binary.find('1', index + 1)
        if next_val_index != -1: # if next '1' is found, then
          zero_sequence_len.append(next_val_index - 1 - index) # length of zero sequence between 1 and 1
      # if binary is 0, then
      else:
        zero_sequence_len.append(0)

    # return the highes sequence
    return max(zero_sequence_len)

  else:
    return 0

print(solution(32))

print(solution(15))

print(solution(529))

print(solution(1041))