l, r = map(int, input().split())
def solution(l,r):
    count = 1e9
    for i in range(l,r+1):
        if '8' not in str(i):
            return 0
        else:
            count = min(count,str(i).count('8'))
    return count
print(solution(l,r))