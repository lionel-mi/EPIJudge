from test_framework import generic_test


def look_and_say(n: int) -> str:
    prev = ["1"]
    for _ in range(n-1):
        next = []
        idx = 1
        curr_digit = prev[0]
        counter = 1
        while idx < len(prev):
            if prev[idx] == curr_digit:
                counter += 1
            else:
                next.append(str(counter))
                next.append(curr_digit)
                counter = 1
                curr_digit = prev[idx]
            idx += 1
        next.append(str(counter))
        next.append(prev[-1])
        prev = next
    sol =  "".join(prev)
    return sol



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('06_07_look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
