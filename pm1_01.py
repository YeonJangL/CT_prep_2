def gcd(w, h):
    if w < h:
        short = w
        long = h
    else:
        short = h
        long = w
        
    # y�� 0�� �� ������ �ݺ�
    while long:
        # long ��  short �� ����
        # short �� long ���� ���� �������� long �� ����
        short, long = long, short % long
    return short

def solution(w,h):
    answer = 1
    origin_count = w * h
    # �밢�������� �߸� �簢���� ���� ���ϴ� ����
    answer = origin_count - (w + h - gcd(w,h))
    return answer

w, h = map(int, input().split())
print(solution(w,h))