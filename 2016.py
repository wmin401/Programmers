import datetime # datetime 라이브러리 호출

def solution(a, b):
    day_of_the_week = ['MON','TUE','WED','THU','FRI','SAT','SUN']  # 날짜 리스트
    answer = day_of_the_week[datetime.datetime(2016,a,b).weekday()] # weakday() 함수 사용 (화요일은 1을 반환함)
    return answer
