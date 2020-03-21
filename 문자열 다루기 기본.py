def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True: # 문자열 길이가 4 or 6 인지 비교하고, isdigit() 함수를 사용하여 숫자로만 되어있는지 확인한다.
        answer = True
    else:
        answer = False
    return answer
