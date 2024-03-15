from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    for idx_to_swap in range(len(perm)-2, -1, -1):
        if perm[idx_to_swap] < perm[idx_to_swap+1]:
            for idx_next in range(len(perm)-1, idx_to_swap, -1):
                if perm[idx_next] > perm[idx_to_swap]:
                    perm[idx_next], perm[idx_to_swap] = perm[idx_to_swap], perm[idx_next]
                    perm[idx_to_swap+1:] = reversed(perm[idx_to_swap+1:])
                    return perm

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_11_next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
