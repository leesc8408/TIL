from posixpath import split


with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruit = text.split('\n')

    fruits = []
    for li in fruit:
        if li.endswith('berry'):
            fruits.append(li)
    
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(set(fruits))}\n')
    for i in set(fruits):
        f.write(f'{i}\n')