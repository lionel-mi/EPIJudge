from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    num = 0
    for ch in col.lower():
        d = ord(ch) - ord('a') + 1
        num = num * 26 + d

    return num



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_03_spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
