from functools import lru_cache
from time import perf_counter

'''
Problem: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
'''

def fib(n):
    '''
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    '''

    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

def DP_fib(n: int, mem = {}) -> int:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    if n == 0: return 0
    if n in mem: return mem[n]
        
    else:
        if n == 1 or n == 2: return 1
        mem[n] = DP_fib(n - 1, mem) + DP_fib(n - 2, mem)
            
        return mem[n]

@lru_cache
def cache_fib(n: int) -> int:
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    if n == 0: return 0
    if n == 1 or n == 2: return 1

    return cache_fib(n - 1) + cache_fib(n - 2)

def main():
    n = 45 #Result should be: 1,134,903,170

    original_time = perf_counter()
    original_fib = fib(n)
    original_time_result = perf_counter() - original_time
    
    DP_time = perf_counter()
    DP = DP_fib(n)
    DP_time_result = perf_counter() - DP_time

    cache_time = perf_counter()
    cached = cache_fib(n)
    cache_time_result = perf_counter() - cache_time

    result_0 = 'True' if original_fib == 1134903170 else 'False'
    result_1 = 'True' if DP == 1134903170 else 'False'
    result_2 = 'True' if cached == 1134903170 else 'False'

    print(f'Correct fib Result: {result_0}\nDuration: {original_time_result:.3E}s '
          f'({original_time_result/60:.3f} mins)\n\n'
          f'Correct DP_fib Result: {result_1}\nDuration: {DP_time_result:.3E}s\n\n'
          f'Correct cache_fib Result: {result_2}\nDuration: {cache_time_result:.3E}s\n')

    if DP_time_result < cache_time_result:
        print(f'DP_fib was faster by: {cache_time_result - DP_time_result:.3E}s')
    else:
        print(f'cache_fib was faster by: {DP_time_result - cache_time_result:.3E}s')

if __name__ == '__main__':
    main()