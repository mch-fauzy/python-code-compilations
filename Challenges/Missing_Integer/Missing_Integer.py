"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    unique_el = set(sorted(A)) #sorted the list and take unique value only
    print(unique_el)
    default = 1 #default smallest positive integer
    for val in unique_el:
        if val == default:
            default += 1
    return default

print(solution([1, 3, 6, 4, 1, 2]))

print(solution([1, 2, 3]))

print(solution([-1, -5, -3]))