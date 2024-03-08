from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_18_spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
