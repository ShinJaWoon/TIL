# 객체지향 프로그래밍(OOP)

> Object Oriented Programming
>
> [객체지향 프로그래밍(OOP)](#객체지향-프로그래밍oop)
>
> [객체 지향의 핵심개념](#객체-지향의-핵심개념)

<br>

## 객체지향 프로그래밍(OOP)

> [객체지향 프로그래밍](#객체지향-프로그래밍)
>
> [OOP 기초](#oop-기초)
>
> [인스턴스](#인스턴스)
>
> [클래스](#클래스)
>
> [메소드 정리](#메소드-정리)

<br>

### 객체지향 프로그래밍

> #### 객체란?
>
> - 객체(Object)는 특정 타입의 인스턴스(instance)
>
>   > - 1, 23, 456 >> int의 인스턴스
>   > - 'a', 'hello' >> string의 인스턴스
>   > - [1, 2, 3], [] >> list의 인스턴스
>
> - 객체의 특징
>
>   > - 타입(type): 어떤 연산자(operator)와 조작(method)가 가능한지
>   > - 속성(attribute): 어떤 상태(데이터)를 가지는지
>   > - 조작법(method): 어떤 행위(함수)가 가능한지
>
> #### 객체지향 프로그래밍
>
> - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
>
> - 절차지향과 객체지향
>
>   > - 절차지향: 함수에 의한 데이터 반환값에 의한 변화 ex) a = sorted(a)
>   > - 객체지향: 데이터가 메소드에 의해 변화가능 ex) a.sort()
>
> - 필요한 이유: 추상화(현실 세계를 프로그램 설계에 반영)
>
> - 클래스(class), 인스턴스(instance), 속성(attribute), 메소드(method)
>
> - 장점
>
>   > - 프로그램을 유연하게 변경 가능 >> 대규모 소프트웨어 개발 \
>   > - 배우기 쉽다
>   > - 소프트웨어의 간편한 개발 및 유지보수
>   > - 직관적인 코드 분석 가능

<br>

### OOP 기초

> #### 기본 문법
>
> - 정의 및 사용방법
>
>   > - 클래스 정의 `class MyClass`
>   > - 인스턴스 생성 `my_instance = MyClass()`
>   > - 메소드 호출 `my_instance.my_method()`
>   > - 속성 `my_instance.my_attribute`
>
> - 클래스를 통해 각각의 인스턴스를 생성
>
>   > - 클래스: 객체들의 분류
>   > - 인스턴스: 하나하나의 실체/예시
>   > - 속성: 객체들이 가지게 될 데이터
>   > - 메소드: 객체에 공통적으로 적용가능한 함수
>
> - 객체 비교
>
>   > - `==` : 두 변수의 내용(값)이 같은 경우
>   >       동등한(equal)
>   > - `is` : (identical)두 변수의 동일한 객체를 가리키는 경우
>   >       동일한(identical)

<br>

### 인스턴스

> #### 인스턴스 변수
>
> > - 인스턴스가 개인적으로 가지는 속성(attribute)
> > - 각 인스턴스들의 고유한 변수
> > - 생성자 메소드에서 `self.<name>` 으로 정의
> > - 인스턴스 생성 이후 `<instance>.<name>`으로 접근, 할당
>
> #### 인스턴스 메소드
>
> > - 인스턴스의 속성을 사용/변경하는 메소드
> > - 호출 시, 첫번째 인자로 인스턴스 자기자신(self) 전달
> >
> > ```python
> > class MyClass:
> >     def instance_method(self):
> > 
> > my_instance = MyClass()
> > my_instance.instance_method()
> > # 실제로는 아래와 같이 동작
> > # MyClass.instance_method(my_instance)
> > ```
> >
>
> #### self
>
> > - 인스턴스 자기자신
> > - 인스턴스 메소드는 호출 시 첫 번째 인자로 자기자신 전달
> > - 인스턴스 메소드 정의 시 첫 번째 매개변수를 self로 둔다.
> > - 다른 단어를 써도 되지만 암묵적인 규칙
>
> #### 생성자(constructor) 메소드
>
> > - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
> > - 인스턴스 변수들의 초기값 설정
> >
> > ```python
> > class MyClass:
> >     def __init__(self):
> > ```
>
> #### 소멸자(destructor) 메소드
>
> > - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
> >
> > ```python
> > class MyClass:
> >     def __del__(self):
> > ```
>
> #### 매직 메소드(스페셜 메소드)
>
> > - Double underscore `__`가 있는 메소드
> > - 특정 상황에 자동으로 불리는 메소드
> >
> > ```python
> > __str__(self): 해당 객체의 출력 형태, 인스턴스 출력시 __str__의 return값 출력, str(<instance>)로 호출 가능
> > __gt__(self, other): 부등호 연산자(>, greather than)
> > ```
> >
> > - 부등호: lt(less than), le(less equal), eq, ge, ne 등
> > - len, reversed 등 여러가지 존재
> > - `dir(<instnace>)`로 확인 가능

<br>

### 클래스

> #### 클래스 변수(클래스 속성)
>
> > - 한 클래스의 모든 인스턴스가 똑값은 값을 가지는 속성
> >
> > - `<classname>.<name>` 으로 접근 및 할당
>
> #### 클래스 메소드
>
> >- 클래스가 사용할 메소드
> >
> >- `@classmethod` 데코레이터를 사용하여 정의
> >
> >- 호출 시, 첫 번째 인자로 클래스(cls) 전달
> >
> > ```python
> > class MyClass:
> >
> >     @classmethod
> >     def class_method(cls):
> >
> > MyClass.class_method()
> > ```
>
> #### 스태틱 메소드
>
> > - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
> >
> > - 속성을 다루지 않고 단지 기능만 하는 메소드를 정의할 때 사용
> >
> >   ```python
> >   class MyClass:
> >         
> >       @staticmethod
> >       def class_method():
> >         
> >   MyClass.class_method()
> >   ```

<br>

### 메소드 정리

>#### 인스턴스 메소드
>
>- self 매개변수를 통해 객체에 정의된 속성 및 다른 메소드에 접근
>- 데코레이터 불필요
>- 클래스 자체에도 접근 가능
>- 인스턴스 메소드가 클래스 상태를 수정할 수도 있다. 
>
>#### 클래스 메소드
>
>- 클래스를 가리키는 cls 매개 변수를 받음
>- @classmethod 데코레이터 필요
>- 객체 인스턴스 상태는 수정할 수 없음
>
>#### 스태틱 메소드
>
>- 임의의 매개변수를 사용 가능하지만, self나 cls는 사용하지 않음
>- @staticmethod 데코레이터 필요
>- 객체 상태나 클래스 상태를 수정할 수 없음
>- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속

---

<br>

<br>

## 객체 지향의 핵심개념

> [추상화](#추상화)
>
> [상속](#상속)
>
> [다형성](#다형성)
>
> [캡슐화](#캡슐화)

<br>

### 추상화

>- 현실 세계를 프로그램 설계에 반영

<br>

### 상속

>#### 상속
>
>- 두 클래스 사이에 부모 - 자식 관계를 정립
>- 모든 파이썬 클래스는 object를 상속받음
>- 하위 클래스는 상위 클래스에 정의된 속성, 메소드를 상속받음
>- 코드 재사용성이 높아짐
>- 메소드 오버라이딩을 통해 하위 클래스에서 재정의 가능
>- 이름공간: 인스턴스 ->자식 클래스-> 부모클래스 순으로 탐색
>
>#### 상속 관련 함수와 메소드
>
>```python
>isinstance(object, classinfo)
># object가 classinfo의 instance이거나 subclass인 경우 True
>
>issubclass(class, classinfo)
># class가 classinfo의 subclass이면 True
># classinfo는 클래스 객체로 이루어진 튜플일 수 있다.
>
>super().
># 자식클래스에서 부모클래스를 사용하고 싶은 경우
>
>.mor
># Method Resolution Order
># 해당 인스턴스가 어떤 부모 클래스를 가지는지 확인하는 메소드
>```
>
>#### 다중 상속
>
>> - 두개 이상의 클래스를 상속받은 경우
>> - 중복된 속성이나 메서드의 경우 먼저 상속받은 순서대로 우선됨

<br>

### 다형성

>#### 다형성
>
>> - 동일한 메소드가 클래스에 따라 다르게 행동
>
>#### 메소드 오버라이딩
>
>> - 상속받은 메소드를 재정의
>> - 부모클래스에서 정의한 메소드를 자식 클래스에서 변경
>> - 부모클래스의 메소드를 실행시키고 싶은 경우 `super()`를 활용

<br>

### 캡슐화

>#### 캡슐화
>
>> - 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단
>> - 파이썬에서는 암묵적으로 존재하지만 언어적으로는 존재하지 않는 경우가 있음
>
>#### 접근제어자 종류
>
>> - Public Access Modifier
>> - Protected  Access Modifier
>> - Private  Access Modifier
>
>#### Public Member
>
>> - 언더바 없이 시작하는 메소드나 속성
>> - 어디서나 호출 가능
>> - 하위 클래스 override 허용
>
>#### Protected Member
>
>> - 언더바 1개 `_`로 시작하는 메소드나 속성
>> - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
>> - 하위 클래스 override 허용
>
>#### Private Member
>
>> - 언더바 2개 `__`로 시작하는 메소드나 속성
>> - 본 클래스 내부에서만 사용이 가능
>> - 하위 클래스 상속 및 호출 불가능 (오류)
>> - 외부 호출 불가능 (오류)
>
>#### getter 메소드와 setter 메소드
>
>> - 변수에 접근할 수 있는 메소드를 별도로 생성
>> - `getter`: 변수의 값을 읽는 메소드
>>   - `@property` 데코레이터 사용
>> - `setter`: 변수의 값을 설정하는 메소드
>>   - `@변수.setter`데코레이터 사용
>>
>> ```python
>> class MyClass:
>>     def __init__(self, name):
>>         self.__name = name
>>      
>>     @property
>>     def name(self):
>>         return self.__name
>>     
>>     @name.property
>>     def name(self, new_name):
>>         self.__name = new_name
>> 
>> a = MyClass('Kim')
>> print(a.name)	#=> 'Kim'
>> a.name = 'Lee'	 
>> print(a.name)	#=> 'Lee'
>> # a.name()이 아니라 a.name으로 사용
>> ```

---

