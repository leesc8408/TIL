# https://www.acmicpc.net/problem/1157
a = list(map(ord, input()))    #  list(input(). upper()) 를 사용하면 7열까지의 코드를 줄일수 있음

for i in range(len(a)):
    if (a[i] + 32) > 128:
        a[i] = a[i] - 32
A = list(map(chr, a))
char =[]
cnt = []
for i in A:                     # 문자열 A의 첫 자리 i
    if i not in char:           # 문자 리스트에 i가 없으면 
        char.append(i)          # char에 i 추가
        cnt.append(A.count(i))  # 카운트 리스트에는 A에 있는 i 의 개수 추가
# 위의 단계를 거치면 char와 cnt는 같은 인덱스 배열을 가진 리스트가 됨
if cnt.count(max(cnt)) > 1:     # cnt 리스트에 가장 많은 문자의 개수가 중복 된다면 ? 출력
    print('?')  
else:                           # 중복이 없다면 cnt리스트에 개수의 max값의 인덱스 값을 char의 인덱스 값으로 해서 출력 
    print(char[cnt.index(max(cnt))])
