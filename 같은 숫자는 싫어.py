def solution(arr):
    answer = []
    
    for i in arr:
        if [i] == answer[-1:]: # 가장 최근 더해진 숫자와 비교
            continue # 위의 논리식이 True 이면 다시 위로
        answer.append(i) # 가장 최근 더해진 숫자와 비교가 False 라면 answer 배열에 추가한다.
    
    return answer
