from dataclasses import replace
import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for test_case in range(1, T + 1):
    char = input()
    char_rev = char[::-1]   # 입력된 문자를 인덱스 역순으로 나열
    # print(char_rev)
    out = []
    for i in char_rev:  # 문자열을 한글자씩 반복
        # if와 elif로 비교하여 replace로 변환하여 out 리스트에 추가
        if i == 'b':
            out.append(i.replace('b', 'd')) 
        elif i == 'd':
            out.append(i.replace('d', 'b'))
        elif i == 'p':
            out.append(i.replace('p', 'q'))
        elif i == 'q':
            out.append(i.replace('q', 'p'))
    rev_ = ''.join(out) # out리스트에는 한글자씩 나뉘어 저장되어 있으므로 join을 써서 하나의 문자열로 변환
    print(f'#{test_case} {rev_}')