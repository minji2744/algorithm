# 계수정령을 이용해, 누락된 요소 찾기

def solution(A):
    # write your code in Python 3.6
    count = []
    for _ in range(len(A) + 3):
        count.append(0)
    for i in range(len(A)):
        count[A[i]] += 1
    return count.index(0, 1, len(count))