#!/usr/bin/env python3
# import random
# from time import time
#
# def sum_list_recursive(nums: list, **kwargs):
#     """Assess the sum of a list recursively."""
#     index = 0 if "index" not in kwargs else kwargs["index"]
#     total = 0 if "total" not in kwargs else kwargs["total"]
#     if index == len(nums):
#         return total
#     return sum_list_recursive(nums, index=index+1, total=total+nums[index])
#
# def sum_list_iterative(nums: list):
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
#
# def main():
#     """Run main functions."""
#     test_list = [random.randint(0, 100000) for _ in range(500)]
#     start = time()
#     print(sum_list_recursive(test_list))
#     print(f"Recursive Time: {time() - start}")
#     start = time()
#     print(sum_list_iterative(test_list))
#     print(f"Sum Time: {time() - start}")
#     start = time()
#     breakpoint()
#     print(sum(test_list))
#     print(f"Sum Time: {time() - start}")
#
#
# if __name__ == '__main__':
#     main()


print(dir(sum))
