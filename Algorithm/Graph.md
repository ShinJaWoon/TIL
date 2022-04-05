## 최소 신장 트리

###  최소 신장 트리 MST(Minimum Spanning Tree)

> - 무방향 가중치 그래프에서 간선들의 가중치의 합이 최소인 신장 트리

### Prim 알고리즘

> #### 방식
>
> > 1. 임의 정점을 하나 선택
> > 2. 선택한 정점과 인접하는 정점 중에서, 최소 비용의 간선으로 연결된 정점을 선택
> > 3. 모든 정점이 선택될 때까지 1, 2 반복
>
> #### 알고리즘
>
> > ```python
> > def MST_PRIM(r, V):
> >     # r은 시작할 정점, V는 총 정점 개수
> >     MST = [0] * (V + 1)  # MST 포함 여부
> >     key = [10000] * (V + 1)  # 가중치의 최대값으로 초기화
> >     key[r] = 0  # 시작정점 키
> > 
> >     # 간선은 V-1개 이므로, V-1번 반복한다.
> >     for _ in range(V):
> > 
> >         u = 0
> >         minV = 10000
> >         # 인접한 정점들 중에서 최소key를 가진 정점을 찾는다.
> >         for i in range(V + 1):
> >             # MST에 포함이 되지 않고, 인접한 정점이라면
> >             if MST[i] == 0 and key[i] < minV:
> >                 u = i
> >                 minV = key[i]
> >         MST[u] = 1
> >         # u에 인접한 v에 대해, MST에 포함되지 않은 정점이라면
> >         # key 값을 비교하여 더 작은 값을 넣는다. (최소 key를 찾는다.)
> >         for v in range(V + 1):
> >             if MST[v] == 0 and adjM[u][v] > 0:
> >                 key[v] = min(key[v], adjM[u][v])
> >     return sum(key)
> > ```
> >
> > ```python
> > def MST_PRIM(r, V):
> >     # r은 시작할 정점, V는 총 정점 개수
> >     MST = [0] * (V + 1)  # MST 포함 여부
> >     MST[r] = 1
> >     s = 0  # 최소 가중치의 합
> > 
> >     # 간선은 V-1개 이므로, V-1번 반복한다.
> >     for _ in range(V):
> >         u = 0
> >         minV = 10000
> >         # MST에 포함된 정점과 인접한 정점들 중에서 최소key를 가진 정점을 찾는다.
> >         for i in range(V + 1):
> >             if MST[i] == 1:
> >                 for j in range(V + 1):
> >                     # 인접한 정점이고, MST에 없는 정점이라면
> >                     if 0 < adjM[i][j] < minV and MST[v] == 0:
> >                         u = j
> >                         minV = adjM[i][j]
> >         s += minV
> >         MST[u] = 1
> > 
> >     return s
> > ```
> >
> > 

### KRUSKAL 알고리즘

> #### 방식
>
> > 1. 모든 간선을 가중치에 따라 오름차순으로 정렬
> > 2. 가중치가 가장 낮은 간선부터 선택
> > 3. 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
> > 4. n-1개 간선까지 2~3 반복
>
> #### 알고리즘
>
> > ```python
> > def find_set(x):
> >     while x != rep[x]:
> >         x = rep[x]
> >     return x
> > 
> > 
> > def union(x, y):
> >     rep[find_set(y)] = find_set(x)
> > 
> > 
> > V, E = map(int, input().split())
> > edge = []
> > for _ in range(E):
> >     u, v, w = map(int, input().split())
> >     edge.append([w, v, u])
> > 
> > edge.sort()  # 가중치 순으로 오름차순 정렬
> > rep = [i for i in range(V + 1)]  # 대표원소 배열
> > # MST의 간선수 N = 정점 수 - 1
> > N = V - 1
> > cnt = 0  # 선택한 edge 수
> > total = 0  # MST 가중치 합
> > for w, v, u in edge:
> >     if find_set(v) != find_set(u):
> >         cnt += 1
> >         union(u, v)
> >         total += w
> >         if cnt == N - 1:
> >             break
> > 
> > 
> > ```
> >
> > 

## 최단 경로

### Dijkstra 알고리즘

> - 음의 가중치 허용 X
>
> ```python
> # s: 시작 정점, A: 인접 행렬, D: 가중치(거리), V: 정점 집합, U: 선택된 정점 집합
> def Dijkstra(s, A, D):
>     U = [0] * (V+1)
>     U[s] = 1
>     
>     for i in range(V+1):
>         if A[s][i]:
>             D[v] = A[s][i]
>             
>         # else:
>         #     D[v] = INF  # 최댓값
>         
>     for _ in range(V):
>         # V에서 선택되지 않은 정점 중 시작점과 가장 거리가 짧은 정점을 찾는다.
>         min_d = INF
>         w = 0
>         for i in range(V+1):
>             if U[i] == 0 and D[i] and D[i] < min_d:
>                 min_d = D[i]
>                 w = i
>                 break
>         
>         U[w] = 1
>         # w와 연결된 점들의 시작점 s 와의 거리를 갱신한다.
>         for i in range(V+1):
>             if A[w][i] and D[i] > D[w] + A[w][i]:
>                 D[i] = D[w] + A[w][i]
>                 
>             if 0 < A[w][i] < INF:
>                 D[i] = min(D[i], D[w]+A[w][i])
>                 
>         
> ```
>
> 
>
> 



### Bellman-Ford 알고리즘

> - 음의 가중치 허용



### Floyd-Warshall 알고리즘

> - 모든 정점들에 대한 최단 경로