def to_base_n(number: list[int], base: int, n_base: int) -> str:
    result_dec = []
    result_n = []
    length = len(number)
    
    for num in number:
        result_dec.append(num * pow(base, length := length - 1))
    
    dec_val = sum(result_dec)

    if n_base != 10:
        while (sentinel := dec_val // n_base) >= 0:
            result_n.append(str(dec_val - (sentinel * n_base)))

            if sentinel == 0:
                result_n.reverse()
                break

            else: dec_val = sentinel
        return ''.join(result_n)

    else: return str(dec_val)

def main():
    A_to_J = [chr(i) for i in range(65, 75)]
    a_j_equivalent = {A_to_J[idx] : (idx + 10) for idx in range(len(A_to_J))}

    temp, old_base = [1, 0, 1, 1], 3
    temp_str = [str(i) for i in temp]
    new_base = 10

    for idx, check in enumerate(temp):
        if isinstance(check, str):
            temp[idx] = a_j_equivalent[check]

    original = ''.join(temp_str)
    conversion = to_base_n(temp, old_base, new_base)

    print(f'Old Number: {original}\nOld Base: {old_base}\n'
        f'New Number: {conversion}\nNew Base: {new_base}')


if __name__ == '__main__':
    main()