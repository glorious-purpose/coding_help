from random import choice, randint
from string import printable, ascii_lowercase

PROBLEMS = 100
STRING_LENGTH = 10**4 * 5
CHARS = ascii_lowercase
OUTPUT_FILE = "test/strings.txt"
ANSWERS_FILE = "test/answers.txt"


def lolsub(s: str) -> int:
    if len(s) < 2:
        return len(s)
    ls = 0
    cs = ""
    for c in s:
        if c in cs:
            cs = cs[cs.index(c) + 1 :]
        cs += c
        ls = max(ls, len(cs))

    return ls


def main():
    problem_set = []
    answers = []
    for _ in range(PROBLEMS):
        problem = ""
        for _ in range(randint(0, STRING_LENGTH)):
            problem += choice(CHARS)
        problem_set.append(problem)
        answers.append(str(lolsub(problem)))
    with open(OUTPUT_FILE, "w", encoding="utf8") as f:
        f.write("\n".join(problem_set))
    with open(ANSWERS_FILE, "w", encoding="utf8") as f:
        f.write("\n".join(answers))


if __name__ == "__main__":
    main()
