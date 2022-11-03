"""
2034. Stock Price Fluctuation
Medium
767
44
Companies

You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

    Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
    Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
    Finds the maximum price the stock has been based on the current records.
    Finds the minimum price the stock has been based on the current records.

Implement the StockPrice class:

    StockPrice() Initializes the object with no price records.
    void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
    int current() Returns the latest price of the stock.
    int maximum() Returns the maximum price of the stock.
    int minimum() Returns the minimum price of the stock.



Example 1:

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.



Constraints:

    1 <= timestamp, price <= 109
    At most 105 calls will be made in total to update, current, maximum, and minimum.
    current, maximum, and minimum will be called only after update has been called at least once.

"""
from unittest import TestCase, main


# class StockPrice:
#     max_changes = 0
#     min_changes = 0
#     lat_changes = 0
#     resets = 0
#
#     def __init__(self):
#         self._history = {}
#         self._current_val = None
#         self._minimum = None
#         self._maximum = None
#         self._latest_ts = None
#         self._minimum_ts = set()
#         self._maximum_ts = set()
#
#     def update(self, timestamp: int, price: int) -> None:
#         """Use incoming values to add to or change stock history"""
#         self._history[timestamp] = price
#         if self._latest_ts is None:
#             self._latest_ts = timestamp
#             self._minimum_ts.add(timestamp)
#             self._maximum_ts.add(timestamp)
#             self._current_val = price
#             self._maximum = price
#             self._minimum = price
#             self.max_changes = 0
#             self.min_changes = 0
#             self.lat_changes = 0
#             self.resets = 0
#             return
#         if timestamp >= self._latest_ts:
#             self._latest_ts = timestamp
#             if self._current_val != price:
#                 self.lat_changes += 1
#             self._current_val = price
#         if self._minimum is not None:
#             if price <= self._minimum:
#                 self.set_min(price, timestamp, self._minimum is None)
#             elif timestamp in self._minimum_ts:
#                 self._minimum_ts.remove(timestamp)
#             if len(self._minimum_ts) == 0:
#                 self._minimum = None
#         if self._maximum is not None:
#             if price >= self._maximum:
#                 self.set_max(price, timestamp, self._maximum is None)
#             elif timestamp in self._maximum_ts:
#                 self._maximum_ts.remove(timestamp)
#             if len(self._maximum_ts) == 0:
#                 self._maximum = None
#
#     def find_minmax(self) -> None:
#         """Run through all values and set min and max values and timestamp sets."""
#         self.resets += 1
#         timestamps = list(self._history.keys())
#         init_price = self._history[timestamps[0]]
#         self.set_max(init_price, timestamps[0], True)
#         self.set_min(init_price, timestamps[0], True)
#         for i in range(1, len(timestamps)):
#             price = self._history[timestamps[i]]
#             if price >= self._maximum:
#                 self.set_max(price, timestamps[i])
#             elif price <= self._minimum:
#                 self.set_min(price, timestamps[i])
#
#     def set_max(self, price: int, timestamp: int, reset: bool = False) -> None:
#         """Change max to reflect maximum or update max_ts."""
#         if reset or price > self._maximum:
#             self._maximum_ts.clear()
#             self._maximum = price
#         self._maximum_ts.add(timestamp)
#         self.max_changes += 1
#
#     def set_min(self, price: int, timestamp: int, reset: bool = False):
#         """Change min to reflect maximum or update min_ts."""
#         if reset or price < self._minimum:
#             self._minimum_ts.clear()
#             self._minimum = price
#         self._minimum_ts.add(timestamp)
#         self.min_changes += 1
#
#     def current(self) -> int:
#         """Return value of latest timestamp."""
#         return self._current_val
#
#     def maximum(self) -> int:
#         """Return maximum recorded value."""
#         if self._maximum is None:
#             self.find_minmax()
#         return self._maximum
#
#     def minimum(self) -> int:
#         """Return minimum recorded value."""
#         if self._minimum is None:
#             self.find_minmax()
#         return self._minimum
#
#     def parse_cmd(self, cmd, *args, **kwargs):
#         cmd = getattr(self, cmd)
#         return cmd(*args, **kwargs)


