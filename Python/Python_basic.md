# 파이썬 (Python)

- Easy to learn
- Expressive Lnaguage
- 크로스 플랫폼 언어
- 인터프리터 언어(Interpreter)
- 객체 지향 프로그래밍

[기초 문법](#기초-문법)

[파이썬 자료형 (Python Datatype)](#파이썬-자료형-python-datatype)

[컨테이너(Container)](#컨테이너container)

[형 변환(Typecasting)](#형-변환typecasting)

[연산자(Operator)](#연산자operator)

## 파이썬 개발 환경 (Python Environment)

### 파이썬 개발환경 종류

- 대화형 환경
- 스크립트 실행
- IDLE (Intergrated Devleopment and Learning Environment)
- Jupyther Lab
  - IDLE 확장판
  - 데이터분석 / 머신러닝 / 딥러닝

## 기초 문법

- **PEP8 스타일** 가이드에 따름

- 스타일가이드의 경우 모든 사람이 같은 코드를 동일하게 작성할 수 있게 해줌

  ex) '', "" 를 혼용하지 않는다, 띄어쓰기, 여백



### 들여쓰기(Identation)

- Tab  = 띄어쓰기 4번
- 띄어쓰기와 Tab은 혼용 금지
- 되도록 **띄어쓰기** 사용



### 변수(Variable)

- abc		=		10

  이름 	할당	 값

- 객체를 참조하기 위해 사용되는 이름

​		객체: 숫자, 문자, 클래스 등 값을 가진 모든 것

- ```python
  type() 		# 값의 타입
  id()		# 메모리 주소
  ```

#### 변수 연산

```python
a = 1
b = 2
c = '파이썬'


a + b 			# 숫자 + 숫자
'Hello' + c		# 문자 + 문자
c = c * 3		# 문자 * 숫자 (문자 반복)
```

#### 변수 할당

```python
a = b = 1		# 같은 값 할당 가능 (a, b = 1 은 오류남)
a, b = 1, 2		# 다른 값 동시 할당 가능
a, b = b, a		# 값 바꾸기 (기본은 임시 변수 tmp 활용)
```

#### 식별자(Identifiers)

- 영문 알파벳, 언더스코어`_`, 숫자로 구성

- 첫 글자 숫자 금지

- 길이 제한 X

- 대소문자 구별

- 금지어

  ```python
  import keword
  print(keyword.kwlist)
  
  [False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finaaly, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield]
  ```

#### 사용자 입력

```python
name = input('블라블라')
```

- 반환값은 항상 `str`

#### 주석 (Comment)

```python
# : 한줄주석
"""
여러줄
주석
"""
```

- VS Code 등에서는 `ctrl + /`으로 여러줄 주석 가능

---

## 파이썬 자료형 (Python Datatype)

[불린(Boolean)](#불린boolean)

[정수(Int)](#정수int)

[실수(Float)](#실수float)

[복소수(Complex)](#복소수complex)

[문자열(String Type)](#문자열string-type)

### 자료형 분류

- Data Type

- Booolean Type : True / False
- Numeric Type
  - Int
  - Float
  - Complex
- String Type



### None

- 값이 없음을 표현

```python
type(None) # << NoneType
```



### 불린(Boolean)

- 0, 공백 외에는 True

```python
bool()		# True / False 검증

bool(-1)	# True
bool([0])	# True
bool('')	# False (공백 하나가 있으면 True)
bool([])	# False
```



### 정수(Int)

- Python의 경우 오버플로우가 없다 (long 타입 없음)

```python
0b10		# 2진수(binary) 	
0o10		# 8진수(Octal)	
0x10		# 16진수(Hexadecimal)
```



### 실수(Float)

- Floating point rounding error

```python
3.14 - 3.02 == 0.12		# False !!!
# 3.14 - 3.02 = 0.1200000000001


# 실수 연산 확인법
abs(x - y) <= 1e-10		# 절댓값 오차가 적은가?

import sys
sys.float_info.epsilon	# = 2.220446049250313E-16

import math				# epsilon은 False가 날 때가 있어서 inclose 추천
math.isclose(x, y)
```



### 복소수(Complex)

```python
a = 1 + 2j
a.real	# 1.0
a.imag	# 2.0
```



### 문자열(String Type)

- Immutable (불변)

```python
a = 'Hello'
a[1] = 'i'		# Error! 문자열 중간을 바꿀 수 없음
```

- Iterable ( 순회가능한 )

```python
a = '123'
for char in a:	# 문자 하나씩 접근은 가능
```

- `''' '''`, `""" """` 3중 따옴표 : 따옴표 안에 따옴표 가능

##### Escape sequence

```python
\n	# 줄바꿈
\t	# 탭
\r	# 캐리지 리턴
\0	# Null
\\	# \
\'	# '
\"	# "
```

##### String Interpolation

```python
print('Hello, %s' % x) 		# %s 문자, %d 정수, %f 실수
print('Hello, {}, {}'.format(x, y))
print(f'Hello, {x}, {y})	# Python 3.6+
      						# {x:.3f} 소수점표기
      						# {x * 2} 연산 가능
      						# {x:0>10.2f} --> 10자리 표기, 소수점은 2째자리까지
      						# 0으로 나머지를 채운다. >는 우측정렬 ^는 가운데정렬
```

---

## 컨테이너(Container)

- 컨테이너
  - 시퀀스형
    - 리스트
    - 튜플
    - 레인지
  - 비시퀀스형
    - 세트
    - 딕셔너리

[리스트(List)](#리스트list)

[튜플(Tuple)](#튜플tuple)

[레인지(Range)](#레인지range)

[셋(Set)](#셋set)

[딕셔너리(Dictionary)](#딕셔너리dictionary)

[패킹/언패킹(Packing/Unpacking)](#패킹언패킹packingunpacking)

[형 변환(Typecasting)](#형-변환typecasting)



### 리스트(List)

- 순서를 가짐

- 가변 자료형

  ```python
  # 초기화 선언
  a = []
  a = list()
  
  b = a[i]	# []로 인덱스
  			# 시작은 0, 맨 끝부터는 -1에서 시작
  c = a[][]	# 다차원
  ```



### 튜플(Tuple)

- 순서를 가짐

- 불변 자료형

  ```python
  # 초기화 선언
  a = ()
  a = tuple()
  
  b = a[i]	# 수정은 안되지만 접근은 가능
  c = 1,		# 단일 항목에는 쉼표가 붙어야 tuple
  d = 1, 2, 3	# 복수 항목은 마지막 쉼표 불필요
  ```



### 레인지(Range)

- 숫자 시퀀스

```python
range(n)		# 0부터 n-1
range(n, m)		# n부터 m-1
range(n, m, s)	# n부터 m-1까지 s만큼 증가
				# s에 음수로 n부터 m-1까지 감소 가능
```



### 패킹/언패킹(Packing/Unpacking)

```python
x, *y = 1, 2, 3, 4
# x = 1
# y = [2, 3, 4]
# 리스트로 패킹

def function(*x)
# 튜플로 언패킹
```



### 셋(Set)

- 순서 없음
- 가변 자료형
- 중복 불가
- 순서가 없어 인덱싱 불가

```python
# 초기화 선언
a = set()

# 아래는 Dictionary # 빈 set은 무조건 set()
a = {} 		
```



### 딕셔너리(Dictionary)

- 순서 없음
- key-value 쌍으로 이뤄진 객체를 참조
  - key: 불변 자료형만 가능
    - string, interger, float, boolean, tuple, range
  - value: 형태 상관X

```python
# 초기화 선언
a = {}
a = dict()


a = { 'x': 1, 'y': 'k', 75: [1, 2, 3]}
```



## 형 변환(Typecasting)

- 암시적 형 변환(Implicit) : 사용자 의도하지 않고, 파이썬 내부적으로 자료형 변환
  - `True` = 1
  - `int` + `float` = `float`
  - `int` + `complex`  =  `complex`
  - `float` + `complex` = `complex`
- 명시적 형 변환(Explicit) : 사용자가 의도적으로 변환
  - int
    - str*(정수로 적힌 문자열만), float
  - float
    - str*(실수로 적힌 문자열만), int
      - float(3) = 3.0
  - str
    - int, float, list, tuple, dict

|                | string | list           | tuple          | range | set            | dictionary |
| -------------- | ------ | -------------- | -------------- | ----- | -------------- | ---------- |
| **string**     | -      | o              | o              | x     | o              | x          |
| **list**       | o      | -              | o              | x     | o              | x          |
| **tuple**      | o      |                | -              | x     | o              | x          |
| **range**      | o      | o              | o              | -     | o              | x          |
| **set**        | o      | o              | o              | x     | -              | x          |
| **dictionary** | o      | o<br />(key만) | o<br />(key만) | x     | o<br />(key만) | -          |

#### 기타

- trailing comma: 리스트나 딕셔너리 등의 요소를 엔터로 구분하며 입력할 때 끝에 `,`를 붙인다.

  ```python
  a = {
      0 : 1,
      1 : 2,
      2 : 3,  # trailing comma를 넣어준다.   
  }
  
  ```

  





---

## 연산자(Operator)

### 산술 연산자 (Airthmetic Operator)

- `+` `-` `*` `/` : 사칙연산
- `//` : 몫
- `%` : 나머지
- `**`: 거듭제곱



### 비교 연산자(Comparison Operator)

- `<` `<=` `>` `>=`
- `==` `!=`
- `is` `is not`



### 논리 연산자(Logical Operator)

- `and` `or` `Not`

- and 
  - 첫번째 값이 False --> 첫번째 값 반환
  - 첫번째 값이 True --> 두번째 값 반환
- or 
  - 첫번째 값이 True --> 첫번째 값 반환
  - 첫번째 값이 False --> 두번째 값 반환



### 멤버십 연산자(Membership Operator)

- `in` `not in`



### 시퀀스형 연산자(Sequence Type Operator)

- `+`: list, tuple, 문자열 접합
- `*`: list, tuple, 문자열 반복

- ```python
  [a, b, c, d][0:3]	# 0~2
  [a, b, c, d][:3]	# 0~2
  [a, b, c, d][2:]	# 2~3
  [a, b, c, d, e][0:5:2] # 0, 2, 4
  [::]	# 전체
  [::-1]	# 전체 거꾸로
  ```



### set 연산자

- `|` : 합집합
- `&`:  교집합
- `-`: 여집합
- `^`: 대칭차



## 프로그램 구성 단위

- 식별자 (identifier) 
  - 변수, 함수, 클래스 등 값을 가질 수 있는 이름
- 리터럴 (literal) 
  - 값 그 자체

- 표현식 (Expression) 
  - 새로운 값을 생성하거나 계산하는 코드 조각
  - 그 자체를 값으로 사용할 수 있는 것.
- 문장 (Statement) 
  - 특정 작업을 수행하는 코드 전체
  - 파이썬이 실행 가능한 최소한의 코드 단위
  - 모든 표현식은 문장
- 함수 (Function)
  - 특정 명령을 수행하는 함수 묶음
- 모듈 (Module)
  - 함수/클래스의 모음
  - 하나의 프로그램을 구성하는 단위
- 패키지 (Package)
  - 프로그램/모듈 묶음
  - 프로그램: 실행하기 위한 것
  - 모듈: 다른 프로그램에서 불러와 사용하기 위한 것
- 라이브러리 (Library)
  - 패키지 모음