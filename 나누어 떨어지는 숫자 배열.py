def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0: # divior로 나눠지는 확인
            answer.append(i) # 나눠지면 anwer 배열에 추가한다.
        
    if len(answer) == 0: # 나눠진 숫자가 없을 경우
        answer.append(-1) # -1 을 추가한다.
        
    answer.sort()
    return answer
