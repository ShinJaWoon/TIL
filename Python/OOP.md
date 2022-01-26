# 객체지향 프로그래밍(OOP)

Object Oriented Programming

## 객체지향 프로그래밍(OOP)

### 객체지향 프로그래밍

#### 객체란?

- 객체(Object)는 특정 타입의 인스턴스(instance)

  > - 1, 23, 456 >> int의 인스턴스
  > - 'a', 'hello' >> string의 인스턴스
  > - [1, 2, 3], [] >> list의 인스턴스

- 객체의 특징

  > - 타입(type): 어떤 연산자(operator)와 조작(method)가 가능한지
  > - 속성(attribute): 어떤 상태(데이터)를 가지는지
  > - 조작법(method): 어떤 행위(함수)가 가능한지

#### 객체지향 프로그래밍

- 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

- 절차지향과 객체지향

  > - 절차지향: 함수에 의한 데이터 반환값에 의한 변화 ex) a = sorted(a)
  > - 객체지향: 데이터가 메소드에 의해 변화가능 ex) a.sort()

- 필요한 이유: 추상화(현실 세계를 프로그램 설계에 반영)

- 클래스(class), 인스턴스(instance), 속성(attribute), 메소드(method)

- 장점

  > - 프로그램을 유연하게 변경 가능 >> 대규모 소프트웨어 개발 \
  > - 배우기 쉽다
  > -  소프트웨어의 간편한 개발 및 유지보수
  > -  직관적인 코드 분석 가능

### OOP 기초

#### 기본 문법

- 정의 및 사용방법

  > - 클래스 정의 `class MyClass`
  > - 인스턴스 생성 `my_instance = MyClass()`
  > - 메소드 호출 `my_instance.my_method()`
  > - 속성 `my_instance.my_attribute`

- 클래스를 통해 각각의 인스턴스를 생성

  > - 클래스: 객체들의 분류
  > - 인스턴스: 하나하나의 실체/예시
  > - 속성: 객체들이 가지게 될 데이터
  > - 메소드: 객체에 공통적으로 적용가능한 함수

- 객체 비교

  > - `==` : 두 변수의 내용(값)이 같은 경우
  >            동등한(equal)
  > - `is` : (identical)두 변수의 동일한 객체를 가리키는 경우
  >            동일한(identical)

### 인스턴스

- 인스턴스 변수

  > - 인스턴스가 개인적으로 가지는 속성(attribute)
  > - 각 인스턴스들의 고유한 변수
  > - 생성자 메소드에서 `self.<name>` 으로 정의
  > - 인스턴스 생성 이후 `<instance>.<name>`으로 접근, 할당

- 인스턴스 메소드

  > - 인스턴스 변수를 사용/변경하는 메소드
  > - 호출 시, 첫번째 인자로 인스턴스 자기자신(self) 전달
  >
  > ```python
  > class MyClass:
  >     def instance_method(self):
  > 
  > my_instance = MyClass()
  > my_instance.instance_method()
  > # 실제로는 아래와 같이 동작
  > # MyClass.instance_method(my_instance)
  > ```
  >
  > 

- self

  > - 인스턴스 자기자신
  > - 인스턴스 메소드는 호출 시 첫 번째 인자로 자기자신 전달
  > - 인스턴스 메소드 정의 시 첫 번째 매개변수를 self로 둔다.
  > - 다른 단어를 써도 되지만 암묵적인 규칙

- 생성자(constructor) 메소드

  > - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
  > - 인스턴스 변수들의 초기값 설정
  >
  > ```python
  > class MyClass:
  >     def __init__(self):
  > ```

- 소멸자(destructor) 메소드

  > - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
  >
  > ```python
  > class MyClass:
  >     def __del__(self):
  > ```

- 매직 메소드(스페셜 메소드)

  > - Double underscore `__`가 있는 메소드
  > - 특정 상황에 자동으로 불리는 메소드
  >
  > ```python
  > __str__(self): 해당 객체의 출력 형태, 인스턴스 출력시 __str__의 return값 출력, str(<instance>)로 호출 가능
  > __gt__(self, other): 부등호 연산자(>, greather than)
  > ```
  >
  > - 부등호: lt(less than), le(less equal), eq, ge, ne 등
  > - len, reversed 등 여러가지 존재
  > - `dir(<instnace>)`로 확인 가능



### 클래스

- 클래스 변수(클래스 속성)

  > - 한 클래스의 모든 인스턴스가 똑값은 값을 가지는 속성
  >
  > - `<classname>.<name>` 으로 접근 및 할당

- 클래스 메소드

  >- 클래스가 사용할 메소드
  >
  >- `@classmethod` 데코레이터를 사용하여 정의
  >
  >- 호출 시, 첫 번째 인자로 클래스(cls) 전달
  >
  >  ```python
  >  class MyClass:
  >      
  >      @classmethod
  >      def class_method(cls):
  >          
  >  MyClass.class_method()
  >  ```

- 스태틱 메소드

  > - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
  >
  > - 속성을 다루지 않고 단지 기능만 하는 메소드를 정의할 때 사용
  >
  >   ```python
  >   class MyClass:
  >       
  >       @staticmethod
  >       def class_method():
  >           
  >   MyClass.class_method()
  >   ```

### 메소드 정리

## 객체 지향의 핵심개념

### 추상화

### 상속

### 다형성

### 캡슐화

