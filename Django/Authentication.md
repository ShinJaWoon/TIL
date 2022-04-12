## Authentication System

> - Django에서 기본적으로 제공하는 시스템
> - 인증 (Authentication) 과 권한(Authorization)을 함께 제공
>   - 인증: 사용자가 누구인지 신원 확인
>   - 권한: 인증된 사용자가 수행할 수 있는 작업을 결정



### Authentication System

> #### 두번째 앱 (accounts) 생성
>
> ```bash
> python manage.py startapp accounts
> ```
>
> ```python
> # settings.py
> 
> INSTALLED_APPS = [
>     'articles',
>     'acoounts', 
> ```
>
> ```python
> # project/urls.py
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     path('articles/', include('articles.urls')),
>     path('accounts/', include('accounts.urls')), 
> ]
> 
> ```
>
> ```python
> # accounts/ursl.py
> from django.urls import path
> from . import views
> 
> app_name = 'accounts'
> urlpatterns = [
>     
> ]
> ```
>
> 

### 쿠기와 세션

> #### HTTP
>
> > - 비연결지향 (connectionless) 
> >   - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
> > - 무상태(stateless)
> >   - 연결을 끊는 순간 클라이언트와 서버 간 통신이 끝난다.
> >   - 상태 정보 유지 X (매번 요청을 보낼 때 로그인이 필요)
> > - 클라이언트와 서버간 지속적 관계를 위해 쿠기와 세션을 사용
>
> #### 쿠키
>
> > - 클라이언트가 웹사이트를 방문할 경우, 웹사이트의 서버를 통해 사용자의 컴퓨터의 설치되는 작은 기록정보 파일
> >   - KEY-VALUE 데이터 형식
> >   - 소프트웨어가 아니므로 프로그램처럼 실행 불가 -> 악성코드 설치 불가
> >   - 단, 행동 추적이나 쿠키를 훔쳐 계정 접근 권한 획득 가능
> > - HTTP 쿠키는 상태가 있는 세션을 만든다.
> > - 최초 웹페이지 방문 시 쿠키를 저장, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 전송
> >
> > ##### 사용 목적
> >
> > > - 세션 관리 (Session management)
> > >   - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 관리
> > > - 개인화 (Personalization)
> > >   - 사용자 선호, 테마 등의 설정
> > > - 트래킹 (Tracking)
> > >   - 사용자 행동을 기록 및 분석
> >
> > ##### 수명
> >
> > > - Session cookies
> > >   - 세션 종료 시 삭제
> > >   - 브라우저가 현재 세션이 종료된느 시기를 정의
> > >   - 일부 브라우저는 세션 복원을 통해 쿠키 지속시간을 연장
> > > - Persistent cookies
> > >   - Expieres 속성에 지정된 날짜 혹은 Max-Age 속성에 저장된 기간이 지나면 삭제
>
> #### 세션
>
> > - 사이트와 특정 브라우저 사이의 **상태**를 유지
> > - 클라이언트가 서버에 접속 시 서버가 특정 session id를 발급, 클라이언트는 session id를 쿠키에 저장
> > - ID는 세션 구별에 사용, 쿠키에는 ID만 저장
> > - Django의 세션은 미들웨어(HTTP 요청과 응답 처리 중간의 시스템)를 통해 구현
> >   - 미들웨어 - 데이터관리, 애플리케이션 서비스 ,메이징, 인증 및 API

### 로그인

> - 세션을 생성하는 로직
>
> ```bash
> python manage.py createsuperuser
> ```
>
> 
>
> ```python
> # urls.py
> from django.urls import path
> from . import views
> 
> app_name = 'accounts'
> urlpatterns = [
>     path('login/', views.login, name='login'),
> ]
> ```
>
> ```django
> {% comment %} login.html {% endcomment %}
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1>로그인</h1>
>   <hr>
>   <form action="{% url 'accounts:login' %}" method="POST">
>     {% csrf_token %}
>     {{ form.as_p }}
>     <input type="submit">
>   </form>
>   <a href="{% url 'articles:index' %}">back</a>
> {% endblock content %}
> 
> ```
>
> ```python
> # views.py
> from django.shortcuts import redirect, render
> from django.contrib.auth import login as auth_login
> from django.contrib.auth.forms import AuthenticationForm
> 
> # Create your views here.
> 
> def login(request):
>     if request.method == 'POST':
>         form = AuthenticationForm(request, request.POST)
>         # 로그인
>         if form.is_valid():
>             auth_login(request, form.get_user())
>             return redirect('articles:index')
>     else:
>         form = AuthenticationForm()
>     context = {
>         'form': form, 
>     }
>     return render(request, 'accounts/login.html', context)
> ```
>
> 

