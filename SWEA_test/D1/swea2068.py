import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = map(int, input().split())
    b = 0
    for i in list(a):
        # print(i)
        if i > b:
            b = i
    print(f'#{test_case} {b}')    
    