import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    # 사작형이라 두면씩 수가 같으므로 if로 기준a와 b,c 를 한번씩 비교
    if a == b:  # a와 b가 같으면 c 출력
        print(f'#{test_case} {c}')
    elif a == c:    # a와 c가 같으면 b 출력
        print(f'#{test_case} {b}')
    else:   # a가 b,c와 같지 않다면 a가 다른수 이므로 출력
        print(f'#{test_case} {a}')