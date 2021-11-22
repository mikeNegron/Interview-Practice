def first_unique(s: str) -> int:
    hashmap = {}

    if s != '':
        for val in s:
            if val not in hashmap:
                hashmap[val] = 1
            else: hashmap[val] += 1

        for idx, i in enumerate(s):
            if hashmap[i] == 1: return idx

    else: return -1

def main():
    test1 = 'tree' #First unique at 0 idx

if __name__ == '__main__':
    main()