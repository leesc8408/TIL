# 🚩데이터 구조

타입.메서드() - 타입의 무언가를 조작해준다. 

객체의 풀이로 생각하자면  - 문자열 너 이거해(메서드)라고 생각해도 됨

타입.함수 - 입력값을 두고 함수의 지시대로 반환

타입.메서드 - 입력값을 메서드의 지시대로 반환

---

- ### 시퀀스 (순서가 있는 데이터 구조)

  - 문자열(string)

    - 탐색

      .find(x) : x의 첫 번째 위치를 반환. 없으면 -1을 반환함.

      .index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생.

    - 검증

      .is<코드>입력 후 각 검증코드에 따라 검증 가능

      ```python
      rint('abc'.isalpha())	#is를 이용하여 alpha를 검증
      # True
      print('Ab'.isupper())	#대문자 검증
      # False
      ```

    - 변경

      .replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자도 바꿔서 반환

      ​								count 지정 시 해당 횟수 만큼만 바꿈

      ```python
      print('wooooowoo'.replace('o', '!', 2))
      # w!!ooowoo
      ```

      .strip() : 특정 문자들을 지정하면 양쪽제거(strip), 좌측제거(lstrip), 우측제거(rstrip)

      ​						대체로 양쪽의 공백 제거 시 많이 사용

      ```python
      print(' 와우!\n'.strip())
      # '와우!'
      ```

      .split : 문자열을 특정한 단위로 나눠 리스트로 반환

      ```python
      print('a!1!b!2!c'.split('!')) # !를 기준으로 나눔
      # ['a', '1', 'b', '2', 'c']
      print('a b c'.split())	# 기본은 공백
      # ['a', 'b', 'c']
      ```

      .'n'.join([iterable]) : 반복 가능한 컨테이너 요소들을 구분자('n')로 합쳐 문자열 반환

      ```python
      print(''.join(['3', '5’]))
      # 35
      ```

      기타 변경

      ```python
      msg = 'hI! Everyone.'
      print(msg)
      print(msg.capitalize())
      print(msg.title())
      print(msg.upper())
      print(msg.lower())
      print(msg.swapcase())
      
      # hI! Everyone.
      # Hi! everyone.
      # Hi! Everyone.
      # HI! EVERYONE.
      # hi! everyone.
      # Hi! eVERYONE.

  - 리스트(list)

    변경 가능한 값들의 나열된 자료형

    순서를 가지고 변경 가능, 반복 가능, 항상 대괄호[] 형태로 정의하며, 요소는 콤마로구분

    - 추가 / 삭제

      .append(x) : 리스트에 값을 추가함

      .pop(i)  :  지정된 i 위치에 값을 삭제하고 해당 항목 반환<미지정 시 마지막 항목 삭제>

      ```python
      numbers = ['hi', 1, 2, 3]
      # ['hi', 1, 2, 3]
      pop_number = numbers.pop()
      print(pop_number)
      # 3
      print(numbers)
      # ['hi', 1, 2]
      ```

       .extend(iterable) : 리스트에 iterable의 항목을 추가함

       .insert(i, x) : 정해진 위치 i에 값을 추가함

      .remove(x) : 리스트에서 값이 x인 것 삭제

    - 탐색 / 정렬

      .index(x) : x값을 찾아 해당 index 값을 반환

      .count(x) : 값의 개수를 반환함

      ```python
      numbers = [1, 2, 3, 1, 1]
      print(numbers.count(1))
      # 3
      print(numbers.count(100))
      # 0
      ```

       .sort() :  원본 리스트를 정렬함.   sorted 함수와는 반환 값 다름

---

- ### 컬렉션 (순서가 없는 데이터 구조)

  - 세트(set)

    유일한 값들의 모음으로 변경 가능하며 반복 가능함.

    순서가 없고 **중복된 값이 없음**

  - 딕셔너리(dictionary)

    키(key)-값(value) 쌍으로 이뤄진 모음, 변경 가능하며 반복 가능함

    키와 값은 : 로 구분되며 개별 요소는 , 로 구분된다.

    ```python
    students = {'홍길동': 30, '김철수': 25}
    students['홍길동']
    # 30 
    ```

    - 조회

      .get(key[,default]) : key를 통해 value를 가져옴

      > KeyError가 발생하지 않음. 기본 None. 
      >
      > 오류가 필요한 경우가 있음을 기억할 것!!!!

      ```python
      my_dict = {'apple': '사과', 'banana': '바나나'}
      print(my_dict.get('pineapple'))
      # None
      print(my_dict.get('apple'))
      # 사과
      ```

    - 추가 / 삭제

      .pop(key[,default]) :  key가 딕셔너리에 있으면 제거하고 해당 값을 반환

      .update([other]) : 값을 제공하는 key, value로 덮어씁니다.

