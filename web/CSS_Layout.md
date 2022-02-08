# CSS Layout

[CSS Layout](#css-layout)

[Bootstrap](#bootstrap)



<br>



## CSS Layout

[Float](#float)

[Flexbox](#flexbox)

[grid](#gird)



<br>



### Float

>  #### Float
>
> > - 박스를 왼쪽, 혹은 오른쪽으로 이동시켜 인라인 요소들이 주변을 wrapping
> > - 워드에서 그림 옆에 글자가 오게 하는 것과 비슷
> > - 요소가 Normal flow를 벗어나도록 함
>
>  #### Float 속성
>
> > - `none` : 기본값
> > - `left` : 요소를 왼쪽으로 띄움
> > - `right` : 요소를 오른쪽으로 띄움
>
> #### Clearing Float
>
> > - float 요소의 **부모 요소**에게 clearfix 클래스를 설정하고 사용
> > - 각 float 요소는 Normal Flow를 벗어나기 때문에 다른 block들과 겹칠 수 있는 것을 방지
> >
> >  ```css
> >  .clearfix:after {
> >      content: "";
> >      display: block;
> >      clear: both;
> >  }
> >  ```
> >
> > - `:after` : 요소의 맨 마지막 자식으로 가상 요소를 하나 생성



<br>



### Flexbox

>  #### CSS Flexible Box Layout
>
> - **메인 축**을 기준으로 행과 열 형태의 **1차원** 레이아웃 모델
> - main axis, cross axis로 메인, 교차 축으로 나뉜다.
> - 수직 정렬이나 내부 아이템의 너비, 높이, 간격을 동일하게 배치할 수 있다.
>
>  #### Flexbox 구성요소
>
> - Flex Container (부모 요소)
>   - Flex item들이 놓여있는 영역
>   - `display: flex;`  또는 `display: inline-flex;` 로 지정
> - Flex Item (자식 요소)
>   - Container에 들어 있는 컨텐츠
>
>  #### Flex 속성
>
> > - `flex-direction` : Main axis 기준 방향 설정
> >
> >   ``` css
> >   flex-direction: row;
> >   |123		|
> >   flex-direction: row-reverse;
> >   |		 321|
> >   flex-direction: column;
> >   --
> >   1
> >   2
> >   3
> >   
> >   --
> >   flex-direction: column-reverse;
> >   --
> >   
> >   3
> >   2
> >   1
> >   --
> >   ```
> >
> > - `flex-wrap` : 아이템이 컨테이너 내부에 위치하도록 설정
> >
> >   ```css
> >   flex-wrap: wrap; /* 한줄이 넘어가면 다음 줄에 배치 */
> >   |1 2 3|
> >   |4 5  |
> >   flex-wrap: nowrap; /* 기본값, 한줄에 배치*/
> >   |12345|
> >   ```
> >
> > - `flex-flow` : flex-direction 과 wrap을 축약형
> >
> > - `justify-content` : Main axis를 기준으로 공간을 배분, 배치
> >
> >   ```css
> >   justify-content: flex-start;
> >   |123						|
> >   justify-content: flex-end;
> >   |						123|
> >   justify-content: center;
> >   |			123			|
> >   justify-content: space-between;  /* 요소 사이에만 */
> >   |1			2			3|
> >   justify-content: space-around;  /* 요소+앞뒤 여유공간 */
> >   | 1    2    3    4    5 |
> >   justify-content: space-evenly;
> >   |  1  2  3  4  5  |
> >   ```
> >
> > - `align-content` : Cross axix를 기준으로 공간배분 - justify-content와 동일 방식
> >
> >   ```css
> >   align-content: flex-start;
> >   |1  2|
> >   |3   |
> >   |    |
> >   align-content: flex-end;
> >   |    |
> >   |1  2|
> >   |3   |
> >   align-content: center;
> >   |    |
> >   |1  2|
> >   |3   |
> >   |    |
> >   align-content: space-between;  /* 요소 사이에만 */
> >   |1  2|
> >   |    |
> >   |    |
> >   |3   |
> >   align-content: space-around;  /* 요소+앞뒤 여유공간 */
> >   |    |
> >   |1  2|
> >   |    |
> >   |    |
> >   |3   |
> >   |    |
> >   align-content: space-evenly;
> >   |    |
> >   |1  2|
> >   |    |
> >   |3   |
> >   |    |
> >   ```
> >
> > - `align-items` : 모든 아이템을 Cross axis를 기준으로 정렬
> >
> >   ```css
> >   align-items: stretch; /* 세로로 꽉 채움 */
> >   |1 2 3|
> >   |1 2 3|
> >   |1 2 3|
> >   align-items: flex-start;
> >   |1 2 3|
> >   |     |
> >   |     |
> >   align-items: flex-end;
> >   |     |
> >   |     |
> >   |1 2 3|
> >   align-items: center;
> >   |     |
> >   |1 2 3|
> >   |     |
> >   align-items: baseline; /* 가운데 맞춤 */
> >   |1    |
> >   |1 2  |
> >   |1 2 3|
> >   |1 2  |
> >   |1    |
> >   ```
> >
> > - `align-self` : 개별 아이템을 Cross axis를 기준으로 정렬
> >
> > - `flex-grow` : 남은 영역을 아이템에 분배
> >
> > - `order` : 배치 순서
> >
> > - `shrink` : 넘친 영역을 축소배분
> >
> > - `basis` : 초기 크기 설정. 넘으면 넘긴대로 늘림
> >
> > - `flex: grow shrink basis` : grow shrink basis 간략화
> >
> >  ※ 가운데 배치
> >
> >  ```css
> >  .container {
> >      display: flex;
> >      justify-content: center;
> >      align-items: center;
> >  }
> >  ```
> >
> > 

---





<br>

<br>



## Bootstrap

> - 기본적인 CSS 설정을 해둔 것

> [CDN](#cdn)
>
> [utility](#utility)
>
> [Grid System](#grid-system)





<br>



### CDN

> - Content Delivery(Distribution) Network
> - CSS, JS, Image, Text 등의 컨텐츠들을 가까운 서버에서 전달 받아 사용하는 것.
>
> ```html
> <!-- head -->
> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
> 
> <!-- </body> 바로 전에 위치 -->
> <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
> ```
>
> 





<br>



### utility

> #### spacing
>
> > | 기호 | 뜻      |
> > | ---- | ------- |
> > | m    | margin  |
> > | p    | padding |
> >
> > | 기호 | 뜻          |
> > | ---- | ----------- |
> > | t    | top         |
> > | b    | bottom      |
> > | s    | left        |
> > | e    | right       |
> > | x    | left, right |
> > | y    | top, bottom |
> >
> > | number | rem  | px   |
> > | ------ | ---- | ---- |
> > | 1      | 0.25 | 4    |
> > | 2      | 0.5  | 8    |
> > | 3      | 1    | 16   |
> > | 4      | 1.5  | 24   |
> > | 5      | 3    | 48   |
>
> #### color
>
> > ```css
> > --primary: 파랑
> > --secondary: 회색
> > --success: 초록
> > --info: 하늘
> > --warning: 노랑
> > --danger: 빨강
> > --light: 흰색
> > --dark: 검정
> >     
> > /* 예시 */
> > class="text-primary"  /* 글자색 */
> > class="bg-primary"    /* 배경색 */
> > 
> > ```
>
> #### Display
>
> > ```css
> > .d-inline  /* display: inline */
> > .d-block  /* display: block */
> > 
> > .d-none  /* 숨김 */
> > .d-block  /* 모두 표시 */
> > /* 디스플레이 크기 */
> > xs (extra small) < sm (small) < md (medium) < lg (large) < xl (extra large) < xxl (extra extra large)
> > .d-xs-none .d-sm-block /* xs에서만 숨김 */
> > .d-block .d-sm-none  /* xs에서만 표시 */
> > .d-none .d-sm-block .d-md-none  /* sm에서만 볼 수 있음 */
> > ```
> >
> > 



<br>



### Grid system

> - 요소들의 디자인과 배치를 돕는 시스템
> - 기본 요소
>   - Column : 컨텐츠를 포함
>   - Gutter : 칼럼과 칼럼 사이 공간
>   - Container : Column을 담는 공간
>
> #### Bootstrap grid system
>
> > - flexbox로 제작됨
> > - container, rows, columns 로 컨텐츠를 배치, 정렬
> > - 12개의 column, 6개의 grid breakpoints
> >
> >  ```css
> >  <div class="row">
> >    <div class="box col-1">1</div>
> >    <div class="box col-1">1</div>
> >    <div class="box col-1">1</div>
> >  
> >    <!-- xs 2개, 그다음 3개, 그다음 4개 -->
> >    <!-- 12/n 개로 생각해야함!!!! -->
> >    <div class="box col-6 col-sm-4 col-md-3">1</div>
> >  </div>
> >  
> >  
> >  <!-- nesting -->
> >  <div class="row">
> >    <div class="box col-6">1</div>
> >      <div class="row">
> >        <div class="box col-3">1</div>
> >        <div class="box col-3">1</div>
> >        <div class="box col-3">1</div>
> >        <div class="box col-3">1</div>
> >      </div>
> >    </div>
> >    <div class="box col-6">1</div>
> >    <div class="box col-6">1</div>
> >    <div class="box col-6">1</div>
> >  </div>
> >  
> >  <!-- offset -->
> >  <div class="row">
> >    <div class="box col-md-4 offset-4">1</div>
> >  </div>
> >  
> >  ```
>
> 

---

