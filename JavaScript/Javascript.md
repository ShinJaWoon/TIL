## JavaScript 기초

### JavaScript의 필요성

> #### 브라우저
>
> > - URL로 웹을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
> >
> > - 웹 브라우저
> >
> > - 브라우저에서 할 수 있는 일
> >
> >   > - DOM 조작 (Document Object Model) 
> >   >   - HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
> >   >   - 문서를 구조화 / 구조화된 구성 요소를 하나의 객체로 취급해서 다루는 논리 트리 모델
> >   >   - 파싱(Parsing) - 구문 분석/해석. 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
> >   > - BOM 조작 (Browser Object Model) 
> >   >   - 자바스크립트가 브라우저와 소통하기 위한 모델
> >   >   - 브라우저 창/프레임을 추상화하여 프로그래밍적으로 제어할 수 있도록 제공하는 수단
> >   >   - 버튼, URL 입력창, 타이틀바 등...
> >   > - JavaScript Core
> >   >   - 브라우저(DOM & BOM)을 조작하기 위한 명령어 (언어)
>
> 
>
> #### JavaScript의 필요성
>
> > - 브라우저 화면을 **동적**으로 만들기 위함
> > - 브라우저를 조작할 수 있는 유일한 언어
> >
> > 

### ECMA Script

> #### ECMA
>
> > - 정보 통신에 대한 표준을 제정하는 비영리 표준화기구
> > - ECMAScript : ECMA-262 (범용적 목적의 프로그래밍 언어에 대한 명세) 규격에 따라 정의한 언어
> >
> > 

### JavaScript 스타일

> #### 세미콜론
>
> > - JS는 세미콜론을 선택적으로 사용 가능
> > - ASI (자동 세미콜론 삽입 규칙)에 의해 자동으로 세미콜론 삽입됨
>
> 
>
> #### 코딩 스타일 가이드
>
> > - 절대적 정답은 없으나, 합의된 원칙과 일관성을 지키는 것이 중요
> > - Airbnb, Google, standardjs 등 여러 코딩 스타일 가이드가 존재
> > - 





### 변수와 식별자

> #### 식별자
>
> > - 문자, 달러 `$` , 밑줄 `_` 로 시작
> > - 대소문자 구분
> > - 클래스명 외에는 모두 소문자 시작
> > - 예약어 (for, if, function... 등 ) 사용 불가
>
> 
>
> ####  식별자 작성 스타일
>
> > - 카멜 케이스 (camelCase)
> >   - 변수, 객체, 함수
> >   - 두번째단어부터 첫글자 대문자
> > - 파스칼 케이스 (PascalCase)
> >   - 클래스, 생성자
> >   - 단어마다 첫글자 대문자
> > - 대문자 스네이크 케이스(SNAKE_CASE)
> >   - 상수
>
> 
>
> #### 변수 선언 키워드
>
> > ##### let
> >
> > > - 재할당 가능
> > > - 변수 **재선언 블가능**
> > > - 블록 스코프
> >
> > ##### const
> >
> > > - **재할당 불가능**
> > > - 변수 **재선언 불가능**
> > > - 블록 스코프
> >
> > ##### var
> >
> > > - 재선언, 재할당 가능
> > > - ES6 이전 변수 선언시 사용했으나, 이후부터는 const와 let 사용 권장
> > > - 함수 스코프
> > > - 호이스팅 특성 : 변수를 선언 이전에 참조할 수 있는 현상
>
> 
>
> #### 스코프
>
> > ##### 블록 스코프
> >
> > > - if, for, 함수 등의 **중괄호 내부**
> > > - 블록 바깥에서 접근 불가능
> >
> > ##### 함수 스코프
> >
> > > - 함수의 **중괄호 내부**
> > > - 함수 바깥에서 접근 불가능
>
> 
>
> #### 선언, 할당, 초기화
>
> > - 선언 (Declaration) 
> >   - 변수를 생성하는 행위 또는 시점
> > - 할당 (Assignment) 
> >   - 선언된 변수에 값을 저장하는 행위 또는 시점
> >   - 변수 조작(append, pop... 등 )과는 다르다.
> > - 초기화 (Initialization) 
> >   - 선언된 변수에 **처음으로** 값을 저장하는 행위 또는 시점



### 데이터 타입

