n = int(input())
a = list(map(int, input().split()))
a_set = set(a)
p = [0]*n
count = 0
while a_set:
    min_num = min(a_set)
    for i in range(n):
        if a[i] == min_num:
            p[i] = count
            count += 1
    a_set.remove(min_num)
print(*p,sep=' ')