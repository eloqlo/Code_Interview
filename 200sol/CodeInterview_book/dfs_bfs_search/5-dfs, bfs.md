# 꼭 필요한 자료구조 기초

## Search (탐색)
- 많은 양의 데이터에서 원하는 데이터를 찾는 과정

## Data Structure (자료구조)
- 데이터를 표현하고 관리하고 처리하기 위한 구조

## Recursive Fucntion (재귀 함수)
- 자기자신을 다시 호출하는 함수
- 언제 끝날지, 종료 조건에 대한 명시가 꼭 필요.
    > 종료하는 법 : return 해주면, 나머지 함수들에서 주르륵 실행되며 나올 수 있다.

# Graph
- Node(Vertex), Edge 로 이루어진 구조
## 표현방식
1. Adjacency Matrix : 2차원 배열로 그래프 연결관계를 표현   -->  Speed good
2. Adjacency List : 리스트로 그래프의 연결 관계를 표현      -->  Memory good

# DFS/BFS
## DFS
- 그래프에서 깊은 부분을 우선으로 탐색하는 알고리즘
- O(N)
## BFS
- 그래프에서 얕은 부분을 우선으로 탐색하는 알고리즘
- 일반적으로 DFS보다 수행시간 낫다.
- O(N)