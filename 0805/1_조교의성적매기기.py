import sys

sys.stdin = open("_조교의성적매기기.txt")

# A+ A0 A- B+ B0 B- C+ C0 C- D0 평가 개수 10개  
# 100 = m_score(35%) + e_score(45%) + h_work(20%)
# 학생수 10<= n <= 100이고 10배수
# 확인학생번호 1<= k <= n
# 1줄:test_case / 2줄:n k / ~줄:m_score e_score h_work
# 출력:#test_case 학점

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    score_dic = {}
    alpha_score = {}
    alpha_ = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(1, n + 1):
        m_score, e_score, h_work = map(int, input().split())
        score_dic[i] = round((m_score*0.35)+(e_score*0.45)+(h_work*0.2))
        # 딕셔너리로 1번부터 생성 value값은 점수들을 소수점까지 곱하고 마지막에 round함수로 실수가 아닌 정수로 
    # print(score_dic)
    k_score = score_dic[k]
    # 딕셔너리 키캆에 찾고자하는 학생 번호 입력하여 점수를 불러옴
    # print(k_score)
    all_score = list(score_dic.values())
    # 딕셔너리 점수들을 모두 리스트로 만듬
    all_score.sort(reverse=True)
    # 점수들을 내림차순으로 정렬하여 고득점이 1등이 되도록
    cnt = all_score.index(k_score)
    # 점수 리스트에서 찾고자하는 점수의 인덱스를 반환 받으면 전체에서 석차가 됨 
    # !!주의 1등=[0],2등=[1],3등=[2],...인덱스 값 [0]이 1등이다.
    # print(cnt)
    no = cnt // (n//10)
    # 한 학점당 학생수는 총인원/10으로 전체 석차에서 학점당 배당 인원을 나누면 정답 
    # print(no)
    print(f'#{test_case} {alpha_[no]}')