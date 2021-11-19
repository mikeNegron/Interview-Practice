#Maximum Sum Sub-Array problem solution


def kadane_algo(arr: list[int])-> int:
    curr_sum = arr[0]
    max_sum = curr_sum

    for i in arr:
        curr_sum = max(i + curr_sum, i)
        max_sum = max(curr_sum, max_sum)

    return max_sum

def main():
    test = [-2, 2, 5, -11, 6]

    result = kadane_algo(test)

    print(result)

if __name__ == '__main__':
    main()