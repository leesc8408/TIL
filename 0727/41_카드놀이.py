# https://www.acmicpc.net/problem/2511



A_cards = list(map(int, input().split()))
B_cards = list(map(int, input().split()))
A_cnt = 0
B_cnt = 0
vic_list = []

for i in range(10):
    if A_cards[i] > B_cards[i]:
        A_cnt += 3
        vic_list.append('A')
    elif A_cards[i] < B_cards[i]:
        B_cnt += 3
        vic_list.append('B')
    else:
        A_cnt += 1
        B_cnt += 1
        vic_list.append('D')
print(A_cnt, B_cnt, sep=' ')
if A_cnt > B_cnt:
    print('A')
elif A_cnt < B_cnt:
    print('B')
elif A_cnt == B_cnt:
    if len(set(vic_list)) == 1:
        print(*set(vic_list))
    else:
        for j in vic_list[::-1]:
            if j == 'D':
                continue
            else:
                print(j)
                break
