def solution(n, lost, reserve):
    answer = 0
    clothes = [1]*(n+2)
    clothes[0] = 0
    clothes[n+1] = 0
    
    for i in lost:
        clothes[i] = clothes[i] - 1
    
    for i in reserve:
        clothes[i] += 1
        
    for i in range(1,len(clothes)-1):
        if clothes[i] == 1 or clothes[i] == 2:
            clothes[i] = clothes[i] - 1
            answer += 1
        else:
            if clothes[i-1] == 1:
                clothes[i-1] = clothes[i-1] - 1
                answer += 1
            elif clothes[i+1] == 2:
                clothes[i+1] = clothes[i+1] - 1
                answer += 1
    return answer
