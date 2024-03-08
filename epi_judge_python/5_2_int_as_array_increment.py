from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    for idx in range(len(A)-1, -1, -1):
        if A[idx] < 9:
            A[idx] += 1
            return A
        A[idx] = 0
    return [1] + [0] * len(A)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5_2_int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
