# ๐ฉํ์ด์ฌ ํ์ค ๋ผ์ด๋ธ๋ฌ๋ฆฌ

- ํ์ด์ฌ์์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ค์น๋ ๋ชจ๋๊ณผ ๋ด์ฅ ํจ์์ ๋ชจ์

---

## - ๋ชจ๋

- ํธ๋ฆฌํ ํจ์๋ฅผ ๊ฐ ํ๋ก๊ทธ๋จ์ ์ ์๋ฅผ ๋ณต์ฌํ์ง ์๊ณ ,

  ์ฌ์ฉํ  ์ ์๋๋ก ์ ์๋ฅผ ํ์ผ์ ๋ฃ์ด์ ์ฌ์ฉํ๋ ๋ฐฉ๋ฒ

#### - ์ฌ์ฉ ์์

```python
import datetime

now = datetime.datetime.now()
print(now, type(now))

# 2022-07-18 22:32:11.855348 <class 'datetime.datetime'>
```

```python
import random

numbers = random.sample(range(1, 46), 6)
numbers.sort()
print(numbers, type(numbers))

# [8, 11, 19, 32, 34, 42] <class 'list'>
```

---

## - ํ์ผ ์ฝ๊ณ  ์ฐ๊ธฐ

- Open (ํ์ผ ์ด๊ธฐ)
  - ๋ชจ๋
    - `'r'` : read (์ฝ๊ธฐ ์ ์ฉ), **๊ธฐ์กด ํ์ผ์ ์ฝ์ด์ด**.
    - `'w'` : write (์ฐ๊ธฐ ์ ์ฉ - ๋ฎ์ด์), **์๋ก ํ์ผ์ ์์ฑํ์ฌ ๊ธฐ๋กํจ**.
    - `'a'` : append (์ฐ๋๋ฐ ํ์ผ ์์ผ๋ฉด ์ด์ด์ ์), **๊ธฐ์กด ํ์ผ์ ์ด์ด์ ๊ธฐ๋กํจ**.

```python
with open('test.txt', 'w', encoding='utf-8') as f:
	#open('๊ฒฝ๋ก/ํ์ผ๋ช', '๋ชจ๋', '์ธ์ฝ๋ฉ')
    
    f.write('Happy Hacking!\n')
    for i in range(1, 6):
        f.write(f'{i} ๋ฒ์งธ!\n')
```

---

## - json ์ฌ์ฉ

- ๋ฌธ์์ด๋ก ์ด๋ฃจ์ด์ง ํ์์ ํฌ๋งท

```python
import json 
from pprint import pprint

	# ํ์ผ์ ์ด๊ณ , 
f = open('stocks.json', 'r', encoding='utf-8')
# JSON์ ํ์ด์ฌ ๊ฐ์ฒด(kospi) ํ์์ผ๋ก ํ๋ค!
kospi = json.load(f)
samsung = kospi['stocks'][0]
# print(samsung, type(samsung))

# stockName ์ ๋ณด๋, closePrice ์ ๋ณด๋ง ๊ฐ์ง ๋์๋๋ฆฌ๋ฅผ ๋ง๋ค๊ณ  ์ถ์ด์!
result = {
    'stockName': samsung.get('stockName'),
    'closePrice': samsung.get('closePrice')
}

print(result)
```

