def solution(a, b):
    answer = 0
    
    for i in range(min(a,b),max(a,b)+1): # min(a,b) a, b 중 작은 수, max(a,b) a,b 중 큰 수 로 범위 설정
        answer += i # 범위 내의 숫자를 모두 더한다.
        
    return answer
