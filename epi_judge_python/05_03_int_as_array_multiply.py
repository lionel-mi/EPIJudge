from typing import List

from test_framework import generic_test
# [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if num1[0] * num2[0] < 0 else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    solution = [0] * (len(num1) + len(num2))
    for n1 in range(len(num1)-1, -1, -1):
        for n2 in range(len(num2)-1, -1, -1):
            solution[n1 + n2 + 1] += (num1[n1] * num2[n2])
            solution[n1 + n2] += solution[n1 + n2 + 1] // 10
            solution[n1 + n2 + 1] %= 10
    for i in range(0, len(solution)):
        if solution[i] != 0:
            solution[i] *= sign
            return solution[i:]

    return [solution[-1] * sign]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_03_int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
