"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0



Constraints:

    3 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
"""


from random import randint, choice, choices


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        counts = {}
        self.closest = sum(nums[:3])
        self.sdif = abs(target - self.closest)
        self.target = target
        nums.sort()
        nums_red = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] == 3:
                # Process triples here, reducing iterations by # triplets ^2 (or ^3?)
                if self.compare([num, num, num]):
                    return target
            if counts[num] < 3:
                # Reduce iterations by trimming excess list members.
                nums_red.append(num)
                if len(nums_red) >= 3 and self.compare(nums_red[-3:]):
                    return target

        # nums_red is sorted, so we can do a binary search to get closest result after <o(n^2)
        for ind, num1 in enumerate(nums_red):
            for j, num2 in enumerate(nums_red[ind + 1 :]):
                pair = num1 + num2
                wanted = target - pair
                # Skip binary search if diff is too big for number to be in list..
                if target < 0 and wanted <= nums_red[0]:
                    continue
                if target > 0 and wanted >= nums_red[-1]:
                    continue

                start = 0
                end = len(nums_red) - 1
                while start <= end:
                    mid = start + (end - start) // 2
                    num3 = nums_red[mid]
                    if counts[num3] - int(num1 == num3) - int(num2 == num3) > 0:
                        if self.compare([pair, num3]):
                            return target
                    if wanted > num3:
                        start = mid + 1
                    else:
                        end = mid - 1
        return self.closest

    def threeSumClosest2(self, nums: list, target: int) -> int:
        counts = {}
        self.closest = sum(nums[:3])
        self.sdif = abs(target - self.closest)
        self.target = target
        nums.sort()
        nums_red = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] == 3:
                # Process triples here, reducing iterations by # triplets ^2 (or ^3?)
                if self.compare([num, num, num]):
                    return target
            if counts[num] < 3:
                # Reduce iterations by trimming excess list members.
                nums_red.append(num)
                if len(nums_red) >= 3 and self.compare(nums_red[-3:]):
                    return target

        # nums_red is sorted, so we can do a binary search to get closest result after <o(n^2)
        for ind, num1 in enumerate(nums_red):
            if ind == len(nums_red) - 3:
                break
            for j, num2 in enumerate(nums_red[ind + 3 :]):
                pair = num1 + num2
                wanted = target - pair
                # Skip binary search if diff is too big for number to be in list..
                if target < 0 and wanted <= nums_red[0]:
                    continue
                if target > 0 and wanted >= nums_red[-1]:
                    continue

                start = 0
                end = len(nums_red) - 1
                while start <= end:
                    mid = start + (end - start) // 2
                    num3 = nums_red[mid]
                    if counts[num3] - int(num1 == num3) - int(num2 == num3) > 0:
                        if self.compare([pair, num3]):
                            return target
                    if wanted > num3:
                        start = mid + 1
                    else:
                        end = mid - 1
        return self.closest

    def compare(self, triplet: list) -> bool:
        res = sum(triplet)
        dif = abs(self.target - res)
        if dif < self.sdif:
            self.closest = res
            self.sdif = dif
        if dif == 0:
            return True
        return False

    @staticmethod
    def generate_tests(num_tests=10, keep_target_close=False):
        num_tests = max(min(num_tests, 1000), 1)  # Always generate between 1 and 1000 tests.
        arr_min_length = 3
        arr_max_length = 1000
        min_val = -1000
        max_val = 1000
        # min_val = -100
        # max_val = 100
        min_tar = -(10**4)
        max_tar = 10**4
        # min_val = -10
        # max_val = 10
        for _ in range(num_tests):
            if keep_target_close:
                yield [1, 1, 1, 0], -100
                # x = [randint(min_val, max_val) for _ in range(randint(arr_min_length, arr_max_length))]
                # yield x, sum(choices(x, k=3)) + choice([-1500, 1500])
            else:
                yield [randint(min_val, max_val) for _ in range(randint(arr_min_length, arr_max_length))], randint(min_tar, max_tar)


if __name__ == "__main__":
    s = Solution()
    results = []
    for test in s.generate_tests(keep_target_close=False):
        print(test[1], ":\t", sep="", end="", flush=True)
        print(s.threeSumClosest(test[0], test[1]), "\t", sep="", end="", flush=True)
        print(result := s.threeSumClosest2(test[0], test[1]))
        results.append(result)
