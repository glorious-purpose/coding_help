"""
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

    If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
    If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.

Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.



Example 1:

Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

Example 2:

Input: tokens = [100,200], power = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.

Example 3:

Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.



Constraints:

    0 <= tokens.length <= 1000
    0 <= tokens[i], power < 104
"""
from random import randint
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        while len(tokens) > 0:
            if power >= tokens[0]:
                power -= tokens.pop(0)
                score += 1
            elif score > 0 and len(tokens) > 1 and power + tokens[-1] >= tokens[0]:
                power += tokens.pop()
                score -= 1
            else:
                break
        return score

    @staticmethod
    def generate_tests(num_tests=10):
        num_tests = max(min(num_tests, 1000), 1)
        VAL_MIN = 0
        VAL_MAX = 10000
        LEN_MIN = 0
        LEN_MAX = 1000

        for _ in range(num_tests):
            this_test_length = randint(LEN_MIN, LEN_MAX)
            this_test = [randint(VAL_MIN, VAL_MAX) for _ in range(this_test_length)]
            yield this_test, randint(VAL_MIN, VAL_MAX)


if __name__ == "__main__":
    s = Solution()
    print(s.bagOfTokensScore([71, 55, 82], 54))
    tests = s.generate_tests(10)
    # for test in tests:
    #     print(s.bagOfTokensScore(*test))
