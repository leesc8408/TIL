# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("28_분해합.txt")
#입력
a = int(input())
#연산
for i in range(1, a+1):     # 1부터 입력값 (a)자신까지 반복
    hap = i + sum(map(int, str(i)))     # 반복되는 수를 str로 변환 ->map(int, )로 문자열 각각에 int 변환
                                        # int로 변환되어 맵(리스트)에 모인 값을 합산 후 반복되는 수에 더한다
    if hap == a:    # 더해진 수와 입력값이 같다면 현재 반복되는 수가 생성자 이므로 출력한다.
        print(i)
        break
    if i == a:
        print(0)

        


