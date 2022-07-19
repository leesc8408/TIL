import sys
sys.stdin = open("input.txt", "r")

# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
# 각 수는 1이상 10000이하의 정수이다.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    ans1 = a //b
    ans2 = a %b
    print(f'#{test_case} {ans1} {ans2}')

# 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 
# 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.
