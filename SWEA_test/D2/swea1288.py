import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    n = int(input())
    num_list = set()
    k = 0

    while len(num_list) < 10:
        k += 1
        i = k * n
        for s in str(i):
            num_list.add(int(s))
    else:
        print(f'#{test_case} {i}')