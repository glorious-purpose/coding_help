"""
901. Online Stock Span
Medium
4.3K
279
Companies

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

    For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].

Implement the StockSpanner class:

    StockSpanner() Initializes the object of the class.
    int next(int price) Returns the span of the stock's price given that today's price is price.



Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6



Constraints:

    1 <= price <= 105
    At most 104 calls will be made to next.
"""


class StockSpanner:
    def __init__(self):
        self._his = []
        self._pos = 0

    def next(self, price: int) -> int:
        max_pos = 0
        self._pos += 1
        temp = (price, (cur_pos := self._pos))
        # O(n) operation to insert new price and retrieve max pos of greater
        # values.
        for idx, (entry, pos) in enumerate(self._his):
            if entry <= price:
                # We only care about values greater than the current price.
                continue
            max_pos = max(max_pos, pos)
            # Insert new price, shifting existing values to the right.
            self._his[idx] = temp
            temp = (entry, pos)
        self._his.append(temp)
        return cur_pos - max_pos


if __name__ == "__main__":
    tests = [100, 80, 60, 70, 60, 75, 85]
    answs = [1, 1, 1, 2, 1, 4, 6]
    stocks = StockSpanner()
    for test, ans in zip(tests, answs):
        assert (res := stocks.next(test)) == ans, f"next({test}) Failed. {res} != {ans}"
