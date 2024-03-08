import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    def handle_left(pivot):
        s_index, ns_index = 0, len(A) - 1
        while s_index < ns_index:
            if A[s_index] < pivot:
                s_index += 1
            elif A[ns_index] >= pivot:
                ns_index -= 1
            else:
                A[s_index], A[ns_index] = A[ns_index], A[s_index]
                s_index += 1
                ns_index -= 1

    def handle_right(pivot):
        nb_index, b_index = 0, len(A) - 1
        while nb_index < b_index:
            if A[nb_index] <= pivot:
                nb_index += 1
            elif A[b_index] > pivot:
                b_index -= 1
            else:
                A[nb_index], A[b_index] = A[b_index], A[nb_index]
                nb_index += 1
                b_index -= 1

    pivot = A[pivot_index]
    handle_left(pivot)
    handle_right(pivot)





@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('5_1_dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
