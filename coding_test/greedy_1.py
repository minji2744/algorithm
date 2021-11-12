import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
m1 = l[n-1]
m2 = l[n-2]

print((m1*k+m2)*(m//(k+1)) + m1*(m%(k+1)))