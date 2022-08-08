from pprint import pprint
import sys

sys.stdin = open("_파리퇴치.txt")

# 행렬값은 n*n 채 m*m
# 행렬 칸 마다 숫자 있고 채에 해당하는 4칸의 숫자 합이 가장 큰 경우 출력
# 5<=n<=15 /  2<=m<=n   /  칸의 숫자<=30

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    # print(n,m)
    pan = [list(map(int, input().split())) for _ in range(n)]
    # pprint(pan)
    max_fly = 0 # 한 번 내리쳐 잡은 최대 파리의 수
    fly = 0     # 한 번 내리쳐 잡은 파리의 수 
    for x in range((n - m) + 1):    
    # x(행)의 인덱스 값은 n(영역)길이에서 m(파리채)의 크기를 뻬고 본인을 인덱스에 포함해야 하므로 +1
        for y in range((n - m) + 1):
            # 여기부터 한 번 내리쳐 잡은 파리 값 계산
            for i in range(m):
                for j in range(m):
                # 좌표 값 기준 파리채 영역으로 2차원리스트 돌며 값을 더 하며 fly값을 계산
                    fly += pan[x + i][y + j]
            if max_fly < fly:
            # fly가 기존 max_fly보다 크면 최대값 수정
                max_fly = fly
                fly = 0
                # fly 초기화
            else:
            # fly가 max_fly보다 작으면 fly 초기화
                fly = 0
        
    print(f'#{test_case} {max_fly}')
