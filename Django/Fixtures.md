## Fixtures

### dumpdata

> ```bash
> python manage.py seed <앱이름> --number=<만들 데이터 개수>
> ```
>
>  ```bash
>  python manage.py seed articles --number=10
>  ```
>
> 
>
> ```bash
> python manage.py dumpdata --indent 4 <앱 이름>.<모델 이름> > <만들json파일이름>.json
> ```
>
> ```bash
> python manage.py dumpdata --indent 4 articles.article > articles.json
> python manage.py dumpdata --indent 4 articles.comment > comments.json
> python manage.py dumpdata --indent 4 accounts.user > users.json
> ```
>
> 

### loaddata

> - app/fixtures/ 다음 경로를 입력
>
> ```bash
> python manage.py loaddata <json 경로> <json2 경로> <json3 경로>
> ```
>
> ```bash
> python manage.py loaddata articles.json comments.json users.json
> python manage.py loaddata articles/articles.json articles/comments.json accounts/users.json
> ```
>
> 





## Qeury

> ```python
> from django.db.models import Count
> 
> articles = Article.objects.annotate(Count('comment')).order_by('-pk')
> ```
>
> 
>
> ```python
> # 1:N에서 N을 부를 때
> articles = Article.objects.select_related('user').ordeer_by('-pk')
> 
> # 1:N에서 1을 부를 때
> articles = Article.objects.prefetch_related('comment_set').ordeer_by('-pk')
> ```
>
> 
>
> ```python
> # M:N 관계
> 
> from django.db.models import Prefetch
> 
> articles = Article.objects.prefetch_related(
> 	Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
> ).order_by('-pk')
> ```
>
> 