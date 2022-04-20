## REST API

### HTTP

> #### HTTP
>
> > - HyperText Transfer Protocol
> > - 웹 상에서 컨텐츠를 전송하기 위한 약속
> > - HTML 문서와 같은 리소스를 가져올 수 있도록 하는 프로토콜(규칙, 약속)
> > - 웹에서 이루어지는 모든 데이터 교환의 기초(요청, 응답)
> > - 특성
> >   - Stateless
> >   - Connectionless
> > - 쿠키와 세션을 통해 서버 상태를 요청하고 연결한다
>
> #### HTTP request methods
>
> > - 주어진 리소스에 대한 수행하고자 하는 동작을 정의
> >
> > - GET, POST, PUT, DELETE
>
> #### HTTP response status code
>
> > 1. (1xx) Informational responses
> > 2. (2xx) Successful responses
> > 3. (3xx) Redirection responses
> > 4. (4xx) Client error responses
> > 5. (5xx) Server error responses
>
> #### URI
>
> > - Uniform Resource Identifier
> > - 통합 자원 식별자
> > - 인터넷의 자원을 식별하는 유일한 주소 / 자원 식별과 이름지정에 사용되는 간단한 문자열
> >
> > #### URL
> >
> > > - Uniform Resource Locator
> > > - 통합 자원 위치
> > > - 네트워크 상 리소스의 위치를 알려주기 위한 약속
> >
> > #### URN
> >
> > > - Uniform Resource Name
> > > - 통합 자원 이름
> > > - URL과는 달리 자원의 위치에 영향을 받지 않는 유일한 이름
> > > - ex) ISBN (국제표준도서번호
> >
> > #### URI 구조
> >
> > > ##### Scheme (protocol)
> > >
> > > > - 브라우저가 사용해야 하는 프로토콜
> > > > - **http(s)**, data, fiel, ftp, mailto
> > > > - https://www.example.com:80/path/to/myfile.html/?key=value#quick-start
> > > > - **https://**www.example.com:80/path/to/myfile.html/?key=value#quick-start
> > >
> > > ##### Host (Domain name)
> > >
> > > > - 요청을 받는 웹 서버의 이름
> > > >
> > > > - IP 주소를 직접 사용도 가능하지만 불편하므로 자주 사용되지는 않는다.
> > > > - https://**www.example.com**:80/path/to/myfile.html/?key=value#quick-start
> > >
> > > ##### Port
> > >
> > > > - 웹 서버상 특정 리소스에 접근하는데 사용되는 gate
> > > > - HTTP 프로토콜 표준 포트
> > > >   - HTTP 80
> > > >   - HTTPS 443
> > > > - https://www.example.com**:80**/path/to/myfile.html/?key=value#quick-start
> > >
> > > ##### Path
> > >
> > > > - 웹 서버상 리소스 경로
> > > > - 초기에는 실제 파일의 물리적 위치였으나, 현재는 실제 위치가 아닌 추상척 형태 구조
> > > > - https://www.example.com:80**/path/to/myfile.html**/?key=value#quick-start
> > >
> > > ##### Query (Identifier)
> > >
> > > > - 웹 서버에 제공되는 추가적인 매개 변수
> > > > - & 로 구분되는 key-value
> > > > - https://www.example.com:80/path/to/myfile.html**/?key=value**#quick-start
> > >
> > > ##### Fragment
> > >
> > > > - Anchor
> > > > - 리소스 안에서 북마크의 한 종류
> > > > - 문서의 특정 부분으로 바로 이동
> > > > - 서버가 아닌 브라우저가 해석하는 내용
> > > > - https://www.example.com:80/path/to/myfile.html/?key=value**#quick-start**



### RESTful API

> #### API
>
> > - Application Programming Interface
> > - 프로그래밍 언어가 제공하는 기능을 수행할 수 있도록 만든 인터페이스
> > - App과 프로그램으로 소통하기 위한 방법
> > - Web API의 경우 다른 서비스에 요청을 보내고 응답을 받기 위한 명세
> > - 응답 데이터 타입
> >   - HTML, XML, JSON 등
>
> #### REST
>
> > - REpresentational State Transfer
> > - API 서버를 개발하기 위한 소프트웨어 설계 방법론
> > - 리소스를 정의하고 리소스에 대한 주소를 지정하는 방법
> > - REST 원리를 따르는 시스템을 RESTful 이라 지칭
>
> #### REST 자원과 주소의 지정 방법
>
> > - 자원, 정보 - URI
> > - 행위 - HTTP Method (GET, POST, PUT, DELETE) - (C, R, U, D)
> > - 표현 - JSON
>
> #### JSON
>
> > - JavaScript의 표기법을 따른 단순 문자열
> > - 사람이 읽고 쓰기 쉽다.
> > - 기계가 해석, 분석하기 쉽다.
> > - key-value 구조 : 파이썬 dictionary, 자바스크립트 object와 같이 C 계열 언어가 갖고 있는 자료구조
>
> 

### Response

> #### Serialization
>
> > - 직렬화
> > - 데이터 구조나 객체 상태를 동일/다른 컴퓨터 환경에 저장하고, 나중에 재구할 할 수 있는 포맷으로 변환하는 과정
> > - 데이터를 json과 같은 다른 유형으로 쉽게 변환할 수 있도록 데이터를 변환하는 중간 과정
>
> 
>
> ```python
> from rest_framework.decorators import api_view
> from rest_framework.response import Response
> from django.shortcuts import render
> from django.http.response import JsonResponse, HttpResponse
> from django.core import serializers
> from .serializers import ArticleSerializer
> from .models import Article
> 
> # 딕셔너리를 json으로 제공, 직렬화를 하려면 safe=False
> def article_json_1(request):
>     articles = Article.objects.all()
>     articles_json = []
> 
>     for article in articles:
>         articles_json.append(
>             {
>                 'id': article.pk,
>                 'title': article.title,
>                 'content': article.content,
>                 'created_at': article.created_at,
>                 'updated_at': article.updated_at,
>             }
>         )
>     return JsonResponse(articles_json, safe=False)
> 
> 
> 
> # Serialization 사용
> def article_json_2(request):
>     articles = Article.objects.all()
>     data = serializers.serialize('json', articles)
>     return HttpResponse(data, content_type='application/json')
> 
> 
> # DRF (Django REST famework) 라이브러리를 사용
> # many=True의 경우 단일 객체가 아닐 때 사용하는 옵션. 기본 False
> # @api_view(['GET'])
> @api_view()
> def article_json_3(request):
>     articles = Article.objects.all()
>     serializer = ArticleSerializer(articles, many=True)
>     return Response(serializer.data)
> 
> ```
>
> ```python
> # articles/serializers.py
> from rest_framework import serializers
> from .models import Article
> 
> 
> class ArticleSerializer(serializers.ModelSerializer):
> 
>     class Meta:
>         model = Article
>         fields = '__all__'
> 
> ```

### DRF

> - Django REST Framework
> - Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
> - ModelForm과 유사함

