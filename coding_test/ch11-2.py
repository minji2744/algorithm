l = [int(i) for i in input()]
answer = l[0]
for i in range(1, len(l)):
    if answer <= 1 or l[i] <= 1:
        answer += l[i]
    else:
        answer *= l[i]
print(answer)