import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_word(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    idx = -1
    while idx < len(s):
        prev_idx = idx+1
        idx += 1
        while idx < len(s) and(s[idx] != "" and s[idx] != " "):
            idx += 1
        reverse_word(prev_idx, idx-1)

    reverse_word(0, len(s)-1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_06_reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
