# Tree

## Tree

### 트리

> - 비선형
> - 원소들 간 1:n 관계를 가지는 자료 구조
> - 원소들 간 계층 구조
>
> #### 정의
>
> > - 최상위 노드 : 루트(root)
> > - 나머지 노드들은 다시 각각의 트리가 되어 부트리 (subtree)라고 함
> > - 차수
> >   - 노드의 차수: 노드에 연결된 자식 노드의 수
> >   - 트리의 차수: 트리의 노드 차수 중 가장 높은 값
> >   - 리프 노드: 노드 차수가 0인 맨 끝의 노드
> > - 높이: 레벨, 계층의 단계







## 이진 트리

### 이진 트리

> - 모든 노드들이 2개의 서브트리를 갖는 트리
> - 각 노드가 자식 노드를 최대 2개 가지는 트리
> - 각 자식 노드들을 왼쪽 자식노드, 오른쪽 자식 노드로 구별
>
> #### 포화 이진 트리 (Full Binary Tree)
>
> > - 모든 레벨에 노드가 포화상태인 이진 트리
> > - 높이가 h 일때, 최대 노드드 개수는 2^(h+1) - 1
>
> #### 완전 이진 트리 (Complete Binary Tree)
>
> > - 포화 이진 트리의 노드번호 1번 부터 n번까지 빈 자리가 없는 이진 트리
>
> #### 편향 이진 트리 (Skewed Binary Tree)
>
> > - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 트리



### 이진트리 - 순회(traversal)

> - 전위 순회(preorder traversal) : VLR 
>
>   - 부모노드 방문, 자식 노드를 좌, 우 순서로 방문
>
>   ```python
>   def preorder(T):
>       if T:
>           visit(T)	#
>           preorder(T.left)
>           preorder(T.right)
>   ```
>
> - 중위 순회(inoder traversal) : LVR
>
>   - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순
>   - 가장 왼쪽 밑 자식노드부터 시작하게 됨
>
>   ```python
>   def inorder(T):
>       if T:
>           inorder(T.left)
>           visit(T)
>           inorder(T.right)
>   ```
>
> - 후위 순회(postorder traversal) : LRV
>
>   - 왼쪽 자식, 오른쪽 자식, 부모노드 순
>   - 아래에서 채우면서 시작하게됨
>
>   ```python
>   def postorder(T):
>       if T:
>           postorder(T.left)
>           postorder(T.right)
>           visit(T)
>   ```
>
>   



### 이진트리 표현 - 배열

> - 루트의 번호 1, 레벨 0
> - 레벨 n의 노드에 대해 2^n 부터 2^(n+1) -1 까지 번호 부여
>
> #### 성질
>
> > - 노드번호 i의 부모 노드 번호 : i // 2
> > - 노드번호 i의 왼쪽 자식 노드 : 2*i
> > - 노드번호 i의 오른쪽 자식 노드 : 2*i + 1
> > - 레벨 n의 시작 노드: 2^n
> > - 

### 이진 탐색

> ```python
> def bin_search(A, k):
>     l = 0
>     r = len(A) - 1
> 
>     while l <= r:
>         m = (l + r) // 2
> 
>         if A[m] == k:
>             return True
>         # 왼쪽
>         elif A[m] > k:
>             r = m - 1
> 
>         # 오른쪽
>         elif A[m] < k:
>             l = m + 1
> 
>     return False
> ```
>
> 