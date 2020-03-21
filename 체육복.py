def solution(n, lost, reserve):
    answer = 0
    clothes = [1]*(n+2) # 모든 학생이 체육복 1개가 있다고 가정한다.
    clothes[0] = 0 # 인덱스 0 은 체육복 0개로 바꿔준다.
    clothes[n+1] = 0 # 마지막 인덱스도 체육복 0개로 바꿔준다.
    
    for i in lost:
        clothes[i] = clothes[i] - 1 # clothes 배열에 체육복을 잊어버린 학생 번호에서 체육복을 제거한다
    
    for i in reserve:
        clothes[i] += 1 # 체육복을 추가로 가져온 학생 번호에 체육복을 추가한다.
        
    for i in range(1,len(clothes)-1):
        if clothes[i] == 1 or clothes[i] == 2: # 체육복을 1개 또는 2개 가진 조건에 일치한다면
            clothes[i] = clothes[i] - 1 # 체육복을 1개를 제거하고
            answer += 1 # 체육수업에 들을 수 있는 인원에 추가한다.
        else:
            if clothes[i-1] == 1: # 체육복이 없는 경우 앞에 학생이 체육복 1개를 가지고 있다면,
                clothes[i-1] = clothes[i-1] - 1 # 체육복 1개를 제거하고
                answer += 1 # 참가자 인원에 추가한다.
            elif clothes[i+1] == 2: # 뒤에 학생이 체육복 2개를 가지고 있다면,
                clothes[i+1] = clothes[i+1] - 1 # 체육복 1개를 제거하고
                answer += 1 # 참가자 인원에 추가한다.
    return answer
