# ๐ฉ๋์๋๋ฆฌ

## ๐ํด์ ํ์ด๋ธ

- ํ์ด์ฌ์๋ ๋์๋๋ฆฌ(dict) ์๋ฃ๊ตฌ์กฐ๊ฐ ๋ด์ฅ๋์ด ์๋ค.

  - key : value ๊ตฌ์กฐ์ด๋ฉฐ key๋ immutableํ๊ณ  uniqueํ๊ฒ,  value๋ mutable์ด๋ค.
- ํด์ ํจ์ : ์์ ๊ธธ์ด์ ๋ฐ์ดํฐ๋ฅผ ๊ณ ์  ๊ธธ์ด์ ๋ฐ์ดํฐ๋ก ๋งคํํ๋ ํจ์

  - ํด์ : ํด์ ํจ์๋ฅผ ํตํด ์ป์ด์ง ๊ฐ


> #### ํ์ด์ฌ์ ๋์๋๋ฆฌ๋ ํด์ ํจ์์ ํด์ ํ์ด๋ธ์ ์ด์ฉํ์ฌ ์ฐ์ฐ์ ์๋๊ฐ ๋ฆฌ์คํธ๋ณด๋ค ๋น ๋ฅด๋ค.

- ๋์๋ฆฌ์ ์ฌ์ฉ์?

  - ๋ฆฌ์คํธ๋ฅผ ์ฌ์ฉํ๊ธฐ ํ๋ ๊ฒฝ์ฐ

  - ๋ฐ์ดํฐ์ ๋ํ ๋น ๋ฅธ ์ ๊ทผ ํ์์ด ํ์ํ ๊ฒฝ์ฐ

  - ํ์ค ์ธ๊ณ์ ๋๋ถ๋ถ์ ๋ฐ์ดํฐ๋ฅผ ๋ค๋ฃฐ ๊ฒฝ์ฐ



## ๐๋์๋๋ฆฌ ๊ธฐ๋ณธ ๋ฌธ๋ฒ

1. ์ ์ธ
   - ๋ณ์ = {key1 : value1), (key2 : value2), ...}    # ๋์๋๋ฆฌ๋ฅผ ์์ฑ

2. ์ฝ์ / ์์ 
   - dict[key] = value     # ๋ด๋ถ์ key๊ฐ ์์ผ๋ฉด key : value ์ฝ์ ์์ผ๋ฉด value ์์  

3. ์ญ์ 

   - dict.pop(key)    # ๋ด๋ถ์ key์ ์๋ value ๋ฐํ ํ ์ญ์ (key์์ผ๋ฉด Error๋ฐ์)

   - dict.pop(key : default)    # ๋ด๋ถ์ key๊ฐ ์์ ์ Error๊ฐ ์๋ default๋ฅผ ๋ฐํ.

4. ์กฐํ

   - dict[key]    # ๋ด๋ถ์ key๊ฐ ์์ผ๋ฉด keyError

   - dict.get(key, default)    # ๋ด๋ถ์ key๊ฐ ์์ผ๋ฉด  value๊ฐ์ผ๋ก None ๋ฐํ, default ์๋ ฅ ์ default๋ฅผ ๋ฐํ


```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
    
}

a['job'] = 'coach'
print(a)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul', 'job': 'coach'}

a['name'] = 'justin'
print(a)
# {'name': 'justin', 'gender': 'male', 'address': 'Seoul'}

gender = a.pop('gender')
print(a)
print(gender)
# {'name': 'justin', 'address': 'Seoul'}
# male

phone = a.pop('phone')
print(a)
print(phone)
# KeyError: 'phone'

phone = a.pop('phone', 'Not phone')
print(a)
print(phone)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
# Not phone

print(a['name'])
# kyle

print(a['phone'])
print(a.get('phone', '์๋ค๊ตฌ์'))
# KeyError: 'phone'
# ์๋ค๊ตฌ์
```





## ๐๋์๋๋ฆฌ ๋ฉ์๋

1. dict.keys()
   - ๋์๋๋ฆฌ์ key ๋ชฉ๋ก์ด ๋ด๊ธด dict_keys ๊ฐ์ฒด ๋ฐํ
2. dict.values()
   - ๋์๋๋ฆฌ์ value ๋ชฉ๋ก์ด ๋ด๊ธด dict_values ๊ฐ์ฒด ๋ฐํ
3. dict.items()
   - ๋์๋๋ฆฌ์ (key, value) ์ ๋ชฉ๋ก์ด ๋ด๊ธด dict_items ๊ฐ์ฒด ๋ฐํ

```python
a = {
    'name' : 'kyle',
    'gender' : 'male',
    'address' : 'Seoul'
    
}

print(a.keys())
# dict_keys(['name', 'gender', 'address'])
print(a.values())
# dict_values(['kyle', 'male', 'Seoul'])
print(a.items())
# dict_items([('name', 'kyle'), ('gender', 'male'), ('address', 'Seoul')])

```



