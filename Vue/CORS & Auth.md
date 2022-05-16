## CORS & Auth

### CORS

> #### SOP (Same-origin policy)
>
> > - 동일 출처 정책
> > - 다른 출처에서 가져온 리소스와 상호작용을 제한
> > - protocol, Port, Host가 모두 같아야 동일한 출처
>
> #### CORS (Cross-Origin Resource Sharing)
>
> > - 교차 출처 리소스 공유
> > - 추가 HTTP header를 통해 다른 출처의 자원에 접근 가능한 권한 부여
> > - 리소스 상호작용을 막는 것은 브라우저 이지만, 서버에서 CORS 응답을 보내야 처리 가능
> >   - 서버에서 해결한다.
> >
> > ```bash
> > pip install django-cors-headers
> > ```
> >
> > ```python
> > INSTALLED_APPS = [
> > ...
> > 'corsheaders',
> > ...
> > ]
> > 
> > MIDDLEWARE = [
> > ...,
> > 'corsheaders.middleware.CorsMiddleware',  # CommonMiddleware 보다 반드시 위에 작성
> > 'django.middleware.common.CommonMiddleware',  # 원래 있음
> > ...,
> > ]
> > 
> > CORS_ALLOWED_ORIGINS = [
> > "https://domain.com",
> > "https://api.domain.com",
> > "http://localhost:8080",
> > "http://127.0.0.1:9000"
> > ]
> > ```



### Authentication & Authorization

> #### Authentication
>
> > - 사용자가 **누구**인가?
>
> #### Authrization
>
> > - 특정 리소스, 기능에 대해 **접근 권한**을 가지고 있는가?
> > - 일반 사용자와 admin의 차이
>
> ```bash
> pip install dj-rest-auth
> ```
>
> ```python
> INSTALLED_APPS = [
>     ...,
>     'rest_framework',
>     'rest_framework.authtoken',
>     ...,
>     'dj_rest_auth'
>     'django.contrib.sites',
>     'allauth',
>     'allauth.account',
>     'dj_rest_auth.registration',
>     
>     'allauth.socialaccount',
>     'allauth.socialaccount.providers.facebook',
>     'allauth.socialaccount.providers.twitter',
> ]
> SITE_ID = 1
> ```
>
> ```python
> urlpatterns = [
>     ...,
>     path('dj-rest-auth/', include('dj_rest_auth.urls')), 
>     path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), 
> ]
> ```
>
> ```bash
> python manage.py migrate
> ```
>
> 





1. Vue에서 로그인 - id/pw
2. django에서 사용자 확인
3. django에서 토큰 정보 생성 후 DB(토큰 테이블)에 저장
4. django에서 토큰 데이터 리턴
5. Vue에서 토큰 정보를 받아 local Storage에 저장



6. 글 1번의 데이터 가져오기 - 서버(django)에 요청
7. 사용자 확인 - 토큰이 없으면 허용 X
   1. 토큰이 없으면 401 Unauthorized 에러
   2. 토큰을 헤더에 넣어서 요청하면, 토큰 테이블에 존재 확인 후 정상 데이터를 리턴
8. 