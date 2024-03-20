import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# replase a with dd
# delete all b

# [a, a, ]

def replace_and_remove(size: int, s: List[str]) -> int:
    def get_final_size():
        counter = 0
        for ch in s:
            if ch == "a":
                counter += 1
            elif ch == "b":
                counter -= 1
            elif ch == "":
                break
            counter += 1
        return counter

    final_size = get_final_size()
    read_idx = size - 1
    write_idx = len(s) - 1
    while read_idx >= 0:
        ch = s[read_idx]
        if ch == "a":
            s[write_idx] = "d"
            s[write_idx-1] = "d"
            write_idx -= 2
        elif ch != "b":
            s[write_idx] = ch
            write_idx -= 1
        read_idx -= 1
    s[0:final_size] = s[len(s) - final_size:]
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_04_replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
