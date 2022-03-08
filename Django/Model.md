# Model

## Model

> - 단일 데이터에 대한 정보
> - 사용자가 저장하는 데이터들의 필수적인 필드와 동작을 포함 (OOP)
> - 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
> - 일반적으로 각각의 model은 하나의 DB Table에 Mapping

### Database

> - 체계화된 데이터의 모임
>
> #### 쿼리(Query)
>
> > - 데이터를 조회하기 위한 명령어
> > - 조건에 맞는 데이터를 추출, 조작
>
> #### 스키마(Schema)
>
> > - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
> > - 자료 구조와 제약조건(표현방법, 관계)에 대한 전반적인 명세
>
> #### 테이블(Table)
>
> > - 열(olumn): 필드(field) or 속성 이라고도 함
> > - 행(row): 레코드(record) or 튜플 이라고도 함
>
> #### 기본키(PK) - Primary Key
>
> > - 각 행의 고유값
> > - 반드시 설정 필요
> > - Djanog 에서는 id



### Model

> ```python
> # articles/models.py
> class Article(models.Model): # models의 Model 클래스를 상속받음
>     # 아래에 각각의 필드(열)를 선언
>     title = modles.CharField(max_length=10)	# 문자형식, 길이제한 필수
>     content = models.TextField() # 길이 제한 없는 문자형식
>     created_at = models.DateTimeField(auto_now_add=True) 
>     # auto_now_add : 데이터가 생설될 대 시간을 자동으로 저장
>     updated_at = models.DateTimeField(auto_now=True)
>     # auto_now : 현재 시간을 자동으로 저장
>     # null=True == blank=Ture : default값 설정, 숫자는 null 문자는 blank
> ```



## ORM

> - Object_Relational-Mapping
> - 객체지향 프로그래밍 언더를 이용하여 호환되지 않는 유형의 시스템 간 (Django - SQL) 데이터를 변환하는 프로그래밍 기술
> - OOP에서 RDBMS를 연동할 때, 데이터베이스와 객체지향 언어 간의 데이터를 변환
> - Django는 내장 Django ORM을 사용



## Migrations

> - django가 model에 생긴 변화를 반영하는 방법
> - OOP class를 Table로 만드는 과정
>
> ```bash
> model 변경시 아래 3단계 무조건 거칠것!
> ===================================================
> >>>>> models.py 변경
> $ python manage.py makemigrations	# 변경된 model에서 migration을 생성
> $ python manage.py migrate # migrate를 DB에 반영
> 
> =====================================================
> 
> $ python manage.py sqlmigrate 앱이름 번호만  # migration이 SQL 문으로 어떻게 보일지 확인
> $ python manage.py showmigrations  # migrate 파일들이 migration 되었는지 확인
> ```
>
> 

## Database API

> ```python
> <Class name>.objects.<Query Set>
> ```
>
> ```bash
> $ pip install ipython
> $ pip install django-extensions
> $ pip freeze > requirements.txt
> 
> >>>> settings.py 에 INSTALLED_APPS 에 'django_extenstions' 추가
> 
> $ python manage.py shell_plus
> >> <Class name>.objects.<Query Set>
> ```
>
> 

## CRUD

> - Create 생성 / Read  읽기 / Update 갱신 / Delete 삭제

### Create

> #### 인스턴스 생성
>
> > - Shell 에서 인스턴스 변수들을 설정하고 save
> >
> > ```bash
> > >>> a = <Class name>
> > >>> a.<instance 변수> = b
> > >>> a.save()
> > ```
>
> #### 인스턴스 활용
>
> > - 인스턴스를 생성할 때 바로 변수를 설정
> >
> > ```bash
> > >>> a = <Class name>(B='b', C='c' ....)
> > >>> a.save()
> > ```
>
> #### objects의 create 사용
>
> > - save()를 할 필요 없이 objects의 create 메소드를 사용
> >
> > ```bash
> > >>> <Class name>.objects.create(B='b', C='c' ...)
> > ```
>
> #### 유효성 검사
>
> > - 정해진 조건에 맞지 않는 값이 있을 경우 에러 발생
> > - save() 전에 사용해야 하므로 create 메소드 방식에서는 사용 불가
> >
> > ```bash
> > >>> a.full_clean()
> > ```
> >
> > 



### Read

> ```bash
> # all() : 전체 객체 조회. QuerySet 리스트로 나옴
> >>> <Class name>.objects.all()
> 
> # get() : 1개 객체 조회. 없는 값을 찾거나 같은 값이 있을 경우 에러가 나므로 보통 id값을 사용
> # from django.shortcuts import get_object_or_404
> # 값이 없으면 404 Error를 발생시키게 만듦
> >>> <Class name>.objects.get(id=<원하는 id값>)
> 
> # filter() : 조건을 만족하는 모든 데이터를 조회
> 
> ```



### UPDATE

> - DB 에서 수정할 데이터를 가져온다
> - 변경한다
> - 저장한다 save()
>
> ```bash
> >>> a = <classname>.objects.get(pk=<가져올 id>)
> >>> a.<변수> = 'K'    # 변수값 변경
> >>> a.save()
> ```



### DELETE

> - DB 에서 수정할 데이터를 가져온다
> - 삭제한다.
>
> ```bash
> >>> a = <classname>.objects.get(pk=<가져올 id>)
> >>> a.delete()
> ```
>
> 



## Admin Site

> - 서버의 관리자가 활용하기 위한 페이지
> - 웹에서 CRUD를 할 수 있도록 함



### admin 생성 및 등록

> #### admin 생성
>
> ```bash
> $ python manage.py createsuperuser
> ```
>
> #### admin 등록
>
> ```python
> # appname/admin.py
> 
> from django.contrib import admin
> from .models import <Classname>
> 
> admin.site.register(<Classname>)
> ```
>
> - `__str__`에 등록된 형태로 데이터가 출력됨
>
> #### admin 출력 변경
>
> ```python
> # appname/admin.py
> 
> from django.contrib import admin
> from .models import <Classname>
> 
> class <Classname>Admin(admin.ModelAdmin):
>     list_display = ('pk', 'name', ...) # 출력 필드 설정
>     list_filter = ('created_at', )  # 오른쪽에 필터 설정 ,로 튜플로 만들기 주의
>     list_display_links = ('pk', 'name', )  # 링크가 걸릴 필드 설정
>     list_editable = ('nick_name', )  # 목록에서 수정가능. (display에 포함, display_links에 미포함)
>     list_perpage = 3
> 
> admin.site.register(<Classname>, <Classname>Admin)
> 
> ```
>
> 