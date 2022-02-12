# Web

> [HTML](#html)
>
> [CSS](#css)



<br>



## HTML & CSS

### 현재의 웹 표준

> #### W3G
>
> - HTML5
> - 현재는 표준을 정하는 일에서 밀려남
>
> #### WHATWG
>
> - HTML Living Standard
> - 현재 웹 표준을 정함
> - 애플, 구글, 마소, Mozilla

### Can I use

> - 브라우저 버전 별 지원하는 요소들을 보여주는 사이트

---



<br>

<br>



## HTML

> [HTML](#html)
>
> [HTML 기본 구조](#html-기본-구조)
>
> [HTML 문서 구조화](#html-문서-구조화)



<br>



### HTML

>#### HTML
>
>- Hyper Text Markup Language
>- 웹 페이지를 구조화하기 위한 언어
>- Web의 뼈대를 만들기 위한 언어
>
>#### Hyper Text
>
>- 참조(하이퍼링크)를 포함하는 텍스트
>- 사용자가 한 문서에서 다른 문서로 즉시 접근 가능한 텍스트
>
>#### Markup Language
>
>- 태그를 이용해 문서나 데이터의 구조를 명시하는 언어
>- 예시: HTML, Markdown



<br>



### HTML 기본 구조

>#### HTML 기본 구조
>
>> - html: 문서의 최상위(root) 요소
>> - head: 문서의 메타데이터 요소
>>   > - html 정보
>>   > - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
>>   > - 정보에 대한 내용이므로 일반적으로 브라우저에 표현되지 않음
>> - body: 문서 본문 요소
>>   
>>   > - 실제 화면에 보이는 내용들
>>
>> ```html
>> <!DOCTYPE html> 
>> <!-- 해당 문서가 html5로 구성되어 있음을 알려주는 역할 -->
>> <!-- 최신 문서에서는 필요 없지만 하위 버전 호환을 위해 필요 -->
>> 
>> <html lang="ko">
>> # lang 기본값은 en
>> 
>>     <haed>
>>         # html 정보
>>         # 보이지 않는 문서에 대한 정보
>>         <meta charset="UTF-8">
>>         <title>Document</title>
>> 
>>     </haed>
>>     <body>
>>         # 실제로 보이는 영역
>>     </body>
>> </html>
>> ```
>
>#### head
>
>> - `<title>` : 브라우저 상단 타이틀
>> - `<meta>` : 문서 레벨 메타데이터 요소
>>   - html 문서의 정보를 담당
>> - `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
>> - `<script>` : 스크립트 요소 (JavaScript 파일/코드)
>> - `<style>` : CSS 직접 작성
>
>#### Open Graph Protocol
>
>> - 메타 데이터를 표현하는 새로운 규약
>> - 페이스북(메타)에서 만듬
>> - 유튜브 미리보기, 이미지 등에서도 사용
>> - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
>> - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
>
>#### DOM(Document Object Model) 트리
>
>> - HTML 문서를 브라우저에서 렌더링 하기 위한 구조
>> - 부모/자식 요소로 구분
>> - 같은 단게의 경우 형제 요소
>> - 들여쓰기는 2 space
>>
>> ```html
>> <body>
>>   <h1> 문서 </h1>
>>   <ul>
>>     <li>HTML</li>
>>     <li>CSS</li>
>>   </ul>
>> </body>
>> ```
>
>#### 요소(element)
>
>> - 태그 `<>` `</>`와 내용(contents)로 구성되어 있다.
>> - 태그는 내용을 감싸며, 정보의 성격과 의미를 정의
>> - 내용이 없는 태그들: 닫히는 태그가 없다.
>>   - `br`(개행), `hr`(수평선), `img`, `input`, `link`, `meta`
>>   - `<hr/>` 처럼 표현하기도 함
>>   
>> - 요소는 중첩(nested)될 수 있음 (여러번 사용할 수 있음)
>> - 태그 쌍이 제대로 되지 않아도 에러 없이 깨져서 출력됨
>
>#### 속성(attribute)
>
>> - 열리는 태그 안에 속성을 작성
>> - 모든 요소는 속성을 가질 수 있다.
>> - 이름과 값이 하나의 쌍으로 존재
>> - `<여는태그 속성명="속성값"></닫는태그>`
>> - 경로나 크기 등 태그의 부가적인 정보 설정
>> - 태그별로 사용가능한 속성이 다르다.
>> - 태그와 상관없이 사용 가능한 속성(HTML Global Attribute) 존재
>>
>> ```html
>> <a href="http://~~~"></a>
>> # herf: 속성명, "http://~~": 속성값
>> # 속성명="속성값"에서 띄어쓰기 X, 쌍따옴표 사용
>> ```
>>
>> 
>
>#### HTML Global Attribute
>
>> - `id` : 문서 전체에서 유일한 고유 식별자 지정
>> - `class` : 공백으로 구분된 해당 요소의 클래스 목록 (CSS, JS에서 요소 선택, 접근)
>> - `data-*` : 페이지에 개인 사용자 정의 데이터 저장
>> - `style` : inline 스타일. 해당 요소를 꾸밀때 사용
>> - `title` : 요소에 대한 추가 정보 지정
>>   - `<title>` 타이틀 태그와는 다름
>> - `tabindex` : 요소의 탭 순서
>
>#### 시맨틱 태그
>
>> - HTML5에서 의미론적 요소를 담은 태그
>>   - 영역을 구분짓고 싶을 때는 `div` 태그 사용했지만 특정 의미는 없었음
>>   
>> - 태그 목록
>>   > - `header` : 문서 전체나 섹션의 헤더(머리말)
>>   > - `nav` : 네비게이션(상단 메뉴)
>>   > - `aside` : 사이드 공간. 메인 콘텐츠와 관련성이 적은 콘텐츠
>>   > - `section` : 문서의 일반적 구분 콘텐츠의 그룹 표현
>>   > - `article` : 사이트 내에서 독립적으로 구분되는 영역
>>   > - `footer` : 문서 전체나 섹션의 푸터(꼬리말)
>>   
>> - Non semantic 요소는 `div`, `span` 등. `h1`, `table` 도 시맨트 태그의 일종
>>
>> - 검색 엔진 등에 의미 있는 정보의 그룹을 태그로 표현에도 사용
>>
>> - 단순히 구역 구분이 아닌 '의미'를 가지는 태그들의 활용
>>
>> - 코드의 가독성 상승, 쉬운 유지보수
>>
>> - 검색엔진최적화(SEO)를 위해 메타태그, 시멘틱 태그의 활용 필요



<br>



### HTML 문서 구조화

>#### 인라인 / 블록 요소
>
> > 
>
>#### 텍스트 요소 - 인라인
>
> > ```html
> > <a></a> <!-- href 속성을 활용해서 하이퍼링크 생성 -->
> > 
> > <b></b> <!-- 굵은 글씨 요소 -->
> > <strong></strong> <!-- 시멘틱 태그. 굵은 요소 중 강조 -->
> > 
> > <i></i> <!-- 기울임 글씨 요소 -->
> > <em></em> <!-- 시멘틱 요소, 기울임 중 강조 -->
> > 
> > <br> <!-- 줄 바꿈 -->
> > 
> > <img> <!-- src 속성을 활용하여 이미지 표현 -->
> > 
> > <span></span> <!-- 의미 없는 인라인 컨테이너, 문장 중 텍스트 -->
> > ```
>
>#### 그룹 컨텐츠 - 블록
>
> > ```html
> > <p></p> <!-- 하나의 문단 (paragraph) -->
> > <hr> <!-- 문단 레벨 요소에서 주제의 분리 , 수평선 -->
> > 
> > <ol></ol> <!-- 순서 있는 리스트 (ordered) -->
> > <ul></ul> <!-- 순서 없는 리스트 (unordered) -->
> > 
> > <pre></pre> <!-- 작성한 내용을 그대로 표현. 고정폭 글꼴, 공백문자 유지 -->
> > <blockquote> <!-- 텍스트가 긴 인용문, 들여쓰기 -->
> > </blockquote>
> > 
> > <div></div> <!-- 의미 없는 블록 레벨 컨테이너 -->
> > ```
>
>#### table
>
> > - `<thead>` `<tbody>` `<tfoot>` 로 상단 중단 하단을 나눔
> > - `<tr>` 로 가로줄 구성 table row
> > - `<thead>` 에서는 `<th>`로 셀을 구분
> > - `<tbody>`, `<tfoot>` 에서는 `<td>` 로 셀을 구분
> > - `colspan`, `rowspan` 속성으로 셀 병합
> > - `<caption>` 으로 표 설명, 제목
>
>#### form
>
> > - 데이터를 서버에 제출하기 위한 영역
> >
> > - `<form>` 기본 속성
> >
> >   > - `action` : form을 처리할 서버의 URL
> >   >   - "abc" : 현재 접속 중인 주소 /abc
> >   >   - "/abc" : main domain/abc
> >   > - `method` : form을 제출할 때 사용할 HTTP 메서드 (GET or POST)
> >   > - `enctype` : method가 post인 경우 데이터의 유형
> >   >   - application/x-www-form-urlencorded : 기본값
> >   >   - multipart/form-data : 파일 전송시 (input type이 file인 경우), 이미지나 비디오
> >   >   - text/plain: HTML5 디버깅용
>
>#### input
>
> > - 다양한 타입의 입력데이터 유형과 위젯
> >
> > - `<input>`의 속성
> >
> >   > - `name` : form control에 적용되는 이름
> >   > - `value` : form control에 적용되는 값
> >   > - `required`, `readonly`, `autofocus`, `autocomplete`, `disabled` 등
>
>#### input label
>
> > - label을 클릭하여 input을 활성화 시킬 수 있음
> > - `<input>` id 속성과 `<label>` for 속성을 일치시킨다
> > - 사용자의 선택 영역 증가로 웹 / 모바일(터치) 환경에서 편의성 증가
> > - 화면리더기에서도 활용
>
>#### input 유형
>
> > - `text` : 일반 텍스트
> > - `password` : 입력 시 값이 보이지 않고 `*`로 표현
> > - `email` : 이메일 형식이 아닌 경우 form 제출 불가
> > - `number` : min, max, step 속성으로 숫자 범위 설정 가능
> > - `file` : 컴퓨터 내 파일 선택 가능
> > - `checkbox` : 다중 선택, 선택 항목에 대해 value 지정 필요
> > - `radio` : 단일 선택, 선택 항목에 대해 value 지정 필요
> > - `color` : 색상 선택
> > - `date` : 날짜 선택
> > - `submit` : value에 제출 버튼안에 내용이 들어간다.
>
>#### markup
>
> > - header
> > - section
> > - footer
>
>

---





<br>

<br>





## CSS

> [CSS](#css란)
>
> [CSS Selectors](#css-selectors)
>
> [CSS 기본 스타일](#css-기본-스타일)
>
> [Selector 심화](#selector-심화)
>
> [CSS Box model](#css-box-model)
>
> [CSS Display](#css-display)
>
> [CSS Position](#css-position)



### CSS란?

>#### CSS
>
> > - Cascading Style Sheets
> > - 스타일을 지정하기 위한 언어
>
>#### CSS 구문 - 용어 정리
>
> > ```html
> > h1 { 		<!-- h1: 선택자 -->
> >   color: blue;   <!-- ; : 선언(Declaration) -->
> >   font-size: 15px;   <!-- 속성(Property): 값(value);-->
> > }
> > ```
>
>#### CSS 정의 방법
>
> > - 인라인(inline) : 해당 태그에 직접 style 적용
> > - 내부참조(embedding) - `<style>` 태그를 이용. 유지보수가 어려워 디버깅이나 간단한 style에 사용
> > - 외부 참조(link file) - 분리된 CSS 파일. `<head>` 내 `<link>` 를 통해 불러온다.



<br>



### CSS Selectors

> #### 선택자(Selector) 유형
>
> > - 기본 선택자
> >
> >   > - 전체 , 요소 선택자
> >   >
> >   > ```css
> >   > /* 전체 선택자: 별표(*) */
> >   > * {
> >   >     color: red;
> >   > }
> >   > 
> >   > /* 요소 선택자 태그 */
> >   > h2 {
> >   >     color: orange;
> >   > }
> >   > 
> >   > h3, h4 {  /* 여러 요소를 선택하고 싶을 대는 콤마(,) 이용*/
> >   >     font-size: 10px;
> >   > }
> >   > ```
> >   >
> >   > - 클래스, 아이디, 속성 선택자
> >   >
> >   > ```css
> >   > /* 클래스 선택자 마침표(.) */
> >   > .green {
> >   >     color: green;
> >   > }
> >   > 
> >   > /* id 선택자 샾(#) */
> >   > #purple {
> >   >     color: purple;
> >   > }
> >   > ```
> >
> > - 결합자(Combinators)
> >
> >   > - 자손, 자식 결합자
> >   > - 일반 형제,  인접 형제 결합자
> >
> > - 의사 클래스/요소(Pseudo Class)
> >
> >   > - 링크, 동적 의사 클래스
> >   > - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
>
> #### CSS 적용 우선순위 (cascading order)
>
> > 1. 중요도(Importance)
> >    - !important
> > 2. 우선순위 (Specificity)
> >    - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element > 전체
> > 3. CSS 파일 로딩 순서 (가장 마지막을 선택)
>
> #### CSS 상속
>
> > - 부모 요소의 텍스트 관련 속성을 자식에게 상속
> > - 상속 되는 것
> >   - Text 관련 요소 (font, color, text-align), opacity, visibility 등
> > - 상속되지 않는 것
> >   - Box model (width, height, margin, padding ...)
> >   - position (position, top/right/bottom/left, z-index ...)



<br>



### CSS 기본 스타일

>#### 크기 단위
>
> >- px (픽셀)
> >   - 모니터 해상도의 한 화소인 픽셀
> >   - 고정적인 단위
> >- %
> >   - 백분율 단위
> >   - 가변적 레이아웃
> >   - 부모 요소에 대해 상속 영향
> >
> >- em
> >   - 배수단위
> >   - 부모 요소에 대해 상속 영향
> >- rem
> >   - 최상위 요소의 사이즈 기준으로 배수
> >   - 부모 요소에 대해 상속 영향 X
> >- viewport
> >   - 브라우저 크기
> >   - 디바이스의 viewport를 기준
>
>#### 색상 단위
>
> > - 색상 키워드
> >   - 대소문자 구분 X
> >   - red, blue 등 특정 색을 글자로 나타냄
> > - RGB 색상
> >   - `#`  + 16진수
> >   - rgb( , , ) 표현법
> >   - rgba 에서 a는 alpha(투명도)
> >   - hsl( , , ) 색상, 채도, 명도 
>
>#### CSS 문서 표현
>
> > - 텍스트 서체, 자간, 단어 간격, 행간, 들여쓰기 등
> > - 컬러, 배경색
> > - 태그별 스타일링: 목록, 표



<br>

### Selector 심화

>#### 결합자(Combinators)
>
> > - 자손 결합자
> >   - 하위의 모든 요소
> >   - `li p` : 띄어쓰기
> > - 자식 결합자
> >   - 바로 아래의 요소
> >   - `li > p` : `>`
> > - 일반 형제 결합자
> >   - 뒤에 위치하는 모든 형제 요소
> >   - `li ~ p`  : `~`
> > - 인접 형제 결합자
> >   - 바로 뒤의 형제 요소
> >   - `li + p` : `+`



<br>



### CSS Box model

>#### CSS 원칙 1 - Normal Flow
>
> > - 모든 요소는 네모(박스모델)이고,
> > - 위에서부터 아래로,
> > - 왼쪽에서 오른쪽으로 쌓인다.
>
> #### Box model
>
> > - 모든 HTML 요소는 bot 형태로 되어있음
> >
> > - 하나의 박스는 네 영역으로 이루어진다.
> >
> >   > - content: 실제로 값이 들어있는 영역
> >   > - padding: 테두리 안 여백
> >   > - border: 테두리
> >   > - margin: 테두리 밖 여백, 배경색 지정 불가
> >
> >  ```css
> >  .margin {
> >    margin-top: 10px;
> >    margin-right: 20px;
> >    margin-bottom: 30px;
> >    margin-left: 40px;
> >  }
> >  .margin-1 {
> >    margin: 10px /* 상하좌우 */
> >  }
> >  .margin-2 {
> >    margin: 10px 20px /* 수직(상하) 수평(좌우) */
> >  }
> >  .margin-3 {
> >    margin: 10px 20px 30px /* 상 중 하 */
> >  }
> >  .margin-4 {
> >    margin: 10px 20px 30px 40px /* 상우하좌 시계방향 */
> >  }
> >  
> >  .margin-padding {
> >    margin: 10px;
> >    padding: 30px;
> >  }
> >  
> >  .border {
> >    border-width: 3px;
> >    border-style: dashed;
> >    border-color: black;
> >  }
> >  .border {
> >    border: 3px dashed black;
> >  }
> >  ```
>
>#### box-sizing
>
>> ```css
>> box-sizing: border-box;  /* 기본값은 content-box */
>> /* 테두리를 기준으로 바뀜 */
>> /* content-box의 경우 width 설정 시 content영역만 설정 */
>> /* border-box의 경우 width 값이 content + 2*padding + 2*border값으로 변환 */
>> ```



<br>



### CSS Display

> #### CSS 원칙2
> > 
> > - 1원칙: 모든 요소는 네모(박스모델)이고, 좌측 상단에 배치.
> > - 2원칙: display에 따라 크기와 배치가 달라진다.
> > 
> #### display
> > 
> > - display: block
> > 
> >   > - 줄바꿈이 일어나는 요소
> >   > - 화면 크기 전체의 가로 폭 차지
> >   > - block 요소 안에 inline 요소가 들어갈 수 있다.
> >   > - div / ul, ol, li, p, hr, form 등
> > 
> > - display: inline
> > 
> >   > - 줄 바꿈이 일어나지 않는 행의 일부 요소
> >   > - 텍스트 관련 요소들
> >   > - content 너비만큼 가로 폭을 차지
> >   > - width, height, margin-top, margin-bottom을 지정할 수 없다.
> >   > - 상하 여백은 line-height로 지정
> >   > - span / a / img / input, label / b, em, i, strong 등
> > 
> > - display: inline-block
> > 
> >   > - block과 inline 레벨 요소 특징을 모두 가진다
> >   > - inline 처럼 한 줄에 표시 가능, block 처럼 width, height, margin 속성 지정 가능
> > 
> > - display: none
> > 
> >   > - 해당 요소를 화면에 표시하지 않고, 공간도 부여하지 않음
> >   > - visibility: hidden의 경우 표시는 하지 않지만 공간은 부여함.
>
>#### 수평 정렬
>
> > - ```css
> >   /* 왼쪽 정렬 */
> >   margin-right: auto;
> >   text-align: left;
> >   ```
> >
> > - ```css
> >   /* 오른쪽 정렬 */
> >   margin-left: auto;
> >   text-align: right;
> >   ```
> >
> > - ```css
> >   /* 가운데 정렬 */
> >   margin-right: auto;
> >   margin-left: auto;
> >   text-align: center;
> >   ```

 

<br>



### CSS position

> #### CSS position
>
> > - 문서 상에서 요소의 위치를 지정
> > 
> > - static
> >
> >   > - 기본값
> >   > - Normal Flow
> >   > - 부모 요소 내에서 배치될 경우 부모 요소의 위치를 기준
> >
> > - top, bottom, left, right를 사용하여 이동 가능
> >
> > - relative : 상대 위치
> >
> >   > - Normal Flow 유지
> >   > - 자기 자신의 static 위치를 기준으로 이동
> >   > - 레이아웃에서 차지하는 공간은 static과 같다.
> >
> > - absolute : 절대 위치
> >
> >   > - Normal Flow 유지 X - 레이아웃 공간 차지 X
> >   > - **static이 아닌** 부모/조상 요소를 기준으로 이동
> >   > - static이 없는 경우 body 태그를 기준으로 이동
> >
> > - fixed : 고정 위치
> >
> >   > - Normal Flow 유지 X - 레이아웃 공간 차지 X
> >   > - 부모 요소와 관계없이 viewport를 기준으로 이동
> >   > - 스크롤을 해도 같은 위치
> >
> > - sticky : 상대적 고정위치
> >
> >   > - 스크롤을 내려서 보기 전까지 relative
> >   > - 보기 시작하면 부모 영역 내에서 fixed와 같이 동작
 >
---





<br>



