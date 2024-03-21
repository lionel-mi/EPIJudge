from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    lowcased_s = s.lower()
    while left < right:
        if lowcased_s[left] == lowcased_s[right]:
            left += 1
            right -= 1
        elif not lowcased_s[left].isalnum():
            left += 1
        elif not lowcased_s[right].isalnum():
            right -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '06_05_is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
