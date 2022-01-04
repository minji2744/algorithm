s = input()
start = s[0]
c0, c1 = 0, 0
if start == '0':
    c0 += 1
    iszero = True
else:
    c1 += 1
    iszero = False

for i in range(1, len(s)):
    if s[i] != start:
        if iszero:
            c1 += 1
            iszero = False
            start = '1'
        else:
            c0 += 1
            iszero = True
            start = '0'

print(min(c0, c1))