## Syntax

### Basic syntax

> #### el
>
> > - Vue 인스턴스에 연결할 DOM 요소 필요
> > - CSS 선택자 / HTML Element
> > - new를 이용한 인스턴스 생성시에만 사용
>
> #### data
>
> > - Vue 인스턴스 데이터 객체
> > - Vue tmeplate -보간법  interplation `{{ }}`을 통해 접근 가능
> > - v-bind, v-on과 같은 directive에서 사용 가능
> > - Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능
>
> #### method
>
> > - Vue 인스턴스에 추가할 메서드
> > - Vue tmeplate - interplation `{{ }}`을 통해 접근 가능
> > - v-on과 같은 directive에서 사용 가능
> > - Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능
> > - **화살표 함수는 사용하지 않는다.**
> >   - this를 사용할 수 없기 때문.



### Template Syntax

> #### Interplation (보간법)
>
> > - Text
> >   - `<span> {{ msg }} </span>`
> > - Raw HTML
> >   - `<span v-html="rawHTML"> </span>`
> > - Attributes
> >   - `<span v-bind:id="dynamicId"> </span>`
> > - JS 표현식
> >   - `{{ number+1 }}`
> >   - `{{ message.split('').reverse().join('') }}`
>
> #### Directive
>
> > - v-접두사가 있는 특수 속성
> > - `:` : 전달 인자를 받을 수 있음
> > - `.` : 특수 접미사
> >
> > ##### v-text
> >
> > > - Element의 textContent 업데이트
> > > - interplation 문법은 내부적으로 v-text로 컴파일된다.
> >
> > ##### v-html
> >
> > > - Element의 innerHTML 업데이트
> > > - XSS 공격에 취약
> > > - 사용자로부터 입력받는 내용에는 v-html 절대 사용 금지
> >
> > ##### v-show
> >
> > > - 조건부 렌더링
> > > - 요소는 항상 렌더링되고, DOM에 남아있음
> > > - element에 display CSS 속성을 토글한다.
> > > - 문서에는 존재하지만 보이지 않게 만드는 것.
> > > - Expensive initial load, cheap toggle
> >
> > ##### v-if, v-else-if, v-else
> >
> > > - 조건부 렌더링
> > > - directive의 표현식이 true일 때만 렌더링
> > > - 참일 경우에만 DOM에 들어간다. 거짓이면 DOM에서 삭제됨(렌더링 안됨)
> > > - cheap initial load, expensive toggle
> >
> > ##### v-for
> >
> > > - `v-for = "item in items" :key="idx"`
> > > - `v-for = "(item, idx) in items" :key="idx"`
> > > - 반드시 key 속성을 각 요소에 작성
> > > - 버전2에서는 v-for 가 v-if 보다 우선순위가 높고 3에서는 반대이다.
> > >   - 무조건 동시에 사용하지 말 것
> >
> > ##### v-on
> >
> > > - element에 이벤트 리스너를 연결
> > > - `v-on:click = "콜백함수"` 
> > > - preventDefault 지정 가능
> > >   - `@submit.prevent` - 기본 동작을 막기만 함
> > >   - `@submit.prevent="콜백함수"`
> > > - 조건 세팅 가능
> > >   - `@keyup.sapce` - space 칠 때만 이벤트 설정
> > > - 약어
> > >   - `@`
> > >   - `v-on:click` -> `@click`
> >
> > ##### v-bind
> >
> > > - HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당
> > > - object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당
> > >   - `:class = "{ class이름 : true}"`
> > > - 배열로 한번에 여러개 할당 가능
> > >   - `:class = "[class1 class2]"`
> > > - 스타일 지정 가능
> > >   - `:style="{ fontSize: fontSize + 'px' }"`
> > > - 약어
> > >   - `:`
> > >   - `v-bind:href` -> `:href`
> >
> > ##### v-model
> >
> > > - HTML form 과 data를 양방향 바인딩
> > > - 수식어
> > >   - `.lazy` : input 대신 change 이벤트 이후에 동기화
> > >   - `.number`: 문자열을 숫자로 변경
> > >   - `.trim`: 입력에 대한 trim을 진행
>
> #### Options
>
> > ##### computed
> >
> > > - data를 기반으로 하는 계산된 속성
> > >
> > > - ```vue
> > >   data: {
> > >   	num: 2, 
> > >   }, 
> > >   computed: {
> > >   	함수이름: function () {
> > >   		return this.num * 2
> > >   	}, 
> > >   }, 
> > >   ```
> > >
> > > - 함수의 형태이지만 함수의 반환값이 바인딩 된다.
> > >
> > >   - 반드시 반환 값이 있어야 한다.
> > >
> > > - 종속된 데이터가 변경될 때만 함수를 실행
> > >
> > >   - 종속된 데이터에 따라 저장됨 (캐싱)
> > >   - 의존하는 데이터가 없으면 절대로 업데이트 되지 않는다.
> > >
> > > - methods는 렌더링 시 함수를 다시 실행하지만 computed는 이미 계산된 값이므로 업데이트가 없다면 계산을 반복하지 않고 계산된 결과를 바로 반환
> >
> > ##### watch
> >
> > > - 데이터를 감시
> > >
> > > - 데이터에 변화가 있다면 실행하는 함수
> > >
> > > - ```vue
> > >   watch: {
> > >   	변수: function (newvalue, oldvalue) {
> > >   		do something
> > >   	}
> > >   }
> > >   ```
> > >
> > > - 반환 값 없이 동작 실행 가능
> > >
> > > - 그냥 computed 쓰는게 낫다.
> >
> > ##### filters
> >
> > > - `{{ numbers | filter1 | filter2 }}`
> > >
> > > - `|`로 필터를 연결해서 사용 가능
> > >
> > > - ```vue
> > >   filters: {
> > >   	getOdd : funtion (numbers) {
> > >   		const oddNums = numbers.filter(function (num) {
> > >   			return num % 2
> > >   		})
> > >   		return oddNums
> > >   	}, 
> > >   }, 
> > >   ```
> > >
> > > - 



## Lifecycle Hooks

### Lifecycle Hooks

> - 각 Vue 인스턴스는 생성될 때 초기화 단계를 거친다.
>
>   - 데이터 관찰/ DOM에 마운트/ DOM 업데이트 등
>
> - created: vue 인스턴스 생성된 후 호출
>
> - ```vue
>   created: function () {
>   	console.log('Vue 인스턴스 생성 완료')
>   }
>   ```
>
> - 