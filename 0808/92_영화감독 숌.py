# https://www.acmicpc.net/problem/1436

from pprint import pprint


t = int(input())
hell = '666'
movie = {}

for i in range(0, 200):
    if i < 6:
        movie[i] = int(str(i) + hell)
# print(movie.items())
    elif 6 <= i < 16:
        j = i + 4 - 10
        j = str(j)
        movie[i] = (hell + j[0])
    elif 16 <= i:
        j = i + 4 - 10
        j = str(j)
        movie[i] = (j[0] + hell + j[1])

pprint(movie.items())
