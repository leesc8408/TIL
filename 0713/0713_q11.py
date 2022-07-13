# 구구단 출력하기
# 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

for dan in range(2,10):
    print(f'{dan}단')

    for a in range(1,10):
        cnt = a * dan
        print(f'{dan} X {a} = {cnt}')
        
        
