def first_unique(s: str) -> int:
    hashmap = {}

    if s:
        for val in s:
            if val not in hashmap:
                hashmap[val] = 1
            else: hashmap[val] += 1

        for idx, i in enumerate(s):
            if hashmap[i] == 1: return idx
    return -1

def main():
    test = 'ttree' #First unique at 0 idx

    result = first_unique(test)

    print(f'The first unique character is found at index: {result}')

if __name__ == '__main__':
    main()