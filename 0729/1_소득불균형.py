import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    humans = int(input())   # 인원수
    moneys = list(map(int, input().split()))    #각 소득을 리스트에 저장
    p_money = sum(moneys) // humans     #평균소득을 각 소득의 총합을 인원수로 나눠 구함
    # print(p_money)
    cnt = 0
    for i in moneys:    # 소득 리스트에서 하나씩 반복
        if i <= p_money: # 평균 소득 이하이면 cnt를 1씩 더함
            cnt += 1
    print(f'#{test_case} {cnt}')