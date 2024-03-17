import math
from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicates(block):
        block = list(filter(lambda x: x > 0, block))
        return len(block) == len(set(block))

    N = len(partial_assignment)
    if any(has_duplicates(partial_assignment[i][j] for j in range(N))
           or has_duplicates(partial_assignment[j][i] for j in range(N))
           for i in range(N)):
        return False

    region_size = int(math.sqrt(N))
    return all(not has_duplicates([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))]
        for I in range(region_size) for J in range(region_size)))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_17_is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
