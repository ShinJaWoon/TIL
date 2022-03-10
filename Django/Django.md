# Django



## Web framework

### Static web page (정적 웹 페이지)

> - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
> - 서버가 클라이언트로부터 정적 웹 페이지에 대한 요청을 받은 경우 추가적인 처리 과정 없이 바로 응답을 보냄
> - **모든 상황, 모든 사용자에게 동일한 정보 표시**
> - 일반적으로 HTML, CSs, JavaScript 로 작성
> - flat page 라고도 함



### Dynamic web page (동적 웹 페이지)

> - 클라이언트로부터 웹 페이지에 대한 요청을 받은 경우, 추가적인 처리 과정 이후 응답을 보냄
> - **방문자와 상호작용하기 때문에 페이지 내용이 그때 그때 다르다.**
> - 서버 사이드 프로그래밍 언어 (python, java, c++)가 사용되며 파일을 처리, 데이터베이스와 상호작용



### Framework

> - 프로그래밍에서 특정 운영체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
> - 재사용이 가능한 코드들을 프레임워크로 통합
> - 개발자가 새로운 어플리케이션을 위한 표준 코드를 다시 작성하지 않도록 도와줌
> - Application Framework라고도 함



### Web framework

> - 웹 페이지 개발의 어려움을 줄이는 것이 주 목적
> - 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함



### Django

> - Python 언어 기반 Web framework
> - spotify, Instagram, Dropbox, Delivery Hero



### Framework Architecture

> - MVC Design Pattern(model-view-controller)
> - 소프트웨어 공학의 디자인 패턴 중 하나
> - Django에서는 MTV Pattern이라고 함



### MTV Pattern

>  #### Model
>
> > - 응용프로그램의 데이터 구조를 정의
> > - 데이터베이스의 기록을 관리(추가, 수정, 삭제)
>
> #### Template (View)
>
> > - 파일의 구조나 레이아웃을 정의
> > - 실제로 내용을 보여주는데 사용 (presentation)
>
> #### View (Controller)
>
> > - HTTP 요청 수신 및 응답 반환
> > - Model을 통해 요청 충족에 필요한 데이터에 접근
> > - template에게 응답의 서식 설정을 맡김





## Django

### Django 시작하기

> #### venv 설정
>
> > ```bash
> > python -m venv venv
> > source venv/Scripts/activate
> > ```
>
> #### Django 설치
>
> > ```bash
> > pip install django==3.2.12
> > pip install django  <- 최신버전
> > 
> > pip freeze > requirements.txt
> > pip install -r requirements.txt
> > ```
>
>  #### 프로젝트 생성
>
> > ```bash
> > django-admin startproject <프로젝트명> .
> > ```
> >
> > - 하이픈 `-` 사용 금지, Django, python 등의 용어 금지
>
> #### 서버 실행
>
> > ```bash
> > python manage.py runserver
> > ```



### Project & Application

> #### Project
>
> > - Application들의 집합
> > - 하나의 프로젝트에는 여러 앱이 포함 가능
> > - 앱은 여러 프로젝트에 있을 수 있음
>
> #### Application
>
> > - 앱에서 실제 요청을 처리하고 페이지를 보여주는 역할
> > - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성



### Django 프로젝트 구조

> #### `__init__.py`
>
> > - Python에서 하나의 패키지로 다루도록 함
>
> #### asgi.py
>
> > - Asynchronous Server Gateway Interface
> > - 어플이 비동기식 웹 서버와 연결 및 소통을 도움
> > - 배포 작업에 사용
>
> #### settings.py
>
> > - 어플리케이션의 모든 설정 포함
>
> #### urls.py
>
> > - 사이트의 url과 적절한 views의 연결 지정
>
> #### wsgi.py
>
> > - Web Server Gateway Interface
> > - 어플리케이션이 웹서버와 연결 및 소통을 도움
> > - 배포에 사용
>
> #### manage.py
>
> > - 커맨드라인 유틸리티
> >
> > ```bash
> > python manage.py <command> [options]
> > ```



### Application 생성 및 구조

> #### Application 생성
>
> > ```bash
> > python manage.py startapp <Application명>
> > ```
> >
> > - Application 명은 **복수형**을 권장
>
> #### admin.py
>
> > - 관리자용 페이지
>
> #### apps.py
>
> > - 앱의 정보 작성
>
> #### models.py
>
> > - 앱에서 사용하는 Model 정의
>
> #### tests.py
>
> > - 테스트코드를 작성하는 곳
>
>  #### views.py
>
> > - view 함수들이 정의되는 곳
>
> 



### Application 등록

> - 프로젝트에서 앱을 사용하기 위해서는 INSTALLED_APPS 리스트에 추가 필요
> - 프로젝트의 `settings.py`에 `INSTALLED_APPS` 에 추가.
> - 등록을 먼저하면 앱이 생성이 되지 않는다.
> - 항상 **생성 후 등록**
> - 상단에는 Local apps, 중단에는 Third party apps, 하단에는 기본 Django apps



