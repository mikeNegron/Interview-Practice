#Maximum Sum Sub-Array problem solution

def kadane_algo(arr: list[int])-> int:
    curr_sum = arr[0]
    max_sum = curr_sum

    for i in arr[1:]:
        curr_sum = max(i + curr_sum, i)
        max_sum = max(curr_sum, max_sum)

    return max_sum

def main():
    test = [5,4,-1,7,8]

    result = kadane_algo(test)
    temp = bin(15)
    print(temp[2:])

        

if __name__ == '__main__':
    main()