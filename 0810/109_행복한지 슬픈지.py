# https://www.acmicpc.net/problem/10769

import sys
sys.stdin = open('_행복한지 슬픈지.txt')

mms = input()
# print(mms)
happy = mms.count(':-)')
sad = mms.count(':-(')
# print(happy, sad)
if happy == 0 and sad == 0:
    print('none')
else:
    if happy > sad:
        print('happy')
    elif happy < sad:
        print('sad')
    elif happy == sad:
        print('unsure')
