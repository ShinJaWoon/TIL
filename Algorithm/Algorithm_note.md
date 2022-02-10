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
                
# ======================================================================

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
# ======================================================================

```

```python
# 문제풀이 꿀팁


# 리스트 출력
print(*arr) # 요소를 하나씩 띄어서 출력
```

