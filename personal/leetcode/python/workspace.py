from plot_nvt import Plotter
from longest_increasing_subsequence import Solution as subseq
from merge_sort import merge_sort
from binary_trees_with_factors import Solution as bt_factors
from three_sum import Solution as three_sum
from time import time
from tqdm import tqdm


def main(fn, tests):
    n_values = []
    times = []
    print("Testing Solution...\nTest:  ", end="")
    count = 0
    for test in tests:
        print("\b" * len(str(count)), end="")
        count += 1
        print(count, end="", flush=True)
        n_values.append(len(test))
        start = time()
        fn(test)
        times.append(time() - start)
    return n_values, times


if __name__ == "__main__":
    plt = Plotter()

    # Test binary_trees_with_factors Solution
    sol = three_sum()
    n_values, result_times = main(sol.threeSum, sol.generate_tests(500))
    plt.plot(n_values, result_times)