## 요청과 응답

### URLs

> #### urls.py
>
> > ```python
> > from django.contrib import admin
> > from django.urls import path
> > from articles import views
> > 
> > urlpatterns = [
> >     path('admin/', admin.site.urls),
> >     path('index/', views.index), 
> > ]
> > ```
>
> #### views.py
>
> > ```python
> > from django.shortcuts import render
> > 
> > # Create your views here.
> > 
> > # 인자로 항상 request를 넣을 것!
> > def index(request):
> >  return render(request, 'index.html')
> > ```
> >
> > - articles 내부에 templates 폴더를 만들고 그 내부에 index.html를 작성한다.
> > - templates 라는 폴더 이름은 framework를 사용하기 위한 조건
>
> #### settings.py
>
> > ```python
> > LANGUAGE_CODE = 'ko-kr'
> > # http://www.i18nguy.com/unicode/language-identifiers.html
> > # django는 소문자로 작성함
> > 
> > TIME_ZONE = 'Asia/Seoul'
> > # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
> > 
> > USE_I18N = True
> > # Internationalization 국제 번역 시스템 활성화 유무
> > USE_L10N = True
> > # Localization 데이터의 지역화된 형식 지정
> > USE_TZ = True
> > # 시간대 인식
> > ```
> >
> > 



## Template

### DTL (Django Template Language)

> - Django template에서 사용하는 built-in template system
> - 조건, 반복, 변수 치환, 필터 등의 기능을 제공
> - 프로그래밍적 로직이 아닌 프레젠테이션 표현을 위한 것
> - Python 코드로 실행되는 것이 아니다!
>
> #### Variable
>
> > ```django
> > # template html
> > {{ 변수명 }}
> > {{ 변수명.index }}
> > {{ 변수명.키값 }}
> > 
> > {{ foods }} # ['apple', 'banana', 'coconut']
> > {{ foods.0 }} # apple
> > {{ info.name }} # Alice
> > ```
> >
> > ```python
> > # views.py
> > def f(request):
> >     foods = ['apple', 'banana', 'coconut', ]
> >     info = {
> >         'name': 'Alice'
> >     }
> >     context = {
> >         'foods': foods,
> >         'info': info,  
> >     }
> >     return render(request, 'f.html', context)
> > ```
> >
> > 
> >
> > - render()를 이용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
> > - 변수 명은 영어, 숫자, 밑줄 `_` 의 조합으로 구성
> >   - 밑줄 `_` 로는 시작 불가
> >   - 공백, 구두점 문자 사용 불가
> > - dot `.` 을 이용하여 변수 속성에 접근 가능
> > - render() 의 세번째 인자로 {'key': value} 딕셔너리 형태로 넘겨준다.
> > - key에 해당하는 문자열이 template에서 사용 가능한 변수명이 된다.
>
> #### Filters
>
> > ```django
> > {{ variable|filter }}
> > 
> > ex)
> > {{ name|lower }} # name변수를 소문자로 출력
> > {{ foods|join:', '}} # foods의 변수들을 이어서 출력
> > 
> > # 체인이 가능 (필터를 여러개 사용 가능) 변수|필터|필터
> > 
> > ```
> >
> > - 표시할 변수를 수정할 때 사용
>
> #### Tags
>
> > ```django
> > {% tag %}
> > 
> > # 일부 태그는 시작과 종료 태그가 필요
> > {% if %}{% endif %}
> > <ul>
> >   {% for food in foods %}
> >     <li>{{ food }}</li>
> >   {% endfor %}
> > </ul>
> > ```
>
> #### Comments
>
> > ```django
> > {# 한줄짜리 주석 #}
> > 
> > {% comment %}
> > 여러줄짜리 주석
> > {% endcomment %}
> > ```
> >
> > 



### Template inheritance (템플릿 상속)

> - 사이트의 공통 요소를 포함하고 하위 템플릿이 재정의(override) 할 수 있는 기본 skeleton 템플릿을 만든다.
>
> #### tags
>
> >  ```django
> >  {% extends '' %}
> >  ```
> >
> > - 자식 템플릿이 부모 템플릿을 확장함(상속받음)을 알림
> > - 반드시 템플릿 최상단에 작성
> >
> > ```django
> > {% block content %}
> > {% endblock %}
> > ```
> >
> > - 하위 템플릿에서 override할 수 있는 블록을 정의
> >
> > ```django
> > {% include '_nav.html' %}
> > ```
> >
> > - 특정 코드만 뜯어내 사용 가능
> > - 언더바 `_` 는 반드시 써야하는 것은 아니지만 관용적 표현
>
> #### settings.py
>
> ```python
> TEMPLATES = [
>     {
>         'BACKEND': 'django.template.backends.django.DjangoTemplates',
>         'DIRS': [BASE_DIR / 'templates', ],
>         'APP_DIRS': True,
>         'OPTIONS': {
>             'context_processors': [
>                 'django.template.context_processors.debug',
>                 'django.template.context_processors.request',
>                 'django.contrib.auth.context_processors.auth',
>                 'django.contrib.messages.context_processors.messages',
>             ],
>         },
>     },
> ]
> # DIRS에 템플릿 추가 경로를 추가
> # BASE_DIR 은 프로젝트를 포함하는 최상단 폴더
> ```
>
> 
>



