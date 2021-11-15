def binary_search(arr, user_in):
    #Assuming the array is sorted
    #Does not work if not sorted
    #IMPORTANT: THIS IS THE ITERATIVE VERSION
    low = 0
    mid = 0
    high = len(arr) - 1

    while high >= low:
        mid = (high + low ) // 2

        #Case 1: Solution is at the right
        if arr[mid] < user_in:
            low = mid + 1

        #Case 2: Solution is at the left
        elif arr[mid] > user_in:
            high = mid - 1

        #Case 3: Solution is the middle
        else:
            return mid

    #Default case: Solution is not found in the tree
    return -1

def main():
    test_array = [x for x in range(47, 91)]
    test_input = 69

    solution = binary_search(test_array, test_input)

    print(solution if solution != -1 else 'Input was not found.')


if __name__ == '__main__':
    main()