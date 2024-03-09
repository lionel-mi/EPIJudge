from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    reachable = 0
    discovered = -1
    target = len(A) - 1
    while discovered < reachable:
        discovered += 1
        reachable = max(reachable, discovered + A[discovered])
        if reachable >= target:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_04_advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
