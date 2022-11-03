"""
433. Minimum Genetic Mutation
Medium
1.9K
197
Companies

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3



Constraints:

    start.length == 8
    end.length == 8
    0 <= bank.length <= 10
    bank[i].length == 8
    start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

"""
from unittest import TestCase, main
from collections import defaultdict, deque


class Solution(TestCase):
    def min_mutation(self, start: str, end: str, bank: list[str]) -> int:
        if end not in bank:
            return -1

        def gene_diff(gene1: str, gene2: str) -> int:
            if len(gene1) != len(gene2):
                raise ValueError("Genes are not the same length.")
            diff_count = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    diff_count += 1
            return diff_count

        stack = [(start, 0, {start})]
        lowest_count = None
        while len(stack) > 0:
            mutation, count, visited = stack.pop()
            if lowest_count is not None and count >= lowest_count:
                continue
            for gene in bank:
                if gene_diff(mutation, gene) == 1 and gene not in visited:
                    if gene == end:
                        lowest_count = min(lowest_count, count + 1) if lowest_count is not None else count + 1
                    visited.add(gene)
                    stack.append((gene, count + 1, visited))
        if lowest_count is None:
            return -1
        return lowest_count

    def min_mutation2(self, start: str, end: str, bank: list[str]) -> int:
        if end not in bank:
            return -1

        def gene_diff(gene1: str, gene2: str) -> int:
            if len(gene1) != len(gene2):
                raise ValueError("Genes are not the same length.")
            diff_count = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    diff_count += 1
            return diff_count

        queue = [(start, 0, {start})]
        lowest_count = None
        while len(queue) > 0 and len(bank) > 0:
            mutation, count, visited = queue.pop(0)
            rem = []
            for idx, gene in enumerate(bank):
                if gene_diff(mutation, gene) == 1 and gene not in visited:
                    if gene == end:
                        return count + 1
                    visited.add(gene)
                    rem.append(idx)
                    queue.append((gene, count + 1, visited))
            for idx in reversed(rem):
                bank.pop(idx)
        if lowest_count is None:
            return -1
        return lowest_count

    def test_0(self, func=None):
        test, ans = ("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1
        func = self.min_mutation if func is None else func
        self.assertEqual(func(*test), ans)

    def test_1(self, func=None):
        test, ans = ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2
        func = self.min_mutation if func is None else func
        self.assertEqual(func(*test), ans)

    def test_2(self, func=None):
        test, ans = ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]), 3
        func = self.min_mutation if func is None else func
        self.assertEqual(func(*test), ans)

    def test_3(self, func=None):
        test, ans = ("AAAACCCC", "CCCCCCCC", ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]), 4
        func = self.min_mutation if func is None else func
        self.assertEqual(func(*test), ans)


if __name__ == "__main__":
    from timeit import timeit

    s = Solution()
    func1 = "min_mutation"
    func2 = "min_mutation2"

    def run_tests(func):
        for test in sorted([method for method in dir(Solution) if method.startswith("test")]):
            # Run the given test, providing a specific function to test.
            getattr(s, test)(getattr(s, func))

    print(timeit("run_tests(func1)", globals=locals()))
    print(timeit("run_tests(func2)", globals=locals()))
    # main()
