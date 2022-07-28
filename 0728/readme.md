# 🚩딕셔너리

## 📕해시 테이블

- 파이썬에는 딕셔너리(dict) 자료구조가 내장되어 있다.

  - key : value 구조이며 key는 immutable하고 unique하게,  value는 mutable이다.
- 해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

  - 해시 : 해시 함수를 통해 얻어진 값


> #### 파이썬의 딕셔너리는 해시 함수와 해시 테이블을 이용하여 연산의 속도가 리스트보다 빠르다.

- 딕셔리의 사용은?

  - 리스트를 사용하기 힘든경우

  - 데이터에 대한 빠른 접근 탐색이 필요한 경우

  - 현실 세계의 대부분의 데이터를 다룰 경우



## 📗딕셔너리 기본 문법

1. 선언
   - 변수 = {key1 : value1), (key2 : value2), ...}    # 딕셔너리를 생성

2. 삽입 / 수정
   - dict[key] = value     # 내부에 key가 없으면 key : value 삽입 있으면 value 수정 

3. 삭제

   - dict.pop(key)    # 내부에 key에 있는 value 반환 후 삭제(key없으면 Error발생)

   - dict.pop(key : default)    # 내부에 key가 없을 시 Error가 아닌 default를 반환.

4. 조회

   - dict[key]    # 내부에 key가 없으면 keyError

   - dict.get(key, default)    # 내부에 key가 없으면  value값으로 None 반환, default 입력 시 default를 반환


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
print(a.get('phone', '없다구요'))
# KeyError: 'phone'
# 없다구요
```





## 📘딕셔너리 메소드

1. dict.keys()
   - 딕셔너리의 key 목록이 담긴 dict_keys 객체 반환
2. dict.values()
   - 딕셔너리의 value 목록이 담긴 dict_values 객체 반환
3. dict.items()
   - 딕셔너리의 (key, value) 쌍 목록이 담긴 dict_items 객체 반환

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



