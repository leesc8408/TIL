# 문제 21. 숫자 뒤집기
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

num = int(input())
ans = 0

while num > 0:
    ans = num%10
    num = num//10
    print(ans, end='')
