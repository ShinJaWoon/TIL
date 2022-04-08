### Django View Decorators

> ```python
> from django.views.decorators.http import require_http_methods, require_safe, require_POST
> 
> 
> # 허용 외의 method에 대해 405 에러를 발생시킴
> @require_safe  # GET만 허용
> @require_POST   # POST만 허용
> @require_http_methods(['GET', 'POST'])
> ```
>
> 

### Media files

> #### Model field
>
> > ##### ImageField()
> >
> > - FileFiled()를 상속받음
> > - 최대길이 100자 문자열 (주소를 저장)
> > - max_length 인자를 통해 최대 길이 수정 가능
> >
> > ##### FileField()
> >
> > - 파일 업로드에 사용
> > - 2개의 선택 인자
> >   - upload_to
> >   - starage
> >
> > ```bash
> > pip install Pillow
> > pip freeze > requirements.txt
> > ```
> >
> > ```python
> > # models.py
> > image = models.IamgeField(upload_to='images/', blank=True)
> > # blank의 경우 빈 값이라도 가능하도록(이미지를 올리지 않아도 되도록) 함
> > 
> > upload = models.FileField(upload_to='uploads/')
> > upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
> > 
> > def articles_image_path(instance, filename):
> >     return f'image_{instance.pk}/{filename}'
> > image = models.IamgeField(upload_to=articles_image_path)
> > ```
> >
> > ```python
> > # settings.py
> > MEDIA_ROOT = BASE_DIR / 'media'
> > MEDIA_URL = '/media/'
> > ```
> >
> > ```python
> > # urls.py
> > from django.conf import settings
> > from django.conf.urls.static import static
> > 
> > urlpatterns = [
> >     # ... the rest of your URLconf goes here ...
> > ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
> > ```
>
> #### 이미지 업로드
>
> > ```django
> > <form action="" method="POST" enctype="multipart/form-data">
> >   {% csrf_token %}
> > 
> >   {% bootstrap_form form %}
> >   {% if request.resolver_match.url_name == 'create' %}
> >     <button class="btn btn-primary">CREATE</button>
> >   {% elif request.resolver_match.url_name == 'update' %}
> >     <button class="btn btn-primary">UPDATE</button>
> >   {% endif %}
> >   
> > </form>
> > ```
> >
> > ```python
> > # views.py
> > def create(request):
> >     if request.method == 'POST':
> >         form = ArticleForm(request.POST, request.FILES)
> >         #form = ArticleForm(request.POST, files=request.FILES)
> >         if form.is_valid():
> >             article = form.save()
> >             return redirect('articles:detail', article.pk)
> >     else:
> >         form = ArticleForm()
> > 
> >     context = {
> >         'form': form
> >     }
> >     return render(request, 'articles/form.html', context)
> > ```
> >
> > ```django
> > {# 이미지 url 사용법 #}
> > {% if article.image %}
> >   <img src="{{ article.image.url }}" alt="{{ article.image }}">
> > {% endif %}
> > ```
>
> #### 이미지 Resizing
>
> > ```bash
> > pip install django-imagekit
> > pip freeze > requirements.txt
> > ```
> >
> > ```python
> > # settings.py
> > INSTALLED_APPS = [
> >  ..
> >  'imagekit', 
> >  ..
> > 
> > ]
> > ```
> >
> > ```python
> > # models.py
> > from imagekit.models import ProcessedImageField
> > from imagekit.processors import Thumbnail
> > 
> > image = ProcessedImageField(
> >     blank=True,
> >     upload_to='thumbnails/',
> >     processors=[Tumbnail(100, 50)],
> >     format='JPEG',
> >     options={'quality': 60}
> > )
> > 
> > ```
> >
> > 