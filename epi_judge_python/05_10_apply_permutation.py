from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    is_permutated = [False] * len(A)
    for next_head in range(len(A)):
        if is_permutated[next_head]:
            continue
        is_permutated[next_head] = True
        prev_idx = None
        next_idx = perm[next_head]
        tmp = A[next_head]
        while prev_idx != next_head:
            A[next_idx], tmp = tmp, A[next_idx]
            is_permutated[next_idx] = True
            prev_idx = next_idx
            next_idx = perm[next_idx]




def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A



apply_permutation([2, 0, 1, 3], ['a', 'b', 'c', 'd'])
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_10_apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
