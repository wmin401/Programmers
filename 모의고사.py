def solution(answers):
    answer = []
    scores = [0,0,0] 
    pattern1 = range(1,6)
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == pattern1[i%len(pattern1)]: # pattern1 정답과 비교
            scores[0] += 1 # 정답과 일치하면 추가한다.
        if answers[i] == pattern2[i%len(pattern2)]: # pattern2 정답과 비교
            scores[1] += 1
        if answers[i] == pattern3[i%len(pattern3)]: # pattern3 정답과 비교
            scores[2] += 1 

    max_score = max(scores) # 점수중 최고값 산출
    for i in range(len(scores)):
        if scores[i] == max_score: # 각 패턴과 최고값 비교
            answer.append(i+1) # 최고값 위치 
    return answer
