def solution(participant, completion):
    participant.sort() # 참가자 오름차순 정렬
    completion.sort() # 완주자 오름차순 정렬
    
    for i,j in zip(participant,completion): # zip 함수를 사용하여 하나의 묶으로 바꾸고 
        if i != j : # i 와 j 를 비교한다.
            return i
    
    return participant[-1] # i와 j를 비교해서 일치 하지 않을 경우 참가자 마지막 사람을 리턴한다.