## HTML Form

### HTML "form" element

> - 웹에서 사용자로부터 입력받은 데이터를 서버로 전송하는 역할
> - text, button, checkbox, file, hidden, image, password, radio, reset, submit 등
>   - `action` : 입력 데이터가 전송될 URL
>     - 앞에 아무것도 붙이지 않으면 현재 page 경로 + 
>     - `/` 를 앞에 붙이면 메인 url +
>   - `method` : 입력 데이터 전달 방식 지정

### HTML "input" element

> - 사용자로부터 데이터를 입력받기 위해 사용
> - `type` 속성에 따라 동작 방식이 달라진다
>   - `name` : 중복 가능, 양식 제출 시 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음. 변수 명과 비슷

### HTML "label" element

> - 사용자 인터페이스 항목에 대한 설명
> - input의 `id` 속성과 동일한 값의 `for` 속성 필요



### HTTP

> - HyperText Transfer Protocal
> - HTTP request method 종류
>   - GET, POST, PUT, DELETE...
>   - Django에서는 GET/POST 만 지원
>
>  #### GET
>
> > - 서버로부터 정보를 조회
> > - 데이터를 가져올 때만 사용
> > - body가 아닌 Query String Parameters를 통해 전송
> >   - 주소로 데이터가 전달되는 형태
> >   - 누구에게나 데이터가 노출되는 형태이므로 중요 데이터는 POST로 전달
> > - 서버에 요청을 하면 HTML 문서를 받는 데, 이 때 요청의 방식이 GET
>
> #### POST
>
> > - DB와 작업을 할 때
> > - 생성, 수정, 삭제



## URL

> - 앱마다 urls를 따로 분류하여 관리

### Variable Routing

> - URL 주소를 변수로 사용하는 것.
> - URL 주소 일부를 변수로 views에서 사용가능
>
> ```python
> # urls.py
> path('appname/<str:username>/', views.profile)
> 
> 
> # views.py
> def profile(request, username):
>     context = {
>         'username': username
>     }
>     return render(request, 'profile.html', context)
> ```
>
> - 사용가능한 자료형
>   - str: `/` d을 제외하고 비어있지 않은 모든 문자열
>   - int: 0 또는 양의 정수
>   - slug : 하이픈, 밑줄이 포함된 문자열

### Naming URL patterns

> ```python
> # urls.py
> path('index/', vies.index, name='index')
> ```
>
> ```django
> <form action="{% url 'index' %}"" method="GET">
> </form>
>                                               
> url 태그를 이용해서 입력받은 인자를 보낼수도 있다.                                            
> <a href="{% url 'articles:index' article.pk %}">index</a>
> ```
>

### NameSpace

> ```python
> # urls.py
> 
> app_name = 'articles'
> urlpatterns = [
>  path('index/', views.index, name='index'),
> ]
> ```
>
> ```django
> {# index.html #}
> 
> {% include 'articles/_nav.html' %}
> 
> {% extends 'base.html' %}
> 
> {% block content %}
> <a href="{% url 'articles:index' %}">index</a>
> 
> {% endblock content %}
> 
> 
> ```
>
> - url 태그를 사용할 때 app_name:url_name 으로 사용
> - include 도 동일
> - app/templates/app/html 의 구조를 지님
>
> 

### Static files

> ```django
> {% load static %}
> 
> <img src="{% static 'app/example.jpg' %}" alt="image name">
> 
> ```
>
> - static 파일은 앱 내부의 static 폴더에 저장.
> - app/static/app/파일 의 구조를 지님
> - built-in 이 아니기 때문에 load를 이용해 불러온 후 사용 (import와 비슷)
>
> #### STATICFILES_DIRS
>
> > ```python
> > # settings.py
> > STATICFILES_DIRS = [
> >     BASE_DIR / 'static', 
> > ]
> > ```
> >
> > - 추가적인 static 파일 경로 지정
>
> #### STATIC_URL
>
> > ```python
> > STATIC_URL = '/static/'
> > ```
> >
> > - 정적 파일을 참조할 때 사용하는 URL
> > - 실제 파일이나 디렉토리가 아닌, URL로만 존재
> > - 비어있지 않은 값일 경우 `/`로 끝나야 함
>
> #### STATIC_ROOT
>
> > - django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
> > - settings.py의 DEBUG 값이 True 일 경우 작용하지 않는다.
