def solution(arr):
    answer = []
    
    for i in arr:
        if [i] == answer[-1:]:
            continue
        answer.append(i)
    
    return answer
