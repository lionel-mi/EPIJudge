from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    sol = [[1]]
    for row in range(1, n):
        next_row = [1]
        for idx in range(row-1):
            next_row.append(sol[row-1][idx] + sol[row-1][idx+1])
        next_row.append(1)
        sol.append(next_row)
    return sol





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_20_pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
