def solution(array, commands):
    answer = []
    
    for command in commands:
        new_array = array[command[0]-1:command[1]] # i 부터 j 범위까지 숫자
        new_array.sort() #  정렬
        answer.append(new_array[command[2]-1]) # #k번째 숫자
    return answer
