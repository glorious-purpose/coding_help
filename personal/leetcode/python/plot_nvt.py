import matplotlib.pyplot as plt
from time import time
import math
import numpy as np


class Plotter:
    def __init__(self):
        self.time_unit = self.initialize_time()
        self.mst = 0
        self.n_values = None

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

    def get_2n_time(self, n_value: int):
        return 2**n_value * self.time_unit

    def get_nf_time(self, n_value: int):
        n_value = min(n_value, 170)
        return math.factorial(n_value) * self.time_unit

    def plot(self, n_values, result_times, plot_n=True, plot_nlogn=True, plot_n2=True, plot_2n=True, plot_nf=True, c="b"):
        if self.n_values is not None and len(n_values) != self.n_values:
            raise ValueError(f"{len(n_values)} does not match previous plot's {self.n_values}.")
        self.n_values = len(n_values)
        indexes = list(range(len(n_values)))
        indexes.sort(key=n_values.__getitem__)
        n_values_sorted = list(map(n_values.__getitem__, indexes))
        result_times_sorted = list(map(result_times.__getitem__, indexes))
        self.mst = max(self.mst, max(result_times))

        plt.scatter(n_values_sorted, result_times_sorted, c=c, label="results")
        z = np.polyfit(n_values_sorted, result_times_sorted, 2)
        p = np.poly1d(z)
        plt.plot(n_values_sorted, p(n_values_sorted), c=c)

        if plot_n:
            calc_times = [self.get_n_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, calc_times, c="yellow", label="n")

        if plot_nlogn:
            calc_times = [self.get_nlogn_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, calc_times, c="darkorange", label="nlogn")

        if plot_n2:
            calc_times = [self.get_n2_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, calc_times, c="r", label="n^2")

        if plot_2n:
            calc_times = [self.get_2n_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, calc_times, c="purple", label="n^2")

        if plot_nf:
            calc_times = [self.get_nf_time(x) for x in n_values_sorted]
            plt.plot(n_values_sorted, calc_times, c="darkred", label="n^2")

    def show(self):
        plt.xlabel("N")
        plt.ylabel("Time")
        plt.title("Time Complexity Graph")
        ax = plt.gca()
        ax.set_ylim([0, self.mst])
        plt.show()
