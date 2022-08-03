# https://www.acmicpc.net/problem/10995

n = int(input())
# *을 입력값만큼 리스트에 반복
list1 = ['*'] * n
# 사이에 공백을 넣어 join하여 문자열로 변환
list2 = ' '.join(list1)
# 입력값을 for문의 반복 range값으로
for i in range(n):
# 반복값 i%2로 나머지 0 이면 열은 훌수열 *문자열 출력 
    if i % 2 == 0:
        print(list2)
# 반복값 i%2로 나머지 1 이면 열은 짝수열 *문자열 앞에 공백을 넣고 출력 
    elif i % 2 == 1:
        print(f' {list2}')