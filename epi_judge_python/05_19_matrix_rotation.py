from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    for i in range(len(square_matrix)//2):
        for j in range(i, len(square_matrix) - i - 1):
            square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i] = square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i], square_matrix[i][j]




    # tmp = square_matrix[i][j]
    # square_matrix[i][j] = square_matrix[~j][i]
    # square_matrix[~j][i] = square_matrix[~i][~j]
    # square_matrix[~j][i] = square_matrix[~i][~j]
    # square_matrix[~i][~j] = square_matrix[~j][~i]
    # square_matrix[~j][i] = tmp



def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_19_matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
