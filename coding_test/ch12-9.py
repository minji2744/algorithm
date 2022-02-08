#프로그래머스 문자열 압축
def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1
    for i1 in range(1, int(len(s)//2+1)):
        l = []
        index, cnt = 0, 1
        l.append(s[index:index+i1])
        index += i1
        while index < len(s):
            n = s[index:index+i1]
            if l[-1] == n:
                cnt += 1
            else:
                if cnt > 1:
                    l.append(str(cnt))
                cnt = 1
                l.append(n)
            index += i1
        if cnt > 1:
            l.append(str(cnt))
        answer = min(answer,len(''.join(l))) 
    return answer