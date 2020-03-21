def solution(s):
    answer = s[(len(s)-1)//2:len(s)//2+1] # 가운데 숫자 보다 1단계 낮은 범위 부터 1단계 높은 범위까지 범위 지정
    return answer
