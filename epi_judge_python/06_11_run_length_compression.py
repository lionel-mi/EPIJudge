from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    lst = []
    idx = 0
    counter = 0
    while idx < len(s):
        if s[idx].isdigit():
            counter = counter * 10 + int(s[idx])
        else:
            lst.append(s[idx] * counter)
            counter = 0

        idx += 1
    return "".join(lst)


def encoding(s: str) -> str:
    lst = []
    counter = 1
    for idx in range(1, len(s)):
        if s[idx-1] != s[idx]:
            lst.append(str(counter))
            lst.append(s[idx-1])
            counter = 0
        counter += 1
    lst.append(str(counter))
    lst.append(s[-1])
    return "".join(lst)




def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_11_run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
