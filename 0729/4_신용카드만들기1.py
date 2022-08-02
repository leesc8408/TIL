import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_ = list(map(int, input().split()))
    # print(card_)
    cnt = []
    for i in range(len(card_)): # 인덱스 수는 0부터 시작이라 홀짝을 반대로 홀은  + , 짝은 *2로 설정
        if i % 2 == 0:
            cnt.append(card_[i] * 2)
        else:
            cnt.append(card_[i])
    n = sum(cnt) % 10   # 자리 수별로 계산 값을 모은 cnt를 합하여 10으로 나눈 나머지가 1의 자리수
    if n == 0:  # 0일경우 그대로 출력
        print(f'#{test_case} {n}')
    else:   # 0이 아니면 10으로 만들기 위한 수를 구하도록 (10 - n)을 하여 출력 
        print(f'#{test_case} {10-n}')