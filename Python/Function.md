# 함수

- Abstraction : 복잡한 내용을 모르더라도(블랙박스) 사용가능하도록 하는 것
- 재사용성 / 가독성 / 생산성

[함수 기초](#함수-기초)

[함수의 결과값(Output)](#함수의-결과값output)

[함수의 입력(Input)](#함수의-입력input)

[함수의 범위(Scope)](#함수의-범위scope)

[함수의 문서화(Doc-string)](#함수의-문서화doc-string)

[함수 응용](#함수-응용)



## 함수 기초

### 함수의 정의

- 함수(Function) 

  - 특정 기능을 하는 코드 조각, 코드 묶음
  - 특정 명령을 수행하는 코드를 필요시 호출하여 간편히 사용
  - 매번 다시 작성하는 번거로움 제거

- 사용자 함수(Custom Function)

  ```python
  def function_name(parameter):
      # code block
      return returning_value
  ```

### 선언과 호출(define & call)

- 선언: `def` 키워드
- 호출: `함수명()`



## 함수의 결과값(Output)

### 값에 따른 함수의 종류

- void function
  - return 값이 없는 경우
  - None 반환
- Value returning function
  - return 값이 있는 경우
  - return 뒤에 값이 여러 개일 경우 튜플로 묶어서 반환
- return 을 통해 함수를 빠져나갈 수 있다.



## 함수의 입력(Input)

### Parameter와 Argument

- Parameter: 함수를 선언하고 실행할 때, 함수 내부에서 사용되는 식별자
- Argument: 함수를 호출 할 때 넣어주는 값

### Argument

- func_name(argument)
- 함수를 호출하면 parameter를 통해 전달되는 값
  - 필수 Argument: 반드시 전달되어야 함
  - 선택 Argument: 값을 전달하지 않아도 되는 경우. 기본값이 전달된다.

#### Positional Argument

```python
def func(x, y):
    return x - y

print(func(1, 2))	# -1
print(func(2, 1))	# 1
```

#### Keyword Argument

- parameter = value 형태로 argument를 넣는다.
- 선언할 때 사용한 parameter명을 쓰지 않으면 오류가 난다.

```python
def func(x, y):
    return x + y

print(func(1, 2))
print(func(y=2, x=1))
print(func(x=1, 2))
print(func(1, y=2))

# Error! 키워드를 쓰면 위치를 조심해야 한다.
# 아래의 코드는 작동하지 않음
print(func(1, x=2))		
```

#### Default Arguments Values

```python
def func(x, y=0):
    return x + y

print(func(2)) 	# y는 입력을 하지 않아도 0이 들어감
```

### 정해지지 않은 여러 개의 Arguments

#### Positional Arguments Packing/Unpacking

```python
def func(*x):
    return sum(x)

print(func(1, 2, 3))
```

#### Keyword Arguments Packing/Unpacking

```python
def func(**x):
    print(x)
        
func(a='one', b='two', c='three')
# 딕셔너리로 묶여 처리된다.
# {'a':'one', 'b':'two', 'c':'three'}

# 다음 아래의 코드들은 오류가 난다.
# func() 안에 들어갈 것들은 def func() 안에 키워드로 선언하는 것과 같기 때문.
func('a'='one', 'b'='two', 'c'='three')        
func(1='one', 2='two', 3='three')
```

#### 주의사항

- 기본값을 지닌 argument다음에 기본값이 없는 argument 순서가 올 수 없음

```python
def func(x=0, y): 	# SyntaxError
```



## 함수의 범위(Scope)

### 함수의 범위(Scope)

- 함수는 코드 내부에 **local scope**를 생성

  그 외 공간은 **global scope**

- scope

  - global scope: 코드 어디서든 참조 가능
  - local scope: 함수 내부에서만 참조 가능

- variable

  - built-in scope variable
    - 파이썬이 실행된 이후부터 영원히 유지
  - global variable
    - global scope에 정의된 변수
    - 모듈이 호출된 시점 이후, 혹은 인터프리터가 끝날 때까지 유지
  - local variable
    - local scope에 정의된 변수
    - 함수가 호출될 때 생성, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)

- 파이썬 식별자 이름은 namespace에 저장된다.
- LEGB Rule - 아래 순서로 이름을 찾아나간다.
  - **L**ocal scope : 함수
  - **E**nclosed scope: 특정 함수의 상위 함수
  - **G**lobal scope: 함수 밖의 변수, Import 모듈
  - **B**uilt-in scope: 파이썬 안에 내장된 함수 또는 속성

- 함수 내에서는 바깥 Scope의 변수에 **접근 가능**, **수정 불가**

### global문

- 현재 코드 블록 전체에 적용
- 함수 내부에서 외부 변수를 수정시킬 수 있다.
- global은 코드 최상단에 위치시키며, global 앞에 같은 변수 이름을 사용하지 않는다.
- global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등에 사용하지 않는다.

```python
a = 1
def func():
    a = 3		# global 앞에 위치하면 안됨
    global a

a = 1
def func(a):	# global이 parameter나 함수 정의에 사용되면 안됨
    global a
```

### nonlocal

- Enclosed scope(가장 가까운 namespace) 연결
- nonlocal은 코드 최상단에 위치시키며, nonlocal 앞에 같은 변수 이름을 사용하지 않는다.
- nonlocal은 parameter, for 루프 대상, 클래스/함수 정의 등에 사용하지 않는다.
- global과는 다르게 이미 있는 이름과의 연결만 가능

### 범위 확인하기

- `globals()`  `locals()`

- namespace를 딕셔너리로 정리한다.
- `locals()`: local namespace를 정리
- `globals()`: global, local, builtin 정보 모두 딕셔너리로 정리



## 함수의 문서화(Doc-string)

### Docstring (Document String)

- 함수나 클래스의 설명

### Naming Convention

- 상수 이름은 영문 전체를 대문자

  ```python
  PI = 3.141592
  ```

- 클래스 및 예외의 이름은 각 단어의 첫 글자만 영문 대문자

- 이외 나머지는 소문자 또는 밑줄로 구분한 소문자

- 함수의 경우 어떤 기능인지, 반환값은 무엇인지 파악 가능하도록

- 가급적 약어 사용 지양

- 



## 함수 응용

### map

- `map(function, iterable)`
- iterable 데이터의 모든 요소에 function을 적용하고 그 결과를 **map object**로 반환

```python
n, m = map(int, input().split())
```

### filter

- `filter(function, iterable)`
- iterable 데이터의 모든 요소에 function을 적용해 그 결과가 True인 것들을 **filter object**로 반환

```python
data_even = list(filter(lambda x: x%2 == 0, data))
```

### zip

- `zip(*iterable)`
- 복수의 iterable을 모아 **튜플**을 원소로 하는 **zip object** 반환

```python
data1 = ['a', 'b']
data2 = [1, 2]
data3 = list(zip(data1, data2))
# data3 = [('a', 1), ('b', 2)]
```

### lambda 함수

- `lambda x, y: <x, y에 관한 리턴값>`
- 표현식을 계산한 결과 값을 반환하는 함수
- 이름이 없는 함수이므로 익명함수라고도 한다.
- 간편 조건문 외 조건문이나 반복문을 가질 수 없다.
- return문을 가질 수 없다.

### 재귀 함수(recursive function)

- 자기 자신을 호출하는 함수
- 1개 이상의 base case(종료 트리거)가 존재하고 수렴하도록 작성
- 메모리 스택이 넘치면 stack overflow 발생
- 파이썬에서 최대 재귀 깊이(maximum recursion depth)는 **1,000번**.
- 1,000번을 넘어가면 Recursion Error 발생
- 보통은 반복문이 더 빠르다.

```python
# 팩토리얼 예시
def factorial(n):
    # 초기값
    if n == 0 or n == 1:
        return 1
    else:
        # 점화식
        return n * factorial(n-1)
```



	##### 1급 객체

1. 변수나 데이타에 할당 할 수 있어야 한다.
2. 객체의 인자로 넘길 수 있어야 한다.
3. 객체의 리턴값으로 리턴 할수 있어야 한다.
