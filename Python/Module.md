# 모듈

[모듈과 패키지](#모듈과-패키지)

[파이썬 표준 라이브러리](#파이썬-표준-라이브러리)

[가상환경](#가상환경)

~~[유용한 패키지와 모듈](#유용한-패키지와-모듈)~~

[사용자 모듈과 패키지](#사용자-모듈과-패키지)

<br>

## 모듈과 패키지

> [모듈과 패키지](#모듈과-패키지)
>
> [모듈과 패키지 불러오기](#모듈과-패키지-불러오기)

<br>

### 모듈과 패키지

> - 모듈
>
>   > 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
>
> - 패키지
>
>   > - 특정 기능과 관련된 여러 모듈의 집합
>   > - 패키지 안에 또 다른 서브 패키지를 포함

<br>

### 모듈과 패키지 불러오기

> ```python
> # module.function 으로 사용
> import module
> # function을 바로 사용 가능
> from module import var, function, Class
> # 모듈에서 전체를 가지고 온다
> from module import *
> 
> from package import module
> from package.module import var, function, Class
> ```
>

---

<br><br>

## 파이썬 표준 라이브러리

### 파이썬 표준 라이브러리(Python Standard Library, PSL)

[표준 라이브러리](https://docs.python.org/ko/3/library/index.html)

[표준 라이브러리 Git](https://github.com/python/cpython/tree/main/Lib)

<br>

### 파이썬 패키지 관리자(pip)

> - PyPI(Python Package Index)에 저장된 외부 패키지 설치를 돕는 패키지 관리 시스템
>
> ```bash
> # 패키지 설치
> $ pip install SomePackage
> $ pip install SomePackage==1.0.5
> $ pip install 'SomePackage>=1.0.4'
> 
> # 패키지 삭제
> # 패키지 업그레이드 시 과거 패키지는 자동 삭제됨
> $ pip uninstall SomePakage
> # 패키지 목록 및 정보
> $ pip list
> $ pip show SomePackage
> # 지금 설치된 패키지 확인
> $ pip freeze
> # 설치된 패키지 텍스트 파일로 생성
> $ pip freeze > requirement.txt
> # 텍스트 파일로 패키지 설치
> $ pip install -r requirement.txt
> 
> ```
>

---

<br><br>

## 가상환경

### 가상환경

> - 복수의 프로젝트 중에 패키지들의 여러 버전을 프로젝트별로 관리할 수 있도록 함

<br>

### venv

> - 가상 환경을 만들고 관리하는데 사용되는 모듈(Python 3.5+)
> - 특정 폴더에 가상 환경을 만들고 패키지를 저장, 관리
>
> ```bash
> # 보통 폴더명은 venv로 한다.
> $ python -m venv venv
> $ source venv/Scripts/activate
> # 가상환경 폴더 상위 폴더에서 실행
> ```

---

<br><br>

## 유용한 패키지와 모듈

---

<br><br>

## 사용자 모듈과 패키지

### 모듈

> `.py` 파일로 저장하고 같은 폴더 내에서 `import`로 불러와 사용한다.

### 패키지

> - 모듈의 상위 폴더가 패키지
> - 각 폴더마다 `__init__.py`를 만들어 패키지로 인식시킨다. (파이썬 하위버전에서도 호환을 위함)
>
> ```python
> from package import module
> from package.module import var, function, Class
> 
> # 서로 다른 패키지의 이름이 같은 패키지 사용
> from package.subpackage_1 import module_a
> from package.subpackage_2 import module_a as module_b
> 
> # 상위 패키지나 다른 서브 패키지 사용
> from ..up_package import module
> from first_package.second_package.third_package import module
> ```
>

---

