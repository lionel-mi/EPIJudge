from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    sol = []
    if len(square_matrix) == 0:
        return sol
    left, right, top, bottom = 0, len(square_matrix[0]), 0, len(square_matrix)
    while left < right and top < bottom:
        #left to right
        for i in range(left, right):
            sol.append(square_matrix[top][i])
        top += 1
        #top to bottom
        for i in range(top, bottom):
            sol.append(square_matrix[i][right-1])
        right -= 1
        if left == right or top == bottom:
            break
        #right to left
        for i in range(right-1, left-1, -1):
            sol.append(square_matrix[bottom-1][i])
        bottom -= 1
        #bottom to top
        for i in range(bottom-1, top-1, -1):
            sol.append(square_matrix[i][left])
        left += 1
    return sol


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_18_spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
