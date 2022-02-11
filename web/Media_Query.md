# Media Query



## 웹페이지 레이아웃

> - 고정폭 레이아웃
>   - 브라우저의 크기가 변화해도 컨텐츠 변화 없음
> - 유동적 레이아웃
>   - 화면을 줄이면 이미지, 크기 글씨 등의 영역이 유동적으로 변화
> - 별도의 사이트
>   - 디바이스에 따라 별도의 사이트(도메인)으로 구분
> - 반응형 레이아웃: 
>   - 하나의 사이트에서 디바이스의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법
>   - 미디어 쿼리를 활용해서 CSS 작성



### 미디어 쿼리(Media Query)

> - `@media`를 활용하여 CSS에서 반응형 레이아웃을 작성
>
>  ```css
>  @media (orientation: landscape) {
>      /* 가로모드: 너비 > 높이 */
>  }
>  
>  @media (orientation: portrait) {
>      /* 가로모드: 너비 < 높이 */
>  }
>  
>  @media only print {
>      /* 인쇄할때만 적용할 스타일 */
>      * {
>          color: black;
>      }
>  }
>  
>  @media (width: 300px) {
>      /* 특정 너비에서만 가능, 1px만 넘거나 줄어도 적용안됨 */
>  }
>  
>  @media (min-width: 700px) {
>      /* 700px 이상 */
>  }
>  @media (max-width: 600px) {
>      /* 600px 이하 */
>  }
>  
>  @media (max-height: 500px) and (max-width: 500px){
>      /* and 조건 가능 */
>  }
>  @media (max-height: 500px), (max-width: 500px) {
>      /* or 조건 가능 */
>  }
>  ```
>
> 





<br>



 ### BEM(Block Element Modifier) 방법론

> - Block
>   - `.block`
> - Element
>   - Block의 구성요소
>   - `.block__elem`
> - Modifier
>   - Block이나 Element의 속성
>   - 색깔, 
>   - `.block__elem--modifier`



<br>

