# 📕이차원 리스트

### 3. 순회 

1. 이중 for문을 이용한 행 우선 순회

   ```python
   matrix = [
       [1,2,3,4],
       [5,6,7,8],
       [9,0,1,2]
   ]
   
   for i in range(3):		# 행
       for j in range(4):	# 열
           print(matrix[i][j], end=' ')
       print()
   
   # 1 2 3 4 
   # 5 6 7 8 
   # 9 0 1 2
   ```



2. 이중 for문을 이용한 열 우선 순회

   ```python
   matrix = [
       [1,2,3,4],
       [5,6,7,8],
       [9,0,1,2]
   ]
   
   for i in range(4):		# 열
       for j in range(3):	# 행
           print(matrix[j][i], end=' ')
       print()
       
   # 1 5 9 
   # 2 6 0 
   # 3 7 1
   # 4 8 2
   ```



> #### 행 순회와 열 순회를 사용하기 위해서는 이중 for문을 사용하며 
>
> #### 고정 인덱스 값과 반복 인덱스 값을 잘 파악하자!!!!



### 4. 전치 

- 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다. 

  (행 순회를 전치 하면 열 순회가 되는 거라 생각하면 됨 )

### 5. 회전

- 큐브의 면이 회전 하듯 90도, 270도 등으로 회전 시키켜야 하는 경우가 생긴다.

  ```python
  # 왼쪽 90도 회전 예시
  matrix = [
  	[1, 2, 3],
  	[4, 5, 6],
  	[7, 8, 9]
  ]
  
  n = 3
  rotated_matrix = [[0] * n for _ in range(n)]
  # 회전 시킨 값들을 할장할 새로운 2차원 리스트 생성
  for i in range(n):
  	for j in range(n):
  		rotated_matrix[i][j] = matrix[j][n-i-1]
  ```
  
  

