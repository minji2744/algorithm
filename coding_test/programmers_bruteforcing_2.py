'''
내 풀이
'''
def solution(numbers):
    # 리스트에서 순열 가져오기
    from itertools import permutations
    
    # 소수인지 판별하는 함수
    def prime(n):
        if n == 0 or n == 1:
            return False
        if n == 2 or n == 3 or n == 5 or n == 7:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    answer = 0
    candidates = []
    numbers = [x for x in numbers]
    
    # 가능한 숫자 조합 찾기
    for i in range(1,len(numbers)+1):
        for it in list(permutations(numbers,i)):
            i = int(''.join(it))
            candidates.append(i)
    
    # 소수의 개수 세기
    for num in set(candidates):
        if prime(num) == True:
            answer += 1
            
    return answer


'''
다른 풀이 - 에라토스테네스 체의 활용
'''
from itertools import permutations
def sol(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0,2))
    for i in range(2, int(max(a)**0.5) + 1):
        a -= set(range(i*2, max(a)+1, i))
    return len(a)
