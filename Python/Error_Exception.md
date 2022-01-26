# 에러/예외 처리(Error/Exception Handling)

> [디버깅](#디버깅)
>
> [에러와 예외](#에러와-예외)
>
> [예외 처리](#예외-처리)
>
> [예외 발생 시키기](#예외-발생-시키기)

<br>

## 디버깅

> - print문이나 breakpoint 활용
> - 누군가에게 설명하면서 정리해보는 것도 좋다

---

<br><br>

## 에러와 예외

> [문법 에러(Syntax Error)](#문법-에러syntax-error)
>
> [예외(Exception)](#예외exception)
>
> [예외 종류](#예외-종류)

<br>

### 문법 에러(Syntax Error)

> - Invalid syntax
> - assign to literal
> - EOL (End of Line)
> - EOF (End of File)

<br>

### 예외(Exception)

> - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
> - 여러 타입으로 나뉜다.
> - 사용자 정의 예외를 만들어 관리할 수 있다.

<br>

### 예외 종류

> - ZeroDivisionError: 0으로 나누고자 할 때 발생
>
> - NameError: namespace 상에 이름이 없는 경우
>
> - TypeError
>
>   > - 타입 불일치
>   > - argument 누락
>   > - argument 개수 초과
>   > - argument 타입 불일치
>
> - ValueError: 타입은 올바르나 값이 적절하지 않은 경우
>
> - IndexError: 인덱스가 존재하지 않거나 범위를 벗어나는 경우
>
> - KeyError: 해당 키가 존재하지 않는 경우
>
> - ModuleNotFoundError: 존재하지 않는 모듈을 import하는 경우
>
> - ImportError: 모듈은 잇지만 존재하지 않는 클래스/함수를 가져오는 경우
>
> - KeyboardInterrupt: 임의로 프로그램을 종료하였을 때
>
> - IndentationError: Identation이 적절하지 않은 경우 (tab, 공백 구분)

---

<br><br>

## 예외 처리

> [예외 처리](#예외-처리)
>
> [작성 방법](#작성-방법)

<br>

### 예외 처리

> - try 문(statement) / except 절(clause)
> - try 문
>   - 오류가 발생할 가능성이 있는 코드 실행
>   - 예외가 발생하지 않으면, except 실행 없이 종료
> - except 절
>   - 예외 발생 시 except 절 실행
>   - 예외 상황을 처리하는 코드를 통해 적절한 조치

<br>

### 작성 방법

> ```python
> # try 문은 한 개 이상의 except 문 필요
> try:						# 코드를 실행
>     try 명령문				
> except 예외그룹1 as 변수1:	# try문에서 예외 발생 시 실행
>     예외처리 명령문1		   # 변수의 경우 에러메시지를 저장
> except 에외그룹2 as 변수2:	
>     예외처리 명령문2
> except:						# 에러1,2가 아닌 에러 발생시 실행
>     예외처리 명령문3
> else:						# try문에서 예외가 발생하지 않으면 실행
>     else 명령문
> finally:					# 예외 발생 여부와 관계 없이 항상 실행
>     finally 명령문
> ```
>

---

<br><br>

## 예외 발생 시키기

> [raise](#raise)
>
> [assert](#assert)

<br>

### raise

> ```python
> raise <표현식>(메시지)
> raise ValueError('값 에러 발생')
> ```
>

<br>

### assert

> - 예외를 강제로 발생
> - 무조건 AssertionError가 발생
> - 디버깅 용도로 사용
> - 특정 조건이 거짓이면 발생
>
> ```python
> assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
> ```

---

