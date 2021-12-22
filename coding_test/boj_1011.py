t = int(input())

def move(x,y):
    l = []
    k = 0
    for i in range(50000):
        k += i
        l.append(k*2)
        l.append(k*2+i+1)
    for i, m in enumerate(l):
        if y-x <= m:
            return i

for _ in range(t):
    x, y = map(int, input().split())
    print(move(x,y))