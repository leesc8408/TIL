# https://www.acmicpc.net/problem/14681

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