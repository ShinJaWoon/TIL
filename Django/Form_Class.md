# Django Form Class

## Django Form Class

### Django forms

> - 외부 공격 및 데이터 손상에 대한 중요 방어 수단
> - 유효성 검사 단순화, 자동화
> - 기능
>   - 렌더링응 위한 데이터 준비 및 재구성
>   - 데이터에 대한 HTML froms 생성
>   - 클라이언트로 받은 데이터 수신 및 처리

### Django 'Form Class'

> - 앱 폴더 안에 `forms.py` 파일 생성
>
> - ```python
>   # forms.py
>   from django import forms
>   
>   class ArticleForm(forms.Form):
>       title = forms.CharField(max_length=10)
>       content = forms.CharField(widget=forms.Text/area)
>   ```
> 
> - ```python
>   # views.py
>   from django.shortcuts import render, redirect
>   from .models import Article
>   from .forms import ArticleForm
> 
>   def new(request):
>       form = ArticleForm()
>       context = {
>           'form': form, 
>       }
>       return render(request, 'articles/new.html', context)
> 
> 
>   # 유효성 검사를 하는 경우
>   def create(request):
>       form = ArticleForm(request.POST)
> 
>       if form.is_valid():
>           article = form.save()
>           return redirect('articles:detail', article.pk)
>       return redirect('articles:new')
>   ```
>
> - ```django
>   {% extends 'base.html' %}
>     
>   {% block content %}
>     <h1>NEW</h1>
>     <hr>
>     <form action="{% url 'articles:create' %}" method="POST">
>       {% csrf_token %}
>
>
>       {{ form.as_p }}
>
>
>     </form>
>     <a href="{% url 'articles:index' %}">back</a>
>   {% endblock content %}
>
>   ```

### Model Form

> - 모델 필드 속성에 맞는 html element를 자동으로 만들어 주고
>
> - 이를 통해 받은 데이터를 view함수에서 유효성 검사를 할 수 있도록 한다.
>
> - ```python
>   # forms.py
>   from django import forms
>   from .models import Article
>       
>   class ArticleForm(forms.ModelForm):
>       
>       class Meta:
>           model = Article
>           fields = '__all__'
>           # exclude = ('title', )
>               
>           # fields와 exclude는 동시에 사용 불가
>   ```
>
> #### is_valid() 유효성 검사
>
> - ```python
>   # 유효성 검사를 하는 경우
>   def create(request):
>       form = ArticleForm(request.POST)
>       
>       # 유효성 검사
>       if form.is_valid():
>           article = form.save()
>           return redirect('articles:detail', article.pk)
>       # print(form.errors)
>       return redirect('articles:new')
>   ```
>
> #### The save() method
>
> - ```python
>   form  = ArticleForm(request.POST)
>       
>   # Create
>   new_articel = form.save()
>       
>   # Update
>   article = Article.objects.get(pk=1)
>   form  = ArticleForm(request.POST, instance=article)
>   form.save()
>   ```
>
> - 데이터베이스 객체를 만들고 저장한다.
>
> - 키워드 인자 instance를 통해 기존 모델 인스턴스를 수정할 수 있음



### form rendering options

> - `as_p()` : 각 필드가 `<p>` 태그로 감싸져서 렌더링
> - `as_ul()` : 각 필드가 `<li>` 태그로 감싸져서 렌더링, `<ul>` 태그는 직접 작성 필요
> - `as_table()` : 각 필드가 `<tr>` 태그로 감싸져서 렌더링, `<table>` 태그는 직접 작성 필요

### HTML input 요소 표현 방법

> 1. Form fields
>    - input에 대해 유효성 검사. 템플릿에서 직접 사용
> 2. Widgets
>    - 웹 페이지의 HTML input 요소 렌더링
>    - 반드시 Form files에 할당
>    - 유효성검사는 하지 않는다.
>
> ```python
> class ArticleForm(forms.ModelForm):
>     title = forms.CharField(
>         widget=forms.TextInput(
>             attrs={
>                 'class': 'my-class', 
>                 'placehoder': 'Enter the title', 
>             }
>         )
>     )
> 
>     content = forms.CharField(
>         widget=forms.Textarea(
>             attrs={
>                 'class': 'my-content', 
>             }
>         ), 
>         error_messages={
>             'required': 'Please enter your content!!!!', 
>         }
>     )
> 
> 
>     class Meta:
>         model = Article
>         fields = '__all__'
> ```
>
> 



### GET과 POST에 따라 다르게 반응

> ```python
> 
> def create(request):
> 
>     if request.method == 'POST':
>         # create
>         form = ArticleForm(request.POST)
> 
>         if form.is_valid():
>             article = form.save()
>             return redirect('articles:detail', article.pk)
>         # print(form.errors)
>     else:
>         # new
>         form = ArticleForm()
>     context = {
>         'form': form,
>     }
>     return render(request, 'articles/create.html', context)
> ```
>
> ```python
> def update(request, pk):
>     article = Article.objects.get(pk=pk)
>     if request.method == 'POST':
>         # update
>         form = ArticleForm(request.POST, instance=article)
>         if form.is_valid():
>             article = form.save()
>             return redirect('articles:detail', article.pk)
>     else:
>         # edit
>         form = ArticleForm(instance=article)
>     context = {
>         'article': article,
>         'form': form,
>     }
>     return render(request, 'articles/update.html', context)
> 
> ```
>
> 

### Rendering fields manually

https://docs.djangoproject.com/en/4.0/topics/forms/#rendering-fields-manually

> - ```django
>   {{ form.title.errors }}
>   {{ form.title.label_tag }}
>   {{ form.title }}
>   ```
>
> - ```django
>   {# 반복문사용 #}
>   {% for field in form %}
>     {{ field.title.errors }}
>     {{ field.title.label_tag }}
>     {{ field.title }}
>   ```

### Django Bootstrap Library

> ```bash
> pip install django-bootstrap-v5
> ```
>
> ```python
> # settings.py
> INSTALLED_APPS = [
>     ..
>     'bootstrap5', 
>     ..
>     
> ]
> ```
>
> ```django
> {% load bootstrap5 %}
> 
> {% bootstrap_css %}
> 
> {% bootstrap_form form.title %}
> 
> {% bootstrap_javascript %}
> ```
>
> 

### 요청에 따른 응답페이지

> ```django
> {% if request.resolver_match.url_name == 'create' %}
>   <h1>CREATE</h1>
> {% elif request.resolver_match.url_name == 'update' %}
>   <h1>UPDATE</h1>
> {% endif %}
> ```
>
> 
