## Custom User Model

### AUTH_User_Model

> - User를 나타나는데 사용하는 모델
> - 프로젝트가 진행되는 동안 **변경 불가**
> - migrations 및 migrate 이전 설정 필요
>
> ```python
> # accounts/models.py
> from django.contrib.auth.models import AbstractUser
> 
> class User(AbstractUser):
>     pass
> ```
>
> ```python
> # settings.py
> AUTH_USER_MODEL = 'accounts.User'
> ```
>
>  ```python
>  # accounts/admin.py
>  from django.contrib import admin
>  from django.contrib.auth.admin import UserAdmin
>  from .models import User
>  
>  admin.site.register(User, UserAdmin)
>  ```
>
> 
>
>  
>
> #### 초기화 방법
>
> > 1. db.sqlite3 파일 삭제
> >
> > 2. migrations 파일 중 파일명에 숫자가 붙은 파일들 모두 삭제
> >
> > 3. ```bash
> >    python manage.py makemigrations
> >    python manage.py migrate
> >    ```





