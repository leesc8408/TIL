# 📕깊이 우선 탐색(DFS)

### 1. 그래프 탐색 알고리즘

- 시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘
- 그래프 탐색 알고리즘에는 깊이우선탐색(DFS)과 너비우선탐색(BFS)이 있다.
  - 깊이우선탐색 (Depth-First Search) : 그래프의 깊이를 우선으로 탐색하기 위해 **스택의 개념**을 활용
  - 너비우선탐색 (Breadth-First Search) : 그래프의 너비를 우선으로 탐색하기 위해 **큐의 개념**을 활용

### 2. 깊이 우선 탐색(DFS)

- **시작 정점**으로부터 갈 수 있는 **하위 정점**까지 가장 깊게 **탐색**,

  더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색,

  모든 **정점을 방문**하는 순회 방법

- 장점

  - 모든 정점을 방문할 때 유리하다. (경우의 수, 순열과 조합 문제에서 많이 사용)
  - 너비우선탐색(BFS)에 비해 코드 구현이 간단하다.

- 단점

  - 모든 정점을 방문할 필요가 없거나 

    최단 거리를 구하는 경우에는 너비우선탐색(BFS) 이 유리하다.

### 3. DFS의 동작 과정

1. 탐색을 진행할 그래프가 필요하다.

   - 그래프는 **인접 행렬** 혹은 **인접 리스트** 방식 가능

2. 각 정점을 방문했는지 여부를 판별할 방문 체크 리스트가 필요하다.

   - visited 리스트를 따로 선언하여 각 정점을 방문했는지 체크

   ```python
   visited = [False] * 7	# 정점이 7개일 경우 (True, False 외에 다른 값 사용 가능)
   [False, False, False, False, False, False, False] # 리스트의 인덱스가 정점이 된다.
   ```

### 4. DFS의 구현 방식

```python
graph = [
    [1, 2],
    [0, 3, 4],
    [0, 4, 5],
    [1],
    [1, 2, 6],
    [2],
    [4]
]

visited = [False] * n # 방문 처리 리스트 만들기

def dfs(start):
	stack = [start] # 돌아갈 곳을 기록
	visited[start] = True # 시작 정점 방문 처리
	
    while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    	cur = stack.pop() # 현재 방문 정점(후입선출)
    	
        for adj in graph[cur]: # 인접한 모든 정점에 대해
            if not visited[adj]: # 아직 방문하지 않았다면
                visited[adj] = True # 방문 처리
                stack.append(adj) # 스택에 넣기
                
dfs(0) # 0번 정점에서 시작

#def 사용하지 않으려면 정점 시작 값을 변수에 할당해주면 된다

start = 0 # 0번 정점에서 시작
stack = [start]	# 돌아갈 곳을 기록 
visited[start] = True	# 시작 정점 방문 처리

while stack:	# 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    cur = stack.pop() # 현재 방문 정점(후입선출)
    
    for adj in graph[cur]: # 인접한 모든 정점에 대해
        if not visited[adj]: # 아직 방문하지 않았다면
            visited[adj] = True # 방문 처리
            stack.append(adj) # 스택에 넣기
```


