# 내 풀이
def solution(progresses, speeds):
    answer = []
    days = [(100-p)/z if p%z == 0 else ((100-p)//z+1) for p, z in zip(progresses, speeds)]

    start = days[0]
    a = 0
    for p in days:
        if p <= start:
            a+=1
        else:
            answer.append(a)
            a = 1
            start = p
    answer.append(a)

    return answer

# 다른 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]