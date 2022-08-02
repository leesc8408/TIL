from itertools import count
import sys

sys.stdin = open("_최빈수구하기.txt")

#input
T = int(input())
score_ = {}
for i in range(T):       # 반복횟수 지정 / i = 테스트 넘버
    test_no = int(input())
    score_[test_no] = list(map(int, input().split()))
# print(score_.items())    # dict_items([(1, [41, 85, ... 16, 28]), (2, [3, 13, ...
    bin_ = {}
    for j in score_[test_no]:
        if j not in bin_.keys():
            bin_[j] = 1
        else:
            bin_[j] += 1
    # print((bin_.items()))   # dict_items([(41, 15), (85, 6), ...,(50, 7)]) 테스트 넙버별로 {(점수 : 중복횟수), ...} 딕셔너리 생성
    bin = max(bin_.values())    # values값 (중복 횟수) 중 가장 큰수가 최빈수
    score = []
    for k, v in bin_.items():   # 점수와 중복횟수를 꺼내 반복하며
        if bin == v:            # 최빈수와 values값이 같으면  
            score.append(k)     # 해당 key값(점수)를 score에 추가
    print(f'#{test_no} {(max(score))}') #출력양식에 맞춰 출력하며 점수들 중 가장 큰 점수를 출력