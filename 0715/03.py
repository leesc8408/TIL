with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruit = text.split('\n')

    f_dic = {}
    for i in fruit:
        f_dic[i] = f_dic.get(i, 0) + 1
    # print(f_dic)


with open('03.txt', 'w', encoding='utf-8') as f:
    for key in f_dic:
        f.write(f'{key} {f_dic[key]}\n')
