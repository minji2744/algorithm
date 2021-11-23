def solution(data):
    priority = [1,2,4,3,6,7,5]
    weather = [0,20,20,17,10]
    rain = [0,5,14]
    scores, answer = [], []
    
    for info in data:
        score = 20 - abs(22-info[2])
        if info[1] > 0:
            score += rain[info[1]]
            scores.append(score)
            continue
        scores.append(score + weather[info[0]])
    
    max_i, min_i = 0,0
    for i, a in enumerate(scores):
        if a > scores[max_i]:
            max_i = i
        if a == scores[max_i]:
            if priority[i] > priority[max_i]:
                max_i = i
        if a < scores[min_i]:
            min_i = i
        if a == scores[min_i]:
            if priority[i] < priority[min_i]:
                min_i = i
                
    answer.append(max_i)
    if data[min_i][0] == 4 or data[min_i][1] == 1 or \
    data[min_i][2] >= 30 or data[min_i][2] <= 0:
        answer.append(min_i)
    else:
        answer.append(-1)
        
    return answer