# https://www.acmicpc.net/problem/14681
# 1면 (+,+) 2면(-,+) 3면(-,-) 4면(+,-)

x = '+' if int(input()) > 0 else '-'
y = '+' if int(input()) > 0 else '-'

if (x, y) == ('+','+'):
    print(1) 
elif (x, y) == ('-','+'):
    print(2) 
elif (x, y) == ('-','-'):
    print(3) 
elif (x, y) == ('+','-'):
    print(4) 