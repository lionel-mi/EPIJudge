from test_framework import generic_test


def snake_string(s: str) -> str:
    sol_lst = []
    for idx in range(1, len(s), 4):
        sol_lst.append(s[idx])
    for idx in range(0, len(s), 2):
        sol_lst.append(s[idx])
    for idx in range(3, len(s), 4):
        sol_lst.append(s[idx])
    return "".join(sol_lst)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_10_snake_string.py', 'snake_string.tsv',
                                       snake_string))
