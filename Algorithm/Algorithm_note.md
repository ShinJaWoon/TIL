```python
# 버블 정렬
# ====================================================================
""" 
인접한 두 수를 비교하여 큰 수를 맨 뒤로 보낸다.
한 번 루프가 돌면 맨 끝에 가장 큰 수가 가게 된다.
첫 번째 for문이 한 번 돌 때마다 맨 뒤에 정렬되는 숫자가 하나씩 늘어나므로
두 번째 for문에서는 첫 번째 for 문이 돈 수만큼 돌지 않아도 된다.
첫 번째 루프는 리스트 길이 만큼 돌기 위함
두 번째 루프는 비교하며 바꾸기 위함
"""

def Bubble_Sort(a, N):	# a: 정렬할 List, N: 리스트의 길이
    for i in range(N-1):	
        for j in range(N-1 - i):
            if a[j] > a[j+1]: # 왼쪽이 더 크면 오른쪽과 교환. 오름차순
                a[j], a[j+1] = a[j+1], a[j]
    return

# 오른쪽부터 비교하는 방식
def Bubble_Sort(a, N):	# a: 정렬할 List, N: 리스트의 길이
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return
                
# -------------------------------------------------------------------

# 카운팅 정렬
# ======================================================================
"""
1. Data의 각 정수 항목 x들의 발생 회수(count)를 센다.
2. 카운트를 각 정수 항목 x가 인덱스가 되는 배열 counts에 새로 저장한다.
3. 누적된 카운트를 저장한다.
4. Data의 정수 항목 x에 하나씩 접근하여 누적 카운트 개수를 찾는다.
5. 누적 카운트를 1 감소 시킨다.
6. 누적 카운트를 인덱스로 갖는 새로운 정렬된 배열에 x를 저장한다.
"""

def Counting_Sort(A):
    # A [] -- 정렬할 배열
    # B [] -- 정렬된 배열
    # C [] -- count 배열
    
    k = max(A)
    B = [0] * len(A)
    C = [0] * (k+1)
    
    for a in A:
        C[a] += 1
    # 아래와 같다.
    # for i in range(0, len(A)):
    #	C[A[i]] += 1
       
    for i in range(1, len(C)):
        C[i] += C[i-1]
   
    
    for i in range(len(B)-1, -1, -1):
    	C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    # 위는 stable sort 아래는 unstable sort
    # 중복된 값들의 순서가 그대로 => stable
    # for a in A:
    #     C[a] -= 1
    #     B[C[a]] = a
    # 또는
    # for i in range(len(B)):
        # C[A[i]] -= 1
        # B[C[A[i]]] = A[i]
        
    return B

# ----------------------------------
def Counting_Sort(A):
    k = max(A)
    B = [0] * len(A)
    C = [0] * (k+1)
    
    for a in A:
        C[a] += 1
        
    for i in range(1, len(C)):
        C[i] += C[i-1]
        
    for a in A:
        C[a] -= 1
        B[C[a]] = a
        
    return B
# -------------------------------------------------------------------


# 선택 정렬
# ======================================================================
"""
남은 리스트에서 최솟값을 찾아 남은 리스트의 맨 앞으로 보낸다.
"""

def selectionSort(a, N):
  # 0 ~ N-1까지. N번째는 혼자 남으므로 정렬할 필요가 없다.
  for i in range(N-1):
      # 리스트의 시작점
      min_idx = i
      for j in range(i+1, N):
          # 최솟값의 인덱스를 찾는다.
          if a[min_idx] > a[j]:
              min_idx = j
      # 최솟값을 시작점과 교환
      a[i], a[min_idx] = a[min_idx], a[i]
-------------------------------------------------------------------

# 퀵 정렬 ==================================================================
def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end) # 파티션 함수를 통해 정렬시켜 고정된 위치들을 받는다.
        quickSort(a, begin, p-1) # 고정된 위치를 제외하고 퀵정렬을 다시 한다.
        quickSort(a, p+1, end)

def partition (a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        # L은 왼쪽에서 피벗보다 큰 값을 찾을 때까지 오른쪽으로 이동
        while(L<R and a[L] < a[pivot]):
            L += 1
        # R은 오른쪽에서 피벗보다 작은 값을 찾을 때까지 왼쪽으로 이동
        while(L<R and a[R] >= a[pivot]):
            R -= 1
        if L < R:
            if L == pivot: # 왼쪽영역에 피벗보다 큰 값이 없을 때
                pivot = R	# 피벗을 다시 지정
                a[L], a[R] = a[R], a[L]
    # L과 R이 만났을 경우, 피벗과 위치를 바꾸고 위치를 고정시킨다. 
    # 만났으므로 a[R] = a[L]
    a[pivot], a[R] = a[R], a[pivot]
    # 고정된 위치를 반환
    return R


# 다른 방법
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    # 오름차순
    # left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    # right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분
    
    # 내림차순
    left_side = [x for x in tail if x > pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x <= pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# ---------------------------------------------------------------




# =========================================================================
# KMP 패턴 서칭

def lps_maker(pattern, len_p):
    table = [0] * (len_p+1)  
    # 패턴을 찾는 중 다른 값이 나왔을 때 다시 비교를 시작할 idx를 저장한다.
    # 접두사가 겹쳐서 불필요한 서칭을 방지
    # ABCDABCE
    #-100001230
    # E 에서 틀릴 경우 text가 D인지 확인해야 한다. ( E 앞에 ABC가 있으므로)
    # E의 인덱스 7을 lps에 넣으면 lps[7] = 3 --> D의 인덱스
    
    # -1을 넣는 이유: lps[0]이 들어왔을 때 i와 j는 동시에 +1을 하게 하기 위함
    # text = OPQRSTUVWXYZ이고 pattern이 ABCDABCE인 경우
    # O와 A가 다르면 j = lps[j] <= j = lps[0] = -1 이 되고 i와 j는 +1이 되지 않는다.
    # 다시 j가 -1이 되면 i+1 j+1 이 되어 j=0(A), i=1(P)
    # i와 j가 동시에 +1이 되기 때문에 패턴에서 찾는 위치를 0부터 시작하기 위해 -1이 들어간다.
    j = 0
    i = 1
    table[0] = -1
    for i in range(1, len_p):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j]
            # AAAADAAAAAAE
            # 0123456789
            #-1012301234440
            # j=8에서 틀리면 table[8]=4, j=4(D)부터 다시 검사하면 된다.
            # j=8에서 앞에 AAA가 있기 때문에 AAAD에서 AAA는 검사할 필요가 없는 것.

        if pattern[i] == pattern[j]:
            j += 1
            table[i+1] = j # 틀릴 경우 패턴에서 어디부터 검사해야 불필요한 부분이 없는가?를 넣는곳

    return table


T = 10
for tc in range(1, T+1):
    tc_n = int(input())
    pattern = input()
    text = input()
    len_pattern = len(pattern)
    len_text = len(text)

    lps = lps_maker(pattern, len_pattern)
    i = 0   # text idx
    j = 0   # pattern idx
    count = 0  # pattern count
    find_index = []
    while i < len_text and j <= len_pattern: # and j <= len_pattern은 없어도 될것 같음
        if j == -1 or text[i] == pattern[j]: 
        # 패턴이 다르고 -1이 아니라면 발동 안됨
        # 패턴과 비교를 시작한 이후에 패턴이 다르면 발동이 안된다는 얘기
        # 패턴 비교를 시작할 때, 그리고 패턴이 일치하고 있을 때만 발동
        # j = 0이고 패턴이 다르면 else에서 j = -1이 되고 다시 여기로 와서 i+1 j+1
        # 패턴검사를 다시 시작할 때 j=0에서 시작하는 것이 아니라 j가 -1이 되었다가 0이되면서 시작한다고 생각하면 됨
            i += 1
            j += 1
        else: 
        # 패턴이 다를 때 돌아갈 곳. j가 0이 되면 다시 -1로 만들어 주는 역할도 함
            j = lps[j]
        if j == len_pattern:
            count += 1
            find_index.append(i-len_pattern)
            j = lps[j]
# ----------------------------------------------
# lps를 1칸 안늘리는 방식
def lps_maker(pattern, len_p):
    table = [0] * (len_p)
    j = 0
    i = 1
    table[0] = -1
    for i in range(1, len_p):
        table[i] = j
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j]

        if pattern[i] == pattern[j]:
            j += 1
            
    return table
```

