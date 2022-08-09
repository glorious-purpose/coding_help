from random import randint
from time import time
from math import log2
import matplotlib.pyplot as plt
from merge_sort import merge_sort


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)
        subs = []
        ml = 1
        max_num_so_far = None
        for i, num in reversed(list(enumerate(nums))):
            if max_num_so_far is None or num >= max_num_so_far:
                max_num_so_far = num
                subs.append(Entry(i, num, 1))
                continue
            ml_this_num = 1
            for entry in reversed(subs):
                if num > entry:
                    continue
                elif num == entry:
                    subs.append(Entry(i, num, entry.length))
                    break
                ml_this_num = max(ml_this_num, entry.length + 1)
            else:
                subs.append(Entry(i, num, ml_this_num))
                ml = max(ml, ml_this_num)
        return ml


class Entry:
    def __init__(self, index: int, value: int, length: int):
        self.index = index
        self.value = value
        self.length = length

    def __lt__(self, other):
        if isinstance(other, Entry):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if isinstance(other, Entry):
            return self.value > other.value
        return self.value > other


def generate_tests(num_tests=10):
    num_tests = max(min(num_tests, 1000), 0)
    tests = []
    for _ in range(num_tests):
        test = []
        for i in range(1 + randint(1, 10000)):
            test.append(randint(-(10**4), 10**4))
        tests.append(test)
    return tests


def n_time(n_list: list, *args) -> None:
    c = [x * 2 for x in n_list]
    del c
    return


def n_logn_time(n_list: list, *args) -> None:
    c = list(n_list)
    merge_sort(c)
    del c
    return


def n_2_time(n_list: list, *args) -> None:
    c = [x * y for x in n_list for y in n_list]
    del c
    return


if __name__ == "__main__":
    s = Solution()
    tests = [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3], [7, 7, 7, 7, 7, 7, 7]]
    tests.extend(generate_tests(500))
    times = []
    lens = list(map(len, tests))
    for test in tests:
        start = time()
        # s.lengthOfLIS(test)
        times.append(time() - start)
        # print(s.lengthOfLIS(test))
        # print(f"N={len(test)}\n{(tt := time()-start):.10f}ms taken.")
        # times.append(tt)

    indexes = list(range(len(lens)))
    indexes.sort(key=lens.__getitem__)
    times_sorted = list(map(times.__getitem__, indexes))
    lens_sorted = list(map(lens.__getitem__, indexes))
    n_times = []
    n_logn_times = []
    n_2_times = []
    for test in tests:
        start = time()
        n_time(test)
        n_times.append(time() - start)

    for test in tests:
        start = time()
        n_logn_time(test)
        n_logn_times.append(time() - start)

    for test in tests:
        start = time()
        n_2_time(test)
        n_2_times.append(time() - start)
    n_times_sorted = list(map(n_times.__getitem__, indexes))
    n_logn_times_sorted = list(map(n_logn_times.__getitem__, indexes))
    n_2_times_sorted = list(map(n_2_times.__getitem__, indexes))

    # plt.plot(lens_sorted, times_sorted, c="b", label="results")
    plt.plot(lens_sorted, n_times_sorted, c="yellow", label="n")
    plt.plot(lens_sorted, n_logn_times_sorted, c="darkorange", label="nlogn")
    plt.plot(lens_sorted, n_2_times_sorted, c="r", label="n^2")
    # plt.plot(n_values, n_e_values, label="2^n")

    plt.xlabel("N")
    plt.ylabel("Time (ms)")
    plt.title("Time Complexity Graph")
    plt.show()
