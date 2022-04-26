### function

> #### 일급 객체
>
> > - 변수에 할당 가능
> > - 함수의 매개변수로 할당 가능
> > - 함수의 반환 값으로 사용 가능
>
> 
>
> #### 함수 선언식
>
> > ```javascript
> > function 함수이름(매개변수) {
> >     
> > }
> > ```
> >
> > - 익명 함수 불가능
> > - 호이스팅 O
>
> 
>
> #### 함수 표현식
>
> > ```javascript
> > const 함수이름 = function (매개변수) {
> >     
> > }
> > ```
> >
> > - 익명 함수 가능
> > - 호이스팅 X
> > - Airbnb Style Guide 권장 방식
>
> 
>
> #### 인자
>
> > -  JS는 매개변수의 개수와 인자의 개수가 **같지 않아도** 에러가 나지 않는다.
> >
> > ##### 기본 인자
> >
> > > ```javascript
> > > const 함수이름 = function (변수 = 기본값) {
> > >     return 변수
> > > }
> > > ```
> > >
> > > - 파이썬의 키워드 인자와 같다.
> >
> > ##### Rest Parameter
> >
> > > ```javascript
> > > const 함수명 = function (arg1, arg2, ...args) {
> > >     
> > > }
> > > ```
> > >
> > > - ...arg에 값이 들어가지 않을 경우 빈 배열 [] 이 들어간다.
> > > - 파이썬의 가변인자 `*args`와 같다.
> >
> > ##### Spread operator
> >
> > > ```javascript
> > > const numbers = [1, 2, 3]
> > > 어떤함수(...numbers)
> > > ```
> > >
> > > - 파이썬의 언패킹 `*` 과 같다.
>
> #### 함수의 타입
>
> > - `typeof` 결과값은 `function`
>
> 



### Arrow Function

> #### 화살표 함수
>
> > - function 키워드 생략 가능
> > - 매개변수가 1개라면 `( )` 생략 가능
> > - 몸통 표현식이 하나라면 `{ }` 과 `return` 생략 가능
> > - return 값이 object 일 경우 `( )`로 묶어줘야 한다.
> >
> > ```javascript
> > const arrow = function (name) {
> >     return `${name}`
> > }
> > 
> > const arrow = name => `${name}`
> > ```
> >
> > 





### 문자열

> #### 메서드
>
> > - `include`: 특정 문자열 존재여부 참/거짓 반환
> > - `split`
> >   - 빈문자열: 기존 문자열을 배열에 담아 반환
> >   -  `''` : 각 문자로 나누어 배열에 담아 반환
> >   - 기타 문자열: 해당 문자열로 나누어 배열에 담아 반환
> > - `replace(from, to)`
> >   - from 값이 존재하면 1개만 to로 교체
> > - `replaceAll(from, to)`
> >   - from 값 전부 to 값으로 교체
> > - `trim`
> >   - 문자열 시작, 끝의 공백(스페이스, 탭, 엔터)를 제거한 문자열 반환
> > - `trimStart()` `trimEnd()`
> >   - 시작 / 끝의 공백문자 제거한 문자열 반환



### 배열

