import math
n = int(input())

def solution(n):
    if n == 1:
        return 0
    primes = [False,False] + [True] * (n-1)
    for i in range(2, int(math.sqrt(n))+2):
        if primes[i]:
            for j in range(i*2, n+1, i):
                primes[j] = False
    prime_list = [i for i, prime in enumerate(primes) if prime]

    count = 0
    end, interval = 0, 0
    m = len(prime_list)
    for start in range(m):
        while interval < n and end < m:
            interval += prime_list[end]
            end += 1
        if interval == n:
            count += 1
        interval -= prime_list[start]
    return count
print(solution(n))