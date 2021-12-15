import math
t = int(input())
def solution(x1, y1, x2, y2, circles):
    answer = 0
    for c in circles:
        cx, cy, r = c
        d1 = math.sqrt((x1-cx)**2+(y1-cy)**2)
        d2 = math.sqrt((x2-cx)**2+(y2-cy)**2)
        if d1 < r and d2 > r:
            answer += 1
        if d1 > r and d2 < r:
            answer += 1
    return answer


for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    circles = [list(map(int, input().split())) for _ in range(n)]
    print(solution(x1, y1, x2, y2, circles))