```python
# 문제풀이 꿀팁


# 리스트 출력
print(*arr) # 요소를 하나씩 띄어서 출력

# 2차원 리스트 받기
N = int(input()) # 열 개수
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 리스트 지그재그
for i in range(m):
    for j in range(n):
        arr[i][j + (n-1 - 2*j)*(i%2)]
        
	
# 부분 집합
n = len(arr)

for i in range(1<<n): # 공집합 포함
    for j in range(n):
        if i & (1<<j):
            print(arr[j, end = ", "])
        print()
    print()
    
# &: 비트 and 연산
# |: 비트 or 연산
# a << b: a의 비트 열을 왼쪽으로 b 만큼 (2^b) 만큼 곱
# a >> b: a의 비트 열을 오른쪽으로 b 만큼 (2^b) 만큼 나눔


# 백트래킹
def f(i, N, s, t):  # s는 현재 상태(ex: 합), t는 기준
    if i == N:
        pass
        # 결과 출력
    elif s < t # 중간에 break를 걸 조건
    	pass
    else:
        # 여기에 재귀를 돌리기 전 변화를 주고
        f(i+1, N, s + alpha, t)
        # 다시 변화를 돌린다.
```

```python
# 트리

# 이중 트리
V = int(input())  # 정점의 개수
E = V - 1		# 간선의 갯수
arr = list(map(int, input().split()))

# 자식 노드
ch1 = [0] * (1 + V)
ch2 = [0] * (1 + V)
# 부모 노드
par = [0] * (1 + V)

for i in range(E):
    # 아래 i*2와 같은 인덱싱은 이진 트리에서만 사용 가능
    p = arr[i*2]
    c = arr[i*2 +1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

# 전위 순회
def pre_order(v):
    # 자식이 있다면. ch[v] 가 0일 경우를 제외하기 위함
    if v:
        print(v, end=' ')
        pre_order(ch1[v])
        pre_order(ch2[v])

# 중위 순회
def in_order(v):
    if v:
        in_order(ch1[v])
        print(v, end=' ')
        in_order(ch2[v])

# 후위 순회
def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v, end=' ')

pre_order(1)
print()
in_order(1)
print()
post_order(1)
print()

# 조상을 찾아보는 코드
def find_ancestor(c):
    while par[c] != 0:
        print(c)
        c = par[c]
    return c


# 완전 이진트리가 아닐 경우 root를 찾는다.
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i

root = find_root(V)
pre_order(root)




```

