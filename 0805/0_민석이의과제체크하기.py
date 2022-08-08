import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    pass_list = list(map(int, input().split()))
    out = set(range(1, n+1)) - set(pass_list)
    # range를 이용 1번,n번까지 있는 셋을 만들고 제출자 리스트를 셋으로 하여 차집합을 하면
    # 제출하지 않은 번호들만이 남으며 set의 성질상 오름차순임
    
    print(f'#{test_case}', *out)