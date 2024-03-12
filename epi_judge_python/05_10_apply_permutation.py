from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    is_permutated = [False] * len(A)
    for next_head in range(len(A)):
        if is_permutated[next_head]:
            continue
        prev_idx = None
        next_idx = perm[next_head]
        tmp = A[next_idx]
        while prev_idx != next_head:
            if prev_idx is None:
                prev_idx = next_head
            A[next_idx] = A[prev_idx]
            prev_idx = next_idx
            next_idx = perm[next_idx]




def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_10_apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
