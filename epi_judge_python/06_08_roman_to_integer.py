from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    sol = 0
    T = {'I': 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M":1000}
    for idx in range(len(s)):
        val = T[s[idx]]
        if idx != len(s) -1 and T[s[idx+1]] > T[s[idx]]:
            val = -val
        sol += val
    return sol


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_08_roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
