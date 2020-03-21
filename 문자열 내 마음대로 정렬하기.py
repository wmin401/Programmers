def solution(strings, n):
    answer = sorted(sorted(strings), key = lambda x: x[n]) # strings 배열을 오름차 순으로 먼저 정리하고, 
    return answer # 또 한 번 정렬하는데 lambda 함수를 이용해 n 자리수 기준으로 오름차 정렬 하게끔 한다.
