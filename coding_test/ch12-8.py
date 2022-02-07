s = input()
answer = []
value = 0
for x in s:
    if x.isdecimal():
        value += int(x)
    else:
        answer.append(x)
answer.sort()

# 이 부분을 빼먹어서 정답 보고 수정했습니다.
if value != 0:
    answer.append(str(value))

print(''.join(answer))