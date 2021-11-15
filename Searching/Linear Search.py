def main():
    example_array = [x for x in range(10,20)]

    user_input = 11

    for index, value in enumerate(example_array):
        
        if value is user_input:
            print(f'Value: {user_input}\nIndex: {index}')


if __name__ == "__main__":
    main()