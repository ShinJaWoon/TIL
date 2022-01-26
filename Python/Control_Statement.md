# 제어문(Control Statement)

[조건문(Conditional Statement)](#조건문conditional-statement)

[반복문(Loop Statement)](#반복문loop-statement)

## 조건문(Conditional Statement)

### 조건문

>  - 참/거짓을 판단하는 조건식과 함께 사용
>
>  ```python
>  if 조건문:
>      실행문
>  else:
>      실행문
>  ```
>

<br>

### 복수 조건문

> ```python
> if 조건문:
>     실행문
> elif 조건문:
>     실행문
> else:
>     실행문
> ```
>

<br>

### 중첩 조건문

> ```python
> if 조건문:
>     실행문
>     if 조건문:
>         실행문
> elif 조건문:
>     실행문
> else:
>     실행문
> ```
>

<br>

### 조건 표현식

>```python
>if 조건문:
>    실행문1
>else:
>    실행문2
>    
>    
>실행문1 if 조건문 else 실행문2
><true인 경우 값> if 조건식 else <false인 경우 값>
>
>#절댓값을 저장하는 코드
>value = num if num >= 0 else -num
>```
>

<br><br>

## 반복문(Loop Statement)

[Python Tutor](https://pythontutor.com/visualize.html#mode=edit)

### While문

> - 조건문인 참일 경우 코드를 반복해서 실행
> - 무한 루프를 하지 않도록 **종료조건** 필요
>
> ```python
> while 조건문:
>     실행문
> ```
>

<br>

### For문

> - 시퀀스(string, tuple, list, range)를 포함한 iterable 요소를 모두 순회한다.
>
> ```python
> for i in 시퀀스:
>     실행문
> ```
>
> - 딕셔너리(Dictionary)의 경우 key를 순회한다.
>
> ```python
> Dict_name = {'a': 1, 'b': 2}
> Dict_name.keys() 	# key로 구성
> Dict_name.values() 	# values로 구성
> Dict_name.items()	# (key, value) 튜플로 구성
> 					# [('a', 1), ('b', 2)] <- 유사 리스트. 리스트는 아님
> ```
>

<br>

### enumerate 순회

> ```python
> data = [1, 2, 3]
> result = list(enumerate(data))
> #[(0, 1), (1, 2), (2, 3)]
> 
> result = list(enumerate(data), start=1)
> #[(1, 1), (2, 2), (3, 3)]
> ```
>

<br>

### 반복문 제어

#### break

> - 반복문을 멈추고 나감

#### continue

> - continue 다음의 실행문은 무시하고 다시 반복문 시작

#### pass

> - 동작이 없을 때 자리 채우는 용도
> - 반복문 아니라도 사용 가능

#### else

> - 반복문이 끝까지 실행되면 (for문이 전부 순회하면) 실행
> - break로 중단되면 실행되지 않음



