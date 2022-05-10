### SFC

> #### Component(컴포넌트)
>
> > - 기본 HTML element를 확장, 재사용 가능한 코드를 캡슐화 하는데 도움
> > - CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어의 구성 요소를 의미
>
> #### SFC (Single File Component)
>
> > - 하나의 컴포넌트는 .vue 확장자 파일 한개
> > - vue 컴포넌트 == vue 인스턴스 == .vue



### Vue CLI

> #### Node.js
>
> > - 브라우저 프로그래밍 언어인 자바스크립트를 브라우저 외의 다른 환경에서도 구동할 수 있도록 하는 런타임 환경
> >
> > ##### NPM (Node Package Manage)
> >
> > > - Python의 pip와 같이 의존성 패키지를 관리
> > > - Node.js 기본 패키지 관리자
> > > - Node.js 설치시 함께 설치됨
>
> #### Vue CLI Quick Start
>
> > - 설치
> >
> > ```ba
> > npm install -g @vue/cli
> > ```
> >
> > - 버전 확인
> >
> > ```bash
> > vue --version
> > ```
> >
> > - 프로젝트 생성
> >
> > ```
> > vue create <프로젝트 이름>
> > ```
> >
> > - 프로젝트 디렉토리 이동 및 서버 실행
> >
> > ```bash
> > cd <프로젝트 이름>
> > npm run serve
> > ```
> >
> > - 서버는 `ctrl + c` 로 종료 가능
> >
> > - 모듈 지우고 새로 받기
> >
> > ```bash
> > node_modules 삭제
> > pakage.json 이 있는 폴더에서
> > npm i
> > ```
> >
> > 



### Babel & Webpack

> #### Babel
>
> > - 자바스크립트 컴파일러
> > - 최신 자바스크립트 문법(ES5+)을 구버전으로 변역/변환
>
> #### Webpack
>
> > - static module bundler
> > - 모듈 간 의존성 문제 해결
> > - 프로젝트에 필요한 모든 모듈을 매핑, 내부적으로 종속성 그래프를 빌드



### Pass Props & Emit Events

> #### 컴포넌트 등록 3단계
>
> > 1. 불러오기 (import)
> >
> >    ```vue
> >    <script>
> >    import HelloWorld from './components/HelloWorld.vue'
> >    import HelloWorld from '@/components/HelloWorld.vue'
> >    // @/는 src/와 같은 의미
> >    ```
> >
> >    ```vue
> >    import <컴포넌트를 부를 이름> from '<컴포넌트위치>'
> >    ```
> >
> >    
> >
> > 2. 등록하기 (register)
> >
> >    ```vue
> >    export default {
> >      name: 'App',
> >      components: {
> >        HelloWord: HelloWorld, 
> >    	// 아래와 같다.
> >    	HelloWord, 
> >      }
> >    }
> >    ```
> >
> >    
> >
> > 3. 보여주기 (print)
> >
> >    ```vue
> >    // 카멜 케이스
> >    <HelloWord />
> >    // 케밥 케이스
> >    <hello-word></hello-word>
> >    ```
> >
> >    
>
> #### 컴포넌트 data
>
> > - **반드시 함수여야 한다.**
> > - 각 인스턴스는 모두 같은 data 객체를 공유하기 때문에 새로운 data 객체를 return 해야 한다.
> >
> > ```vue
> > data: function () {
> >     return {
> >       parentData: 'This is parent Data by v-bind', 
> >     }
> > ```
> >
> > 
>
> #### Props
>
> > - 부모 컴포넌트의 정보, 데이터를 전달하기 위한 사용자 지정 특성
> > - 자식에서 상위를 직접 참조는 불가
> >
> > ```vue
> > // 부모 컴포넌트
> > <TheAbout my-messae="CamelCase"/>
> > <the-about my-message="kebab-case"></the-about>
> > 
> > // v-bind를 사용해서 동적 전달 가능
> > <the-about :my-message="myMessage"></the-about>
> > <the-about :my-message="`메세지는 ${myMessage}`"></the-about>
> > ```
> >
> > ```vue
> > // 자식 컴포넌트
> > <template>
> >   <h1>{{ myMessage }}</h1>
> > </template>
> > 
> > <script>
> > export default {
> >   name : 'TheAbout', 
> >   props: {
> >     myMessage: String, 
> >   }, 
> > }
> > ```
>
> #### Emit event
>
> > - 자식 컴포넌트가 부모 컴포넌트에 보내는 이벤트
> > - `$emit` 인스턴스 메서드 사용
> >   - `$emit('이벤트이름', 데이터)`
> >
> > - 이벤트 이름은 kebab-case 사용 권장
> >
> > ```vue
> > // 자식 컴포넌트
> > <input 
> >   type="text"
> >   v-model="childInputData"
> >   @keyup.enter="childInputChange"
> > >
> > 
> > ...
> > data: function () {
> >     return {
> >       childInputData: ''
> >     }
> >   },
> > methods: {
> >     childInputChange: function () {
> >     this.$emit('child-input-change', this.childInputData)
> >     }
> > }, 
> > ...
> > ```
> >
> > ```vue
> > <the-about 
> > 	...
> >     @child-input-change="parentGetChange"
> >     ...
> > ></the-about>
> > 
> > 
> > ...
> >   methods: {
> >     parentGetChange: function (inputData) {
> >       console.log(`About으로 부터 ${inputData}를 받음!`);
> > 
> >     }
> >   }
> > ...
> > 
> > ```
> >
> > 
>
> 



### Vue Router

> #### vue router 시작
>
> > ```bash
> > vue create my-router-app
> > cd my-router-app
> > ```
> >
> > ```bash
> > vue add router
> > 
> > npm run serve
> > ```
> >
> > ##### 변화
> >
> > > 1. App.vue
> > > 2. router/index.js 생성
> > > 3. views 디렉토리 생성
>
> #### router-link
>
> > ```vue
> > <nav>
> >     <router-link :to="{ name: 'home' }">Home</router-link> |
> >     <router-link :to="{ name: 'about' }">About</router-link>
> > </nav>
> > <router-view/>
> > ```
> >
> > - 페이지를 새로고침 하지 않고 페이지를 바꿔 보여준다. 
> > - 브라우저 페이지를 다시 로드 하지 않지만 url은 변경된다.
> > - router-link 는 하나의 컴포넌트
> > - router-link를 클릭하게 되면 router-view에 컴포넌트가 넘어간다.
>
> #### 동적 인자 전달
>
> > ```vue
> > import UserProfile from '../views/UserProfile.vue'
> > ...
> > 
> > {
> >     path: '/user/:userId/:username/:major', 
> >     name: 'profile', 
> >     component: UserProfile, 
> > }, 
> > ```
> >
> > ```vue
> > <template>
> >   <div>
> >     <h1>user profile</h1>
> >     <p>
> >       id: {{ user.userId }}
> >       이름: {{ user.username }}
> >       전공: {{ user.major }}
> >     </p>
> >   </div>
> > </template>
> > 
> > <script>
> > export default {
> >   name: 'UserProfile', 
> >   data: function () {
> >     return {
> >       user: this.$route.params, 
> >     }
> >   }
> > 
> > }
> > </script>
> > ```
> >
> > 