# 1986. 지그재그 숫자
# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cnt = []
    for i in list(range(1, n + 1)):
        if i %2 == 0:
            cnt.append(-i)
        else:
            cnt.append(i)
    print(f'#{test_case} {sum(cnt)}')