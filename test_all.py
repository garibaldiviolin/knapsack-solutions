from time import monotonic

from take_and_release import knapsack as take_and_release_knapsack
from naive_recursion import knapsack as naive_recursion_knapsack
from dynamic_programming import knapsack as dynamic_programming_knapsack


def time_algorithm(algorithm, times):
    """Call the algorithm for n times."""
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)

    start = monotonic()
    for _ in range(times):
        max_value = algorithm(W, wt, val, n)
    end = monotonic()

    interval = end - start

    print("max_value={}, interval={:0.10f}".format(max_value, interval))


algorithms = [naive_recursion_knapsack, dynamic_programming_knapsack, take_and_release_knapsack]

for algorithm in algorithms:
    time_algorithm(algorithm, 50)
