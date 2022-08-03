# https://www.acmicpc.net/problem/1110

# 0 <= n <= 99 이고 n < 10 이면 두 자리수로 만들기
# 예시 26 => 2+6=8 => 68 => 6+8=14 => 84 => 8+4=12 => 42 => 4+2=6 => 26
# 예시처럼 처음 수와 같아지는 시점이 1싸이클
# n은 몇 싸이클인가??

# 리스트와 문자열로 풀이
n = input()
n_list  =[]
for i in n:
    if int(n) < 10:
        n_list.append('0')
        n_list.append(i)
    else:
        n_list.append(i)
hap = 0
cnt = 0

while True:
    hap = sum(map(int, n_list))
    cnt += 1
    n_list.pop(0)
    if hap < 10:
        n_list.append(str(hap))
    else:
        n_list.append(str(hap)[1])
    if int(n) == int(''.join(n_list)):
        print(cnt)
        break

# 연산식으로 풀이
# n = input()
# if int(n) < 10:
#     n = '0' + n

# n2 = n
# cnt = 0
# while True:
#     hap = int(n2)//10 + int(n2)%10
#     n2 = str(int(n2)%10) + str(hap%10)
#     cnt += 1
#     if n == n2:
#         break
# print(cnt)