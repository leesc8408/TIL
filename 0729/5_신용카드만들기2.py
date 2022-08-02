import sys

sys.stdin = open("_신용카드만들기2.txt")
test =  ''
T = int(input())
for test_case in range(1, T + 1):
    card_no = input().split()
    for i in card_no:
        i = i.replace('-', '')
        if len(i) == 16 and i[0] in '34569':
            print(f'#{test_case} 1')
        else:
            print(f'#{test_case} 0') 