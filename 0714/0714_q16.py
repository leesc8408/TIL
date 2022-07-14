# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

# 문제 16. 모음 등장 여부 확인하기
word = 'apple'
cnt = 0
for i in word:
    if i == 'a':
       cnt += 1
    elif i == 'e':
        cnt += 1
    elif i == 'i':
        cnt += 1
    elif i == 'o':
        cnt += 1
    elif i == 'u':
        cnt += 1
print(cnt)
   