> #### 정의 및 특징
>
> > - 키와 속성들을 담고 있는 참조 타입의 **객체(object)**
> > - 순서를 보장한다.
> > - 대괄호를 이용하여 생성
> > - 0을 포함한 양의 정수 인덱싱
> > - 길이 : `arr.length`
>
> 
>
> #### 메서드
>
> > - `reverse`: 배열 거꾸로
> > - `push` / `pop` : 가장 뒤에 추가 / 제거
> > - `unshift` / `shift` : 가장 앞에 추가 / 제거
> > - `includes` : in
> > - `indexOf` : 없으면 -1, 있으면 인덱스 반환
> > - `join` : 구분자를 이용하여 연결, 없으면 쉼표`,`
>
> ##### Spread operator
>
> > ```javascript
> > const arr = [1, 2, 3]
> > const newArr = [0, ...arr, 4]  // [0, 1, 2, 3, 4]
> > ```
> >
> > - 얕은 복사에 활용 가능
>
> 
>
> #### 배열 순회 메서드
>
> > - `forEach` 
> >
> >   - 배열의 각 요소에 콜백 함수를 한 번씩 실행
> >
> >     - callback 함수: 어떤 함수 내부에서 실행될 목적으로 인자로 넘겨받는 함수
> >
> >   - 반환값(return)이 없는 메서드
> >
> >   - break, continue 사용 불가 - return으로 조절
> >
> >   - ```javascript
> >     arr.forEach((element[, index[, array]]) => {  
> >         
> >     })
> >     // element: 배열 요소, index: 인덱스(선택), array: 배열자체(선택)
> >     
> >     arr.forEach(function (element) {
> >         
> >     })
> >     ```
> >
> > - `map`
> >
> >   - 배열의 각 요소에 대해 콜백 함수를 실행
> >   - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
> >   - 형식은 forEach와 같다.
> >
> > - `filter`
> >
> >   - 배열의 각 요소에 대해 콜백 함수를 실행
> >   - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
> >   - 형식은 forEach와 같다.
> >
> > - `reduce`
> >
> >   - 콜백 함수의 반환 값들을 acc에 누적 후 반환
> >
> >   - ```javascript
> >     arr.reduce((acc, element, [index[, array]])[, initialValue])
> >     ```
> >
> >     ```java
> >     const numbers = [1, 2, 3]
> >     const result = numbers.reduce((acc, num) => {
> >         return acc + num
> >     }, initialValue)
> >     console.log(result) // 6
> >     ```
> >
> > - `find`
> >
> >   - 콜백 함수의 반환 값이 참이면 첫 번째 요소를 반환
> >   - 없으면 undefined
> >
> > - `some`
> >
> >   - 배열 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
> >   - 모든 요소가 통과하지 못하면 거짓 반환
> >   - 빈 배열은 거짓 반환
> >
> > - `every`
> >
> >   - 배열 중 하나라도 주어진 판별 함수를 통과하지 못하면 거짓을 반환
> >   - 모든 요소가 통과하면 참을 반환
> >   - 빈 배열은 참 반환



### 객체 (Objects)

> #### 객체 정의 및 특징
>
> > - 객체는 속성(property)의 집합
> > - 중괄호 내부 key와 value의 쌍으로 표현
> > - key는 문자열 타입만 가능
> >   - 따옴표가 없어도 인식하지만 띄어쓰기 등의 구분자가 있으면 따옴표 사용
> > - 객체 요소 접근은 점`.` 또는 대괄호`[]`로 가능
> >   - 키 이름에 띄어쓰기와 같은 구분자가 있으면 대괄호`[]`만 가능
>
> 
>
> #### 메서드
>
> > - **메서드** 내부에서는 `this` 가 객체를 의미
> >   - key의 value에서는 사용해도 정상작동하지 않는다.
>
> 
>
> #### ES6 문법
>
> > ##### 속성명 축약 (shorthand)
> >
> > > - key와 value의 이름이 같으면 축약 가능
> > >
> > > ```javascript
> > > // ES5
> > > var bookShop = {
> > >     books: books,
> > >     magazines: magazines, 
> > > }
> > > ```
> > >
> > > ```javascript
> > > // ES6
> > > const bookShop = {
> > >     bookss,
> > >     magazines, 
> > > }
> > > ```
> >
> > ##### 메서드명 축약
> >
> > > - 메서드 선언 시 function 키워드 생략 가능
> > >
> > > ```javascript
> > > // ES5
> > > var obj = {
> > >     greeting: function () {
> > >         console.log('Hello')
> > >     }
> > > }
> > > ```
> > >
> > > ```javascript
> > > // ES6
> > > const obj = {
> > >     greeting() {
> > >         console.log('Hello')
> > >     }
> > > }
> > > ```
> >
> > ##### 계산된 속성
> >
> > > - 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
> > > - key를 대괄호`[]`로 감싸서 사용
> > >
> > > ```javascript
> > > const key = 'abc'
> > > const value = ['a', 'b', 'c']
> > > 
> > > const obj = {
> > >     [key]: value, 
> > > }
> > > ```
> >
> > ##### 구조 분해 할당
> >
> > > - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당하는 문법
> > >
> > > ```javascript
> > > const arr = {
> > >     name: 'a', 
> > >     id: 'i', 
> > > }
> > > 
> > > const {name} = arr  // const name = arr.name
> > > const {id} = arr  // const id = arr.id
> > > ```
>
> 
>
> #### JSON
>
> > - `JSON.parse()` : JSON => 객체
> > - `JSON.stringify()` : 객체 => JSON
>
>  
>
> #### this
>
> > - 기본적으로는 최상위 객체 window를 가리킨다.
> > - class 내부 생성자 함수 - 해당 class 객체 (self와 같음)
> > - 메서드 내부 - 해당 메서드가 소속된 객체