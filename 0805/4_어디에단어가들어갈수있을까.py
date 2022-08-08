import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(n)]

    word_space = 0
    # k길이의 단어가 들어갈 수 있는 자리의 수

    for x in range(n):
        cnt1 = 0
        cnt2 = 0
        # 가로와 세로의 빈칸 카운트는 따로 사용
        for y in range(n):
        # 가로,세로가 같아서 for문 하나에서 반복
        # 위에 카운트를 2개 놓은 이유 이기도 함
            # (0,0),(0,1),(0,2),(0,3),...으로 진행 가로줄 확인
            if pan[x][y] == 1:
                cnt1 += 1
            elif pan[x][y] == 0:
                if cnt1 == k:
                    word_space +=1
                cnt1 = 0
            # (0,0),(1,0),(2,0),(3,0),... 세로줄 확인
            if pan[y][x] == 1:
                cnt2 += 1
            elif pan[y][x] == 0:
                if cnt2 == k:
                    word_space +=1
                cnt2 = 0
            # y가 행렬마지막 인덱스와 같으면 현재 기록된 cnt를 확인하여 k길이가 되는지 확인
            if y == n-1:
                if cnt1 == k:
                    word_space += 1
                else:
                    cnt1 = 0
                if cnt2 == k:
                    word_space += 1
                else:
                    cnt2 = 0
                
    print(f'#{test_case} {word_space}')