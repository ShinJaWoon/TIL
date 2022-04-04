# 분할 정복과 백 트래킹

## 분할 정복(Divide and Conquer)

### 분할 정복

> - 크기 n인 문제의 해를 n/2 크기의 문제들의 해를 이용해 푸는 방식

### 병합 정렬(Merge Sort)

> - 여러 개의 정렬된 자료를 병합하여 한 개의 정렬된 집합으로 만드는 정렬방식
> - 분할정복 알고리즘을 사용한다.
> - top-down 방식
> - O(n logn)
>
> #### 분할과정
>
> > ```python
> > def merge_sort(arr):
> >        if len(arr) == 1:
> >            return arr
> >     
> >        middle = len(arr) // 2
> >        left = merge_sort(arr[:middle])
> >        right = merge_sort(arr[middle:])
> >     
> >        return merge(left, right)
> > ```
>
> #### 병합과정
>
> > ```python
> > def merge(left, right):
> >     result = []
> > 
> >     while len(left) > 0 or len(right) > 0:
> >         if len(left) > 0 and len(right) > 0:
> >             if left[0] <= right[0]:
> >                 result.append(left.pop(0))
> >             else:
> >                 result.append(right.pop(0))
> >         elif len(left) > 0:
> >             result.append(left.pop(0))
> >         elif len(right) > 0:
> >             result.append(right.pop(0))
> >     return result
> > ```
> >
> > ```python
> > """
> > 위 코드보다 pop 과정이 없어 더 빠르다.
> > """
> > def merge(left, right):
> > 
> >     result = []
> >     l = r = 0
> >     while l < len(left) and r < len(right):
> >         if left[l] <= right[r]:
> >             result.append(left[l])
> >             l += 1
> >         else:
> >             result.append(right[r])
> >             r += 1
> >     result += left[l:]
> >     result += right[r:]
> > 
> >     return result
> > ```
> >
> > 

### 퀵 정렬

> - 병합정렬은 절반으로 분할하지만, 퀵 정렬은 분할할 때 pivot 이라는 기준을 중심으로 작은 것은 왼쪽, 큰 것은 오른쪽에 위치시킨다.
> - 각 분할 후 병합을 필요로 하지 않음
>
> #### 알고리즘
>
> > ```python
> > def quick_sort(arr, l, r):
> >     if l < r:
> >         s = partition(arr, l, r)
> >         quick_sort(arr, l, s - 1)
> >         quick_sort(arr, s + 1, r)
> > ```
> >
> > ```python
> > # Hoare-Partition 알고리즘
> > def partition(arr, l, r):
> >     p = arr[l]
> >     i = l
> >     j = r
> >     while i <= j:
> >         while i <= j and arr[i] <= p:
> >             i += 1
> >         while i <= j and arr[j] >= p:
> >             j -= 1
> >         if i < j:
> >             arr[i], arr[j] = arr[j], arr[i]
> >     arr[l], arr[j] = arr[j], arr[l]
> >     return j
> > 
> > ```
> >
> > ```python
> > # Lomuto partition 알고리즘
> > # r이 pivot으로 작동
> > def partition(arr, l, r):
> >     p = arr[r]
> >     i = l - 1
> > 
> >     for j in range(l, r):
> >         if arr[j] <= p:
> >             i += 1
> >             arr[i], arr[j] = arr[j], arr[i]
> >     arr[i + 1], arr[r] = arr[r], arr[i + 1]
> >     return i + 1
> > 
> > ```
> >
> > 

### 이진 검색(Binary Search)

> ```python
> # 반복
> def binary_search(n, arr, key):
>        low = 0
>        high = n - 1
>     
>        while low <= high:
>            mid = low + (high - low) // 2
>         
>            if arr[mid] == key:
>                return mid
>            elif arr[mid] > key:
>                high = mid - 1
>            else:
>                low = mid + 1
>        return -1
> ```
>
> ```python
> def binary_search(arr, low, high, key):
>        if low > high:
>            return -1
>        else:
>            mid = (low + high) // 2
>            if key == arr[mid]:
>                return mid
>            elif key < arr[mid]:
>                return binary_search(arr, low, mid -1, key)
>            else:
>                return binary_search(arr, mid + 1, high, key)
> ```
>
> 



## 백트래킹

### 백트래킹

> - DFS에서 가지치기(prunning)를 통해 시도의 횟수를 줄인다.
> - 최악의 경우에는 지수함수 시간을 요할 수 있음



## 트리

### 힙의 추가 삭제

> ```python
> def enq(n):
>     global last
>     last += 1
>     tree[last] = n  # 완전 이진트리
>     c = last	# 새로 추가된 정점
>     p = c // 2  # 새로 추가된 정점의 부모 정점
>     # 부모가 있고, 자식이 부모보다 크면 교환
>     while p >= 1 and tree[p] < tree[c]:
>         tree[p], tree[c] = tree[c], tree[p]
>         c = p
>         p = c // 2
> ```
>
> ```python
> def deq():
>     global last
>     tmp = tree[1] #  루트 값
>     tree[1] = tree[last]  # 마지막 정점 값을 루트에 저장
>     last -= 1 # 마지막 정점 삭제
>     
>     p = 1	# 루트
>     c = p * 2  # 왼쪽자식
>     # 왼쪽 자식이 있으면
>     while c <= last:
>         # 오른쪽 자식이 있고, 오른쪽 자식이 더 크면
>         if c+1 <= last and tree[c] < tree[c+1]:
>             c += 1  # 오른쪽 자식과 교환 (더 큰쪽이 위로 올라오게 됨)
>         if tree[p] < tree[c]:
>             tree[p], tree[c] = tree[c], tree[p]
>             p = c
>             c = p*2
>         else:
>             break
>    return tmp
> ```
>
> 