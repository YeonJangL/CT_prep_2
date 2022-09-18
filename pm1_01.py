def gcd(w, h):
    if w < h:
        short = w
        long = h
    else:
        short = h
        long = w
        
    # y가 0이 될 때까지 반복
    while long:
        # long 을  short 에 대입
        # short 를 long 으로 나눈 나머지를 long 에 대입
        short, long = long, short % long
    return short

def solution(w,h):
    answer = 1
    origin_count = w * h
    # 대각선에의해 잘린 사각형의 개수 구하는 공식
    answer = origin_count - (w + h - gcd(w,h))
    return answer

w, h = map(int, input().split())
print(solution(w,h))