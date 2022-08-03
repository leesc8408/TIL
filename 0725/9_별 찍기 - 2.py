# https://www.acmicpc.net/problem/2439

n = int(input())

for i in range(n):
    star = '*' * (i + 1)    
    gong = ' ' * (n - len(star))    #입력값에서 *개수를 뺀만큼 공백을 넣어 출력값 인덱스가 5가 되도록 맞춤
    print(f'{gong}{star}')