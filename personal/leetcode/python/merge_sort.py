def merge_sort(data_list: list, start: int = 0, end: int = None):
    if end is None:
        end = len(data_list) - 1
    if start < end:
        middle = start + ((end - start) // 2) + 1
        merge_sort(data_list, start, middle - 1)
        merge_sort(data_list, middle, end)
        merge(data_list, start, middle, end)


def merge(data_list: list, start: int, middle: int, end: int):
    left = data_list[start:middle]
    right = data_list[middle : end + 1]

    l_ptr = 0
    r_ptr = 0
    d_ind = start

    while l_ptr < len(left) and r_ptr < len(right):
        if right[r_ptr] < left[l_ptr]:
            data_list[d_ind] = right[r_ptr]
            r_ptr += 1
        else:
            data_list[d_ind] = left[l_ptr]
            l_ptr += 1
        d_ind += 1

    while l_ptr < len(left):
        data_list[d_ind] = left[l_ptr]
        l_ptr += 1
        d_ind += 1

    while r_ptr < len(right):
        data_list[d_ind] = right[r_ptr]
        r_ptr += 1
        d_ind += 1


if __name__ == "__main__":
    from random import randint

    tests = [[randint(-100000, 100000) for _ in range(randint(50, 10000))] for _ in range(1000)]
    times = []
    for test in tests:
        merge_sort(test)
    i = 0
    j = 1
    while j < len(test):
        assert test[i] <= test[j], f"{test[i]} is not less than or equal to {test[i]}."
        i += 1
        j += 1
    print("Test successful.")
