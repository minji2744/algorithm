def nonDivisibleSubset(k, s):
    # Write your code here
    cnt = [0]*k
    for x in s:
        cnt[x%k] += 1
    answer = 0
    answer += min(cnt[0], 1)
    for i in range(1, (k+1)//2):
        answer += max(cnt[i], cnt[k-i])
    if k % 2 == 0:
        answer += min(cnt[k//2], 1)
    return answer