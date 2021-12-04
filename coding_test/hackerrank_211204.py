def solution(stockPrices, k):
    # Write your code here
    count = 0
    answer = 0
    for i in range(len(stockPrices)-1):
        if stockPrices[i+1]-stockPrices[i] > 0:
            count += 1
        else:
            if count >= k - 1:
                answer += count - k + 2
            count = 0
    if count >= k - 1:
        answer += count - k + 2      
    return answer