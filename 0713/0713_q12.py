# 주어진 문자열 (apple)가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = 'apple'

for i in word:
    # print(i)
    if i == 'a':
        continue
    print(i,end='')

    

