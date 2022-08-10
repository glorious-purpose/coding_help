"""
Given a sequence, find the longest sub-sequence (doesn't need to be sequential.).

I wound up needing help to figure this one out. My solutions were trending towards 2^n.
I couldn't crack how to optimize for nlogn performance, because I was focused on looking at the original list.
Turns out the solution was to build the subsequence as you go, replacing high numbers with lowers allowing the
subsequence to morph into a different subsequence as needed.
"""
from random import randint  # For generating tests


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) in [0, 1]:
            return len(nums)
        sub_list = [nums[0]]
        for num in nums[1:]:
            if num < sub_list[-1]:
                l_ptr = 0
                u_ptr = len(sub_list) - 1
                while l_ptr <= u_ptr:
                    m_ptr = l_ptr + (u_ptr - l_ptr) // 2
                    if sub_list[m_ptr] < num:
                        l_ptr = m_ptr + 1
                        continue
                    u_ptr = m_ptr - 1
                sub_list[l_ptr] = num
            elif sub_list[-1] != num:
                sub_list.append(num)
        return len(sub_list)

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 0)
        for _ in range(num_tests):
            test_set = []
            for _ in range(1 + randint(1, 2500)):
                test_set.append(randint(-(10**4), 10**4))
            yield test_set


if __name__ == "__main__":
    s = Solution()
    tests = [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3], [7, 7, 7, 7, 7, 7, 7]]
    print("Generating tests...")
    tests.extend(s.generate_tests(1000))
    print("Testing Solution...")
    for test in tests:
        print(s.lengthOfLIS(test))
