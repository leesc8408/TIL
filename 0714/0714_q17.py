# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

# 문제 17. 소문자-대문자 변환하기
word = 'apple'
W = ord('a') - ord('A')
for i in word:
    out = ord(i) - W
    print(chr(out), end='')