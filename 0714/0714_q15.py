# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# 문제 15. 문자의 위치 구하기
word = 'apple'
cnt = 0
for i in word:
    if i == 'a':
       print(cnt)
       break
    else:
        cnt += 1
else:
    print(-1)

# upgrade

word1 = 'pineapple'
print(word1.find('a'))