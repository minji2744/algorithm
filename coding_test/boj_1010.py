t = int(input())

def factorial(n):
    d = [0] * (n+1)
    for i in range(n+1):
        if i == 0 or i == 1:
            d[i] = 1
        else:
            d[i] = i * d[i-1]
    return d[n]

def combination(n, r):
    #nCr
    return int(factorial(n) / (factorial(r)*factorial(n-r)))
    
for _ in range(t):
    n, m = map(int,input().split())
    print(combination(m,n))