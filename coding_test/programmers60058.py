def check(string):
    start = string[0]
    c1 = 1
    c2 = 0
    for i in range(1, len(string)):
        if start == string[i]:
            c1 += 1
        else:
            c2 += 1
        if c1 == c2:
            return string[:c1+c2], string[c1+c2:]

def correct(string):
    if string[0] == '(':
        return True
    else:
        return False

def solution(p):
    if len(p) == 0:
        return ''
    else:
        u, v = check(p)
        if correct(u):
            return u + solution(v)
        else:
            answer = '(' + solution(v) + ')'
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    answer = answer + ')'
                else:
                    answer = answer + '('
            return answer