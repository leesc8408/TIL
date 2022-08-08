import sys

sys.stdin = open("_암호생성기.txt")

t = 10
for i in range(1, t + 1):
    test_case = int(input())
    se_code = list(map(int, input().split()))
    
    while 0 not in se_code:
    # 암호문 리스트에 0이 나올 때까지 반복
        for i in range(1, 6):
        # 1싸이클은 1부터5까지 빼야 해서 
            a = se_code.pop(0)
            # 암호문 리스트에서 [0]번째 값을 반환/삭제
            if (a - i) > 0:
            # 마이너스 계산 후 0보다 크면 
                se_code.append(a - i)
                # 계산 값을 암호문 리스트에 추가(자동 가장 뒤로 됨)
            else:
            # 마이너스 후 0보다 크지 않으면
                se_code.append(0)
                # 리스트에 0을 추가
                break
                # 0이 들어 갔으므로 반복문은 종료
    
    print(f'#{test_case} ', *se_code)    # 출력 