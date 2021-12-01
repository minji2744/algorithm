from collections import deque
import math
n, m = map(int, input().split())
order = list(map(lambda x : int(x)-1, input().split()))
q = [i for i in range(n)]
q = deque(q)

count = 0
i = 0
while i < m:
    if order[i] == q[0]:
        q.popleft()
        i += 1
        continue
    left = False
    for k in range(math.ceil(len(q)/2)):
        if order[i] == q[k]:
            left = True
    if left:
        a = q.popleft()
        q.append(a)
        count += 1
        continue
    a = q.pop()
    q.appendleft(a)
    count += 1
print(count)