l, r = input().split()
def solution(l,r):
    count = 0
    if '8' not in l:
        return count
    else:
        if len(l) < len(r):
            return count
        else:
            if l == r:
                return l.count('8')
            before = True
            for i in range(len(l)):
                if before and l[i] == r[i]:
                    if l[i] == '8':
                        count += 1
                else: before = False
            return count
print(solution(l,r))