# 🖥프로젝트4(모의고사)

- 델타 탐색

  - 기준 좌표를 두고 상하좌우,대각선 등 주변을 탐색하는 법

    |         | [2 , 1]             |         |
    | ------- | ------------------- | ------- |
    | [1 , 0] | 기준[x = 1 , y = 1] | [1 , 2] |
    |         | [0 , 1]             |         |

    

  ```python
  delta_x = [1, -1, 0, 0]    # 상하좌우 x값 차이를 리스트로 만듬
  delta_y = [0, 0, 1, -1]    # 상하좌우 y값 차이를 리스트로 만듬
  x, y = 1, 1
  for d in range(4):
      quest_x = x + delta_x[d]
      quest_y = y + delta_y[d]
      print(quest_x, quest_y)
    
  # 예시(8방향)
  
  delta_x = [-1, 0, 1, -1, 1, -1, 0, 1]
  delta_y = [-1, -1, -1, 0, 0, 1, 1, 1]
  
  x, y = 1, 1
  for d in range(8):
      quest_x = x + delta_x[d]
      quest_y = y + delta_y[d]
    
  ```

  