class StockPrice:
    def __init__(self):
        self._cur = None
        self._sorted_stocks = []
        self._stocks_by_val = {}
        self._stocks = {}

    def update(self, time, price):
        if self._cur is None:
            self._cur = time
            self._stocks[time] = price
            self._sorted_stocks.append(price)
            self._stocks_by_val[price] = 1
            return
        self._cur = max(time, self._cur)
        # Get current price from timestamp, if exists.
        cur_price = self._stocks.get(time, None)
        self._stocks[time] = price

        if price not in self._stocks_by_val:
            # If new price, add to sorted list and count dict.
            self._sort(price)
        self._stocks_by_val[price] = self._stocks_by_val.get(price, 0) + 1

        if cur_price is not None:
            # Reduce count. Del from sorted list and dict if 0.
            new_count = self._stocks_by_val[cur_price] - 1
            if new_count == 0:
                self._drop(cur_price)
            else:
                self._stocks_by_val[cur_price] = new_count

    def _sort(self, new_price):
        l_p = 0
        r_p = len(self._sorted_stocks)
        while l_p < r_p:
            m_p = (l_p + r_p) // 2
            if self._sorted_stocks[m_p] < new_price:
                l_p = m_p + 1
            else:
                r_p = m_p
        self._sorted_stocks[l_p:l_p] = [new_price]

    def _drop(self, old_price):
        self._stocks_by_val.pop(old_price)
        l_p = 0
        r_p = len(self._sorted_stocks)
        while l_p < r_p:
            m_p = (l_p + r_p) // 2
            if self._sorted_stocks[m_p] < old_price:
                l_p = m_p + 1
            else:
                r_p = m_p
        self._sorted_stocks.pop(l_p)

    def current(self):
        return self._stocks[self._cur]

    def maximum(self):
        return self._sorted_stocks[-1]

    def minimum(self):
        return self._sorted_stocks[0]

    def parse_cmd(self, cmd, *args, **kwargs):
        cmd = getattr(self, cmd)
        return cmd(*args, **kwargs)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


class Test(TestCase):
    def setUp(self):
        print("\n------Start------\n")
        self.stock = StockPrice()
        self.stock.update(1, 10)
        self.stock.update(2, 5)

    def tearDown(self):
        print("\n-------End-------\n")

    def test_1(self):
        self.assertEqual(self.stock.current(), 5, f"Current: {self.stock.current()} is not 5.")
        self.assertEqual(self.stock.maximum(), 10, f"Maximum: {self.stock.maximum()} is not 10.")
        self.assertEqual(self.stock.minimum(), 5, f"Minimum: {self.stock.minimum()} is not 5.")

    def test_2(self):
        self.stock.update(1, 3)
        self.assertEqual(self.stock.current(), 5, f"Current: {self.stock.current()} is not 5.")
        self.assertEqual(self.stock.maximum(), 5, f"Maximum: {self.stock.maximum()} is not 5.")
        self.assertEqual(self.stock.minimum(), 3, f"Minimum: {self.stock.minimum()} is not 3.")

    def test_3(self):

        self.stock.update(1, 3)

        self.stock.update(4, 2)

        self.assertEqual(self.stock.current(), 2, f"Current: {self.stock.current()} is not 5.")
        self.assertEqual(self.stock.maximum(), 5, f"Maximum: {self.stock.maximum()} is not 5.")
        self.assertEqual(self.stock.minimum(), 2, f"Minimum: {self.stock.minimum()} is not 3.")

    def test_timeout(self):
        with open("test/stock_price_input_cmds.txt", "r") as file:
            cmds = file.readlines()
        with open("test/stock_price_input_vals.txt", "r") as file:
            vals = file.readlines()
        with open("test/stock_price_output.txt", "r") as file:
            answers = file.readlines()
        for idx, entry in enumerate(answers):
            if "null" in entry:
                answers[idx] = None
                continue
            if "\n" in entry:
                answers[idx] = entry[:-1]

            try:
                answers[idx] = int(entry)
            except Exception as e:
                print(e)
                raises
        del self.stock
        self.stock = StockPrice()
        print("Running Command: 0", end="", flush=True)
        for i in range(1, len(cmds)):
            print("\b" * len(str(i - 1)) + str(i), end="", flush=True)
            # cmd = getattr(self.stock, cmds[i].strip("\n"))
            args = vals[i].strip("[]\n").split(",")
            if len(args) == 1:
                res = self.stock.parse_cmd(cmds[i].strip("\n"))
            else:
                args = list(map(int, args))
                res = self.stock.parse_cmd(cmds[i].strip("\n"), *args)
            self.assertEqual(res, answers[i])

    def test_timeout2(self):
        source = "test/stock_price_input_{}.txt"
        with open(source.format("cmds-9"), "r") as file:
            cmds = file.readlines()
        with open(source.format("vals-9"), "r") as file:
            vals = file.readlines()
        del self.stock
        self.stock = StockPrice()
        print("Running Command: 0", end="", flush=True)
        for i in range(1, len(cmds)):
            print("\b" * len(str(i - 1)) + str(i), end="", flush=True)
            # cmd = getattr(self.stock, cmds[i].strip("\n"))
            args = vals[i].strip("[]\n").split(",")
            if len(args) == 1:
                res = self.stock.parse_cmd(cmds[i].strip("\n"))
            else:
                args = list(map(int, args))
                res = self.stock.parse_cmd(cmds[i].strip("\n"), *args)
            # self.assertEqual(res, answers[i])


if __name__ == "__main__":
    main()
