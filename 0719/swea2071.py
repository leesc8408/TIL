# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    hap = sum(num_list) / len(num_list)
    print(f'#{test_case} {round(hap)}')
    