### 로그인 템플릿

> ```django
> {{ user }}
> AnonymousUser 와 로그인한 유저 id를 나타냄
> 
> {{ request.user.is_authenticated }}
> 로그인 상태를 확인
> ```



### 로그아웃

> ```python
> #urls.py
> urlpatterns = [
>     path('logout/', views.logout, name='logout'),
> ]
> ```
>
> ```python
> # views.py
> from django.shortcuts import redirect, render
> from django.contrib.auth import login as auth_login
> from django.contrib.auth import logout as auth_logout
> from django.views.decorators.http import require_http_methods, require_POST
> from django.contrib.auth.forms import AuthenticationForm
> 
> @require_POST
> def logout(request):
>     auth_logout(request)
>     return redirect('articles:index')
> ```
>
> ```django
> {% extends 'base.html' %}
> 
> {% block content %}
>   <h1>로그인</h1>
>   <hr>
>   <form action="{% url 'accounts:login' %}" method="POST">
>     {% csrf_token %}
>     {{ form.as_p }}
>     <input type="submit">
>   </form>
>   <a href="{% url 'articles:index' %}">back</a>
> {% endblock content %}
> 
> ```

### 

### 접근 제한

> #### is_authenticated
>
> ```python
> # views.py
> from django.shortcuts import redirect, render
> from django.contrib.auth import login as auth_login
> from django.contrib.auth import logout as auth_logout
> from django.views.decorators.http import require_http_methods, require_POST
> from django.contrib.auth.forms import AuthenticationForm
> 
> 
> @require_http_methods(['GET', 'POST'])
> def login(request):
>  if request.user.is_authenticated:
>      return redirect('articles:index')
>  if request.method == 'POST':
>      form = AuthenticationForm(request, request.POST)
>      # 로그인
>      if form.is_valid():
>          auth_login(request, form.get_user())
>          return redirect('articles:index')
>  else:
>      form = AuthenticationForm()
>  context = {
>      'form': form, 
>  }
>  return render(request, 'accounts/login.html', context)
> 
> 
> @require_POST
> def logout(request):
>  if request.user.is_authenticated:
>      auth_logout(request)
>  return redirect('articles:index')
> 
> ```
>
> ```django
>  {% if request.user.is_authenticated %}
>    <h3>Hello, {{ user }}</h3>
>    <form action="{% url 'accounts:logout' %}" method="POST">
>      {% csrf_token %}
>      <button>logout</button>
>    </form>
>  {% else %}
>   <a href="{% url 'accounts:login' %}">login</a>
>  {% endif %}
> ```
>
> #### login_required (decorator)
>
> ```python
> # views.py
> from django.contrib.auth.decorators import login_required
> 
> @login_required
> @require_http_methods(['GET', 'POST'])
> def create(request):
> ```
>
> - 로그인이 되어있지 않으면  settings.LOGIN_URL에 설정된 값으로 redirect
> - 기본 경로는 `/accounts/login`
> - 데코레이터는 2개 이상 사용가능, 위쪽 데코레이터부터 확인
>
> #### next
>
> ```python
> # views.py login
>         if form.is_valid():
>             auth_login(request, form.get_user())
>             return redirect(request.GET.get('next') or 'articles:index')
> ```
>
> ```django
>  <form action="" method="POST">
>     {% csrf_token %}
>     {{ form.as_p }}
>     <input type="submit">
>   </form>
> ```
>
> ```python
> # views.py delete
> @require_POST
> def delete(request, pk):
>     if request.user.is_authenticated:
>         article = get_object_or_404(Article, pk=pk)
>         article.delete()
>     return redirect('articles:index')
> ```
>
> 
>
> - 접근 제한이 걸렸을 때, 로그인 후 해당 페이지로 넘어가게 해준다.
> - form의 action값을 비워야 가능하다.
> - next는 GET 방식이므로 delete의 조건을 달아주어야 한다.

