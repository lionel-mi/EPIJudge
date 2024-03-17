import collections
import functools
import math
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook


def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:
    aggregated_probabilities = []
    aggregated_probabilities.append(probabilities[0])
    for p in probabilities[1:]:
        aggregated_probabilities.append(p + aggregated_probabilities[-1])

    random_num = random.random()
    for idx, p in enumerate(aggregated_probabilities):
        if p > random_num:
            return values[idx]
    return values[-1]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda: [
            nonuniform_random_number_generation(values, probabilities)
            for _ in range(N)
        ])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            '05_16_nonuniform_random_number.py', 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
