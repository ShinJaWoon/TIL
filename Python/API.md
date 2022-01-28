# 외부데이터, API 수집

## 웹 스크래핑

| 클라이언트 | 프로토콜 | 서버          |
| ---------- | -------- | ------------- |
| 요청       | 연결     | 응답          |
| 검색       | HTTP     | HTML, JSON... |



### 요청

>`pip install requests`
>
>```python
>import requests
>
>URL = 'https://www.naver.com/'
>
>response = requests.get(URL)
># type = <class requests.model.Requests>
># response(200) <= 성공적으로 가져왔다는 뜻
># response(404) <= 에러, 본인 잘못
># response(500) <= 개발자 잘못
>
>response = requests.get(URL).txt
># type = <class 'str'>
>```



<br>



### BeautifulSoup

>- HTML과 XML의 데이터를 가져오는 파이썬 라이브러리
>- `pip install beautifulsoup4`
>- `페이지 우클릭`->`검사`->`selector 복사`
>
>```python
>from bs4 import BeautifulSoup
>
>data = BeautifulSoup(response, 'html.parser')
># type = <class 'bs5.BeautifulSoup'>
>
>data2 = data.select_one('selector 경로')
>print(data2.txt)
>```



<br>



## API

### API

>- API (Applilcation Programming Interface)
>- 컴퓨터나 컴퓨터 프로그램 사이의 연결
>- 일종의 소프트웨어 인터페이스
>- 다른 종류의 소프트웨어에 서비스를 제공
>- 사용법을 기술하는 문서, 표준 => API사양 / 명세(specification)
>
>```python
>import requests
>
>BASE_URL =  'https://A.B.com/C/'
>path = '/D/F'
># path에 {}가 들어간 경우 f-string. path parameter가 필요
>params = {
>    'api_key': '1234',
>    'region': 'KR',
>    'language': 'ko'
>}
>
>response = requests.get(BASE_URL+path, params=params)
>
>print(response.status_code, response.url)
>data = response.json()
>print(data)
>```
>
>



### JSON

> ```python
> import requests
> 
> # 1번 방법 ===============================
> URL = 'https://api.agify.io?name=michael'
> response = requests.get(URL).json()
> 
> # 2번 방법 ================================
> URL = 'https://api.agify.io'
> 
> params = {
>     'name': 'michael'
> }
> 
> # 요청
> response = requests.get(URL, params=params).json()
> print(response.get('age'))
> 
> ```