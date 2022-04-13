## Foreign Key

### ForeignKey

> - 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
>
> #### Foreign Key model
>
> > ```python
> > # articles/models.py
> > class Comment(models.Model):
> >        article = models.ForeignKey(Article, on_delete=models.CASCADE)
> >        content = models.CharField(max_length=200)
> >        created_at = models.DateTimeField(auto_now_add=True)
> >        updated_at = models.DateTimeField(auto_now=True)
> >     
> >        def __str__(self):
> >            return self.content
> >     
> > ```
> >
> > - ForeignKey field는 1. 참조하는 모델클래스, 2. on_delete 인자 2개를 가진다.
> > - on_delete : 외래 키가 참조하는 객체가 사라졌을 경우, 처리 방법을 정의
> >   - cascade: : 상위 삭제시 하위도 삭제
> >   - protect :  하위가 있을 경우 상위 삭제 불가
> >   - restrict : restrict로 지정된 관계는 상위에서 삭제가 안되지만 상위의 상위가 restrict가 아니라면 삭제 가능.
> >   - set_null
> >   - set_Default
> > - related_name : 역참조시 사용할 이름
>
> #### Migration
>
> > ```bash
> > python manage.py makemigrations
> > python manage.py migrate
> > ```



#### Comment CRUD

> #### CREATE
>
> > ```python
> > # articles/forms.py
> > from .models import Article, Comment
> > 
> > class CommentForm(forms.ModelForm):
> >     
> >        class Meta:
> >            model = Comment
> >            exclude = ('article', )
> >            # fields = ('content',)
> > ```
> >
> > ```python
> > # articles/urs.py
> > app_name = 'articles'
> > urlpatterns = [
> >        path('<int:pk>/comments/', views.comments_create, name='comments_create')
> > ]
> > ```
> >
> > ```django
> > {# articles/detail.html #}
> > 
> > <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
> >     {% csrf_token %}
> >     {{ comment_form }}
> >     <input type="submit">
> > </form>
> > ```
> >
> > ```python
> > from .forms import ArticleForm, CommentForm
> > 
> > @require_POST
> > def comments_create(request, pk):
> >        if request.user.is_authenticated:
> >            article = get_object_or_404(Article, pk=pk)
> >            comment_form = CommentForm(request.POST)
> >            if comment_form.is_valid():
> >                comment = comment_form.save(commit=False)
> >                comment.article = article
> >                comment.save()
> >            return redirect('articles:detail', article.pk)
> >        return redirect('accounts:login')
> > 
> > ```
> >
> > 
>
> #### READ
>
> > ```python
> > # articles/views.py
> > from .models import Article, Comment
> > 
> > @require_safe
> > def detail(request, pk):
> >     article = get_object_or_404(Article, pk=pk)
> >     comment_form = CommentForm()
> >     # 조회한 article의 모든 댓글을 조회(역참조)
> >     comments = article.comment_set.all()
> >     context = {
> >         'article': article,
> >         'comment_form': comment_form,
> >         'comments': comments,
> >     }
> >     return render(request, 'articles/detail.html', context)
> > ```
> >
> > ```django
> > <ul>
> >  {% for comment in comments %}
> >    <li>
> >      {{ comment.content }}
> >    </li>
> >  {% endfor %}
> > </ul>
> > ```
> >
> > - 댓글 개수 
> >
> >   ```django
> >   {{ comments|length }}
> >   {{ article.comment_set.all|length }}
> >   {{ comments.count }}
> >   {% for comment in comments %}
> >   
> >   {% empty %}
> >   
> >   {% emdfor %}
> >
> > 
>
> #### DELETE
>
> > ```python
> > # articles/urs.py
> > app_name = 'articles'
> > urlpatterns = [
> >        path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
> > ]
> > ```
> >
> > ```python
> > # articles/views.py
> > @require_POST
> > def comment_delete(request, article_pk ,comment_pk):
> >       if request.user.is_authenticated:
> >           comment = get_object_or_404(Comment, pk=comment_pk)
> >           comment.delete()
> >       return redirect('articles:detail', article_pk)
> > 
> > ```
> >
> > ```django
> > <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
> >   {% csrf_token %}
> >   <input type="submit" value="삭제">
> > </form>
> > ```
> >
> > 



### 데이터 무결성

> - 데이터의 정확성과 일관성을 유지하고 보증하는 것
>
> 1. 개체 무결성 (Entity integrity)
>    - 모든 테이블이 PK를 가지고, PK로 선택된 열은 고유한 값, 빈 값은 허용 X
>
> 2. 참조 무결성 (Referential integrity)
>    - FK 값이 데이터베이스의 특정 테이블의 PK를 참조한다.
>
> 3. 범위(도메인) 무결성 ( Domain integrity)
>    - 정의된 형식(범위)에서 관계형 데이터베이스의 모든 컬럼이 선언되도록 규정