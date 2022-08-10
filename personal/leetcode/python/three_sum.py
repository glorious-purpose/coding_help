"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.



Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

"""

from random import randint


class Solution:
    def threeSum(self, nums: list) -> list:
        # Identify outliers.
        outliers = set()
        sorted_nums = sorted(set(nums))
        i = 0
        j = -1
        while sorted_nums[i] < 0 < sorted_nums[j]:
            if abs(sorted_nums[i]) > (2 * sorted_nums[j]):
                outliers.add(sorted_nums[i])
                i += 1
            elif sorted_nums[j] > -2 * sorted_nums[i]:
                outliers.add(sorted_nums[j])
                j -= 1
            else:
                break
        # Build separate sets and get 0 count in one O(n) pass.
        pos_nums = set()
        neg_nums = set()
        triplets = set()
        counts = {}
        for num in nums:
            if num in outliers:
                continue
            counts[num] = counts.get(num, 0) + 1
            if num > 0:
                pos_nums.add(num)
            elif num < 0:
                neg_nums.add(num)

        if counts.get(0, 0) >= 3:
            triplets.add((0, 0, 0))

        if len(pos_nums) > 0 and len(neg_nums) > 0:
            # Run through combinations to see if triplets can be made.
            for p_val in pos_nums:
                for n_val in neg_nums:
                    if p_val > -2 * n_val:
                        break
                    addend = -(p_val + n_val)
                    if counts.get(addend, 0) >= 1 + int(p_val == addend) + int(n_val == addend):
                        triplets.add((min(n_val, addend), min(max(n_val, addend), p_val), max(addend, p_val)))

        return list(map(list, triplets))

    def three_sum(self, nums: list) -> list:
        nums = sorted(nums)
        nums_set = sorted(set(nums))
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        triplets = set()
        for n_num in nums_set:
            if n_num > 0:
                break
            for p_num in reversed(nums_set):
                if abs(n_num) > 2 * p_num or p_num < 0:
                    break
                if counts.get((addend := -(p_num + n_num)), 0) >= int(p_num == addend) + int(n_num == addend) + 1:
                    triplets.add((min(n_num, addend), min(max(n_num, addend), p_num), max(addend, p_num)))
        return list(map(list, triplets))

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)  # Always generate between 1 and 1000 tests.
        arr_min_length = 3
        arr_max_length = 3000
        # arr_max_length = 10
        min_val = -105
        max_val = 105
        # min_val = -10
        # max_val = 10
        for _ in range(num_tests):
            yield [randint(min_val, max_val) for _ in range(randint(arr_min_length, arr_max_length))]


if __name__ == "__main__":
    s = Solution()
    results = []
    for test in s.generate_tests():
        print(test)
        print(result := s.threeSum(test))
        results.append(result)
    for result in results:
        for num_set in result:
            assert sum(num_set) == 0, f"Bad result {num_set}"