### 회원가입

> ```python
> # urls.py
> urlpatterns = [
>     path('signup/', views.signup, name='signup'),
> ]
> ```
>
> ```python
> def signup(request):
>     if request.method == 'POST':
>         form = UserCreationForm(request.POST)
>         if form.is_valid():
>             form.save()
>             return redirect('articeles:index')
> 
>     else:
>         form = UserCreationForm()
>     context = {
>         'form': form, 
>     }
>     return render(request, 'accounts/signup.html', context)
> ```
>
> #### 회원 가입 후 자동으로 로그인
>
> ```python
> # views.py
> from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
> 
> def signup(request):
>     if request.method == 'POST':
>         form = UserCreationForm(request.POST)
>         if form.is_valid():
>             user = form.save()
>             auth_login(request, user)
>             return redirect('articeles:index')
> 
>     else:
>         form = UserCreationForm()
>     context = {
>         'form': form, 
>     }
>     return render(request, 'accounts/signup.html', context)
> ```
>
> 
>
> 

### 회원탈퇴

> ```python
> # urls.py
> urlpatterns = [
>     path('delete/', views.delete, name='delete'),
> ]
> ```
>
> ```python
> 
> @require_POST
> def delete(request):
>     if request.user.is_authenticated:
>         reqeust.user.delete()
>         auth_logout(request)
>         # 탈퇴하면서 세션 데이터도 지울 경우.
>         # 반드시 탈퇴 후 로그아웃 순으로 처리
>     return redirect('articles:index')
> ```
>
> #### 
>
> ```django
>       <form action="{% url 'accounts:delete' %}" method="POST">
>         {% csrf_token %}
>         <button>회원탈퇴</button>
>       </form>
> ```
>
> 

### 회원정보 수정

> ```python
> # forms.py
> from django.contrib.auth.forms import UserChangeForm
> from django.contrib.auth import get_user_model
> 
> 
> class CustomUserChangeForm(UserChangeForm)
> 
>     class Meta:
>         model = get_user_model()
>         fields = ('email', 'first_name', 'last_name', )
> ```
>
> 
>
> ```python
> # urls.py
> urlpatterns = [
>     path('update/', views.update, name='update'),
> ]
> ```
>
> ```python
> # views.py
> from django.contrib.auth.decorators import login_required
> from .forms import CustomUserChangeForm
> 
> def update(request):
>     if request.method == 'POST':
>         form = UserCreationForm(request.POST, instance=request.user)
>         if form.is_valid():
>             user = form.save()
>             auth_login(request, user)
>             return redirect('articeles:index')
> 
>     else:
>         form = UserCreationForm(instance=request.user)
>     context = {
>         'form': form, 
>     }
>     return render(request, 'accounts/signup.html', context)
> ```

### 비밀번호 변경

> 
>
> ```python
> # urls.py
> urlpatterns = [
>     path('password/', views.change_password, name='change_password'),
> ]
> ```
>
> ```python
> # views.py
> from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
> from django.contrib.auth import update_session_auth_hash
> 
> 
> @login_required
> @require_http_methods(['GET', 'POST'])
> def change_password(request):
>     if request.method == 'POST':
>         form = PasswordChangeForm(request.user, request.POST)
>         if form.is_valid():
>             form.save()
>             update_session_auth_hash(request, form.user)
>             return redirect('articeles:index')
> 
>     else:
>         form = PasswordChangeForm(request.user)
>     context = {
>         'form': form, 
>     }
>     return render(request, 'accounts/signup.html', context)
> ```

### 메세지

> 1. settings.py
>
>    - ```python
>      MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
>      ```
>
> 2. views.py
>
>    - ```python
>      messages.info(request, 'Three credits remain in your account.')
>      ```
>
> 3. django.html
>
>    - ```django
>      {% if messages %}
>      <ul class="messages">
>          {% for message in messages %}
>          <li class="alert alert-{{ message.tags }}">{{ message }}</li>
>          {% endfor %}
>      </ul>
>      {% endif %}
>      ```
>
>    - 
>
> - https://docs.djangoproject.com/en/3.2/ref/contrib/messages/

