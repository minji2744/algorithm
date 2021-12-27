import re
t = int(input())

def solution(n):
    pat = re.compile('(100+1+|01)+')
    if pat.fullmatch(n):
        return 'YES'
    return 'NO'

for _ in range(t):
    n = input()
    print(solution(n))