> #### 원시 타입 (Primitive Type)
>
> > - 객체 (object)가 아닌 기본 타입
> >
> > - 변수에 해당 타입의 값이 담긴다.
> >
> > - 다른 변수에 복사할 때 실제 값이 복사된다.
> >
> > - 종류
> >
> >   > ##### 숫자 (Number)
> >   >
> >   > - 정수, 실수 구분이 없는 숫자
> >   > - 부동소수점형식
> >   > - 무한대 (Infinity) 존재
> >   >   - 1/0 -> Infinity
> >   > - NaN (Not-A-Number) : 계산 불가능한 경우
> >   >   - 'asdf' / 100
> >   >
> >   > ##### 문자 (String)
> >   >
> >   > - 텍스트 데이터
> >   >
> >   > - 16비트 유니코드
> >   >
> >   > - 작은 따옴표 `'`, 큰 따옴표 `"` 모두 가능
> >   >
> >   > - 템플릿 리터럴 (Template Literal) 
> >   >
> >   >   - backtick (`)  으로 표현 
> >   >
> >   >   - ${<표현>} 으로 f-string처럼 사용 가능
> >   >
> >   >   - ```javascript
> >   >     `${a} ${b}`
> >   >     ```
> >   >
> >   > ##### undefined
> >   >
> >   > - 변수에 값이 없음을 의도치 않게 사용하게 될 경우
> >   > - 변수 선언 이후 직접 할당하지 않으면 자동으로 undefined 할당
> >   > - 개발자의 의도 없이 할당되지 않은 경우
> >   > - typeof 연산자 결과 : undefined
> >   >
> >   > ##### null
> >   >
> >   > - 변수에 값이 없음을 의도적으로 표현할 때
> >   > - typeof 연산자 결과 : object
> >   >
> >   > ##### Boolean
> >   >
> >   > - 논리적 참 거짓
> >   > - true / false
> >   >
> >   > - 자동 형변환
> >   >
> >   > - | 데이터 타입 | 거짓       | 참               |
> >   >   | ----------- | ---------- | ---------------- |
> >   >   | Undefined   | 항상 거짓  | -                |
> >   >   | Null        | 항상 거짓  | -                |
> >   >   | Number      | 0, -0, NaN | 나머지 모든 경우 |
> >   >   | String      | 빈 문자열  | 나머지 모든 경우 |
> >   >   | Object      | -          | 항상 참          |
> >   >
> >   >   
>
> 
>
> #### 참조 타입 (Reference Type)
>
> > - 객체(object) 타입
> >
> > - 변수에 해당 객체의 참조 값이 담긴다.
> >
> > - 다른 변수에 복사할 대 참조 값이 복사된다.
> >
> > - 종류
> >
> >   > ##### 함수 (Function)
> >   >
> >   > ##### 배열(Arrays)
> >   >
> >   > ##### 객체 (Objects)



### 연산자

> #### 할당 연산자
>
> > `=` 
> >
> > ##### 단축 연산자
> >
> > > `++` : 1 증가
> > >
> > > `--` : 1 감소
> > >
> > > `+=` `-=` `*=`, `/=` : 파이썬과 동일
>
> 
>
> #### 비교 연산자
>
> > ##### 비교 연산자
> >
> > > - `<` `<=` `>` `>=`
> > > - 파이썬과 동일 (boolean 값을 반환)
> > >
> > > - 알파벳끼리 비교할 경우 아스키코드를 비교한 값과 동일
> > >   - 순서상 후순위가 크다
> > >   - 소문자가 대문자보다 크다
> > > - 파이썬 처럼 여러개의 연산자를 동시에 사용 불가 (1 <= n < N 이 아니라 1 <= n && n < N)
> >
> > 
> >
> > ##### `==` 동등 비교 연산자
> >
> > > - 암묵적 타입 변환을 통해 타입을 일치시킨 후 비교
> > > - 1 == true  =>  ture
> > > - 1004 == '1004'  =>  true
> > > - **쓰지 않는다.**
> >
> > ##### `===` 일치 비교 연산자
> >
> > > - 암묵적 타입 변환 발생 X
> > > - 객체끼리 비교할 경우 같은 메모리를 참조하는지 판별
> >
> > ##### 논리 연산자
> >
> > > - `&&` and
> > > - `||` or
> > > - `!` not
> > > - 파이썬과 같이단축평가
> > >   - 1 && 4 => 4 
> > >   - 1 || 4 => 1
> >
> > ##### 삼항 연산자 (Ternary Operator)
> >
> > > - 세 개의 피연산자 사용, 조건에 따라 값을 반환
> > > - 가장 왼쪽 조건식이 참이면 콜론`:` 앞의 값 사용 / 거짓이면 콜론`:` 뒤의 값 사용
> > > - `true ? 1 : 2` => 1
> > > - `false ? 1 : 2` => 2



### 조건문

> #### if statement
>
> > - `if`,  `else if`,  `else`
> >
> > - ```javascript
> >   if (condition) {
> >           
> >   } else if (condition) {
> >           
> >   } else {
> >           
> >   }
> >   ```
>
> #### switch statement
>
> > - expression의 결과값에 따라 case를 나누어 실행
> >
> > - `break`와 `default`는 [선택적]으로 사용 가능
> >
> > - `break`가 없는 경우, 다음 `break`를 만나거나 `default` 만날 때까지 다음 case도 실행시킨다.
> >
> > - ```javascript
> >   switch(expression) {
> >       case 'value1' : {
> >               
> >           [break]
> >       }
> >       case 'value2' : {
> >               
> >           [break]
> >       }
> >       [default: {
> >            
> >       }]
> >   }
> >   ```





### 반복문

> #### while
>
> > ```javascript
> > while (condition) {
> >     
> > }
> > ```
>
> #### for
>
> > - initialization : 최초 반복문 진입 시 1회 실행
> > - condition 매 반복 시행 전 평가
> > - expression : 매 반복 시행 후 평가
> >
> > ```javascript
> > for (initialization; condition; expression) {
> >     
> > }
> > ```
> >
> > ```javascript
> > for (let i = 0; i < 6; i++) {
> >     console.log(i) // 0, 1, 2, 3, 4, 5
> > }
> > ```
>
> #### for ... in
>
> > - 객체(object)의 속성(key)들을 순회할 때 사용
> > - 배열도 순회는 가능하지만 권장하지 않는다.
> >
> > ```javascript
> > for (variable in object) {
> >     
> > }
> > ```
>
> #### for ... of
>
> > - 반복가능한 (iterable) 객체를 순회
> >
> > ```javascript
> > for (variable of iterables) {
> >     
> > }
> > ```
> >
> > 