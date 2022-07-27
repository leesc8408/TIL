# 🚩문자열

### 1. 문자열 슬라이싱

- 문자열은 순서대로 나열된 immutable 자료

- s[ 부터: 까지: 방향] 식으로 사용되며 입력값은 인덱스를 사용

  - 인덱스는 0부터 세고 역순으로 사용 가능하나 -0은 없다. -1부터 역순 

  |       | a    | b    | c    | d    | e    | f    | g    | h    | i    |
  | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | index | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
  | index | -9   | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |

  ```python
  word = 'abcdefghi'
  
  word[2:5]		# cde
  word[-5:-2]		# efg
  word[2:5:1]		# cde
  word[2:5:-1]	# 출력 없음 (2부터 역방향으로 5까지이므로 표시할 수없음)
  word[5:2:-1]	# fed
  ```

  

### 2. 문자열 메소드

1. split('기준문자')
   - 문자열을 일정 기준으로 나누어 리스트로 변환(기본은 공백)
2. strip('제거문자')
   - 문자열의 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환(기본은 공백)
3. find('찾을문자')
   - 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환(없다면 -1 반환 후 진행)
4. index('찾을문자')
   - 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환(없다면 오류 후 멈춤)
5. count('개수 셀 문자')
   - 문자열에서 특정 문자의 개수를 세서 반환
6. replace('기존문자', '새로운문자')
   - 문자열에서 기존 문자를 새로운 문자로 수정한 새로운 문자열 반환
7. '삽입문자'.join(iterable)
   - iterable의 각 원소 사이에 삽입문자를 삽입한 새로운 문자열로 반환



### 3. 아스키(ASCII) 코드 (미국 정보교환 표준부호)

- 처음으로 숫자를 알파벳으로 표현하기 시작
- 알파벳을 표현하는 대표 인코딩 방식(8bit 중 1bit는 에러 검출용 7bit는 문자 정보 저장(총128개))

1. ord('문자')
   - 문자를 해당 아스키코드 번호로 반환
2. chr(번호)
   - 번호를 해당 아스키코드 문자로 반환
