import matplotlib.pyplot as plt
from time import time
import math


class Plotter:
    def __init__(self):
        self.time_unit = self.initialize_time()

    def initialize_time(self):
        times = []
        for _ in range(1000):
            t1 = time()
            while (t2 := time()) == t1:
                pass
            times.append(t2 - t1)
        times.sort()
        return times[499]

    def get_n_time(self, n_value: int):
        return n_value * self.time_unit

    def get_nlogn_time(self, n_value: int):
        return n_value * math.log2(n_value) * self.time_unit

    def get_n2_time(self, n_value: int):
        return n_value**2 * self.time_unit

    def plot(self, n_values, result_times, n_times=True, nlogn_times=True, n2_times=True):
        indexes = list(range(len(n_values)))
        indexes.sort(key=n_values.__getitem__)
        n_values_sorted = list(map(n_values.__getitem__, indexes))
        result_times_sorted = list(map(result_times.__getitem__, indexes))

        plt.plot(n_values_sorted, result_times_sorted, c="b", label="results")

        if n_times:
            n_times = [self.get_n_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, n_times, c="yellow", label="n")

        if nlogn_times:
            nlogn_times = [self.get_nlogn_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, nlogn_times, c="darkorange", label="nlogn")

        if n2_times:
            n2_times = [self.get_n2_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, n2_times, c="r", label="n^2")

        plt.xlabel("N")
        plt.ylabel("Time")
        plt.title("Time Complexity Graph")
        ax = plt.gca()
        ax.set_ylim([0, max(result_times)])
        plt.show()
