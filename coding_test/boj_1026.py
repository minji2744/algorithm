n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = 0

a = sorted(a, reverse=False)
b = sorted(b, reverse=True)
for idx, num in enumerate(b):
    s1 += num*a[idx]
print(s1)