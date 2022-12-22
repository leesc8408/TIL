# https://www.acmicpc.net/problem/1302

t = int(input())
book_list = {}

for i in range(t):
    book = input()
    if book not in book_list:
        book_list[book] = 1
    else:
        book_list[book] += 1

best_sell = max(book_list.values())

best_book = []
for book, sell in book_list.items():
    if sell == best_sell:
        best_book.append(book)

print(sorted(best_book)[0])
