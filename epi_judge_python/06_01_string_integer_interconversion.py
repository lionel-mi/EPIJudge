from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    str_lst = []
    possitive = x >= 0
    x = abs(x)
    if x == 0:
        return "0"
    while x > 0:
        d = x % 10
        x = x // 10
        str_lst.append(chr(ord('0') + d))
    if not possitive:
        str_lst.append("-")
    else:
        str_lst.append("+")
    return "".join(list(reversed(str_lst)))


def string_to_int(s: str) -> int:
    str_lst = list(s)
    num = 0
    if str_lst[0] == "-":
        possitive = False
        str_lst = str_lst[1:]
    elif str_lst[0] == "+":
        possitive = True
        str_lst = str_lst[1:]
    else:
        possitive = True
    for ch in str_lst:
        d = ord(ch) - ord('0')
        num = num * 10 + d
    if not possitive:
        num = -num
    return num



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_01_string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
