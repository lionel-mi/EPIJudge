from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    sol = []
    parts = [["0"]] * 4
    def is_valid(part):
        return len(part) == 1 or (len(part) > 0 and part[0] != "0" and int(part) <= 255)

    for idx1 in range(1, 4):
        if is_valid(s[:idx1]):
            parts[0] = s[:idx1]
            for idx2 in range(idx1+1, idx1+4):
                if is_valid(s[idx1: idx2]):
                    parts[1] = s[idx1: idx2]
                    for idx3 in range(idx2+1, min(idx2+4, len(s))):
                        if is_valid(s[idx2:idx3]) and is_valid(s[idx3:]):
                            parts[2] = s[idx2:idx3]
                            parts[3] = s[idx3:]
                            sol.append(".".join(parts))
    return sol





def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_09_valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
