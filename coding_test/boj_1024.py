def solution(n, l):
    Found = False
    while not Found:
        if l > 100:
            return -1
        if (n*2/l -l+1) % 2 == 0:
            start = (n*2/l -l+1)/2
            if start >= 0:
                break
        l += 1
    
    answer = [int(start+i) for i in range(l)]
    return answer

n, l = map(int, input().split())
answer = solution(n,l)
if answer == -1:
    print(answer)
else:
    print(*answer,sep=' ')