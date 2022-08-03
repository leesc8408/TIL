# https://www.acmicpc.net/problem/1065

n = int(input())
cnt = 0

for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    # 한 자리 수는 연속수가 없으므로 일정하다고 보며, 두 자리수는 두 수의 차이가 1개이라 일정하다고 봄.
    # 그러므로 100미만의 수는 모두 한수에 포함된다.
    if i < 100: 
        cnt += 1
    # 세 자리 수부터 [0], [1], [2] 각 자리수의 차이를 비교하여 같을 경우만 한수
    elif n_list[0] - n_list[1] == n_list [1] - n_list[2]:
        cnt += 1
print(cnt)