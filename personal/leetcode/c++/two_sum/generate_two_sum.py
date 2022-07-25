#!/bin/env/python3
from random import randint, shuffle
from time import time
from tqdm import tqdm

V_OUTPUT = "test/vectors.txt"
T_OUTPUT = "test/targets.txt"
A_OUTPUT = "test/answer.txt"

PROBLEMS = 1000
N_LOWER_LIMIT = -(10**9)
N_UPPER_LIMIT = 10**9
T_LOWER_LIMIT = -(10**9)
T_UPPER_LIMIT = 10**9
V_SIZE_LIMIT = 10**4


def main():
    v_out = []
    t_out = []
    a_out = []
    # Generate vectors and target, and record answer.
    for _ in tqdm(range(PROBLEMS)):
        target = randint(T_LOWER_LIMIT, T_UPPER_LIMIT)
        first_value = randint(N_LOWER_LIMIT, N_UPPER_LIMIT)
        vector = [first_value, target - first_value]
        answers = list(vector)
        this_vector_size = randint(0, V_SIZE_LIMIT - 2)
        start = time()
        while len(vector) < this_vector_size and time() - start < 10:
            new_value = randint(N_LOWER_LIMIT, N_UPPER_LIMIT)
            if target - new_value not in vector:
                vector.append(new_value)
        shuffle(vector)
        a = [vector.index(x) for x in answers]
        v_out.append(vector)
        t_out.append(target)
        a_out.append(sorted(a))

    # Write lists to provided files.
    with open(V_OUTPUT, "w") as f:
        for line in v_out:
            f.write(" ".join(map(str, line)) + "\n")

    with open(T_OUTPUT, "w") as f:
        for target in t_out:
            f.write(str(target) + "\n")

    with open(A_OUTPUT, "w") as f:
        for a in a_out:
            f.write(" ".join(map(str, a)) + "\n")


if __name__ == "__main__":
    main()
