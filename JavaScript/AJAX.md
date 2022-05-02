## AJAX

### AJAX

> - Asynchronous JavaScript And XML
> - 비동기식 JS 와 XML
> - 서버와 통신하기 위해 **XMLHttpRequest** 객체를 활용
> - JSON, XML, HTML, TXT 등을 포함은 다양한 포맷을 주고 받을 수 있다.
>
> 
>
> #### 특징
>
> > - 페이지를 새로고침 하지 않아도 수행되는 **비동기성**
> > - 서버의 응답에 따라 전체 페이지가 일부만 업데이트 가능
> >
> > 1. 페이지 새로 고침 없이 서버에 요청
> > 2. 서버로부터 데이터를 받고 작업을 수행
>
> 





### Asynchronous JavaScript

> #### 동기식
>
> > - 순차적, 직렬적 Task
> > - 요청을 보낸 후 응답을 받아야만 다음 동작 (blocking)
>
> #### 비동기식
>
> > - 병렬적 Task
> > - 요청을 보낸 후 응답을 기다리지 않고 다음 동작 (non-blocking)
> >
> > ##### 비동기식을 사용하는 이유
> >
> > > - 매우 큰 데이터가 있을 경우 데이터를 불러올 때 까지 화면이나 앱이 멈춘것 처럼 보인다.
> > > - 데이터를 요청하고 응답받는 동안 앱 실행을 진행하고, 지속적으로 응답하는 화면을 통해 쾌적한 사용자 경험 제공
>
> 
>
> ##### ※ Threads 쓰레드
>
> > - 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스
>
> 
>
> #### Concurrency model
>
> > ##### Call Stack
> >
> > > - 요청이 들어올 때 마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조
> >
> > ##### Web API (Browser API)
> >
> > > - JS 가 아닌 브라우저 영역에서 제공하는 API
> > > - AJAX로 데이터를 가져오거나 시간 관련된 작업을 처리
> > >   - setTimeout(), DOM events, AJAX 데이터를 가져오기
> >
> > ##### Task Queue
> >
> > > - 비동기 처리된 콜백 함수가 대기하는 Queue(FIFO) 형태의 자료 구조
> > > - main thread 가 끝난 후 실행 - JS 코드가 차단되는 것을 방지
> >
> > ##### Event Loop
> >
> > > - Call Stack이 비어있는지 확인
> > > - 비어있을 경우 Task Queue에서 실행 대기 중인 콜백 함수가 있는지 확인
> > > - Task Queue에 대기 중인 콜백 함수가 있다면 가장 앞에 있는 콜백 함수를 Call Stack으로 push



### Callback Function

> #### Callback function
>
> > - 다른 함수에 인자로 전달된 함수
> > - 외부 함수 내에서 호출되어 일종의 루틴이나 작업을 완료
> > - 동기/비동기 모두 사용 가능
> > - 비동기 콜백 (asynchronous callback): 비동기 작업이 완료된 후 코드 실행을 계속하는 데 사용되는 경우
>
> #### Async callbacks
>
> > - 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
> > - 백그라운드 코드 실행이 끝나면 callback 함수를 호출 -> 작업 완료을 알리거나 다음 작업 실행



### Promise

> #### Promis object
>
> > - 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
> > - 비동기 콜백만 사용하면 피라미드 형태의 callback hell 이 벌어진다.
> > - `.then(callback)` : 성공
> > - `.catch(callback)` : 실패
> >   - `.then`이 하나라도 실패하면 동작
> > - `.finally()` : 결과와 상관없이 무조건 지정된 callback 함수 실행
> >   - 무조건 실행되므로 어떠한 인자도 받지 않는다.
> > - **반환값이 반드시 있어야 한다.**





### Axios

> #### Axios
>
> > - AJAX 요청을 편리하게 만드는 Promise 기반의 클라이언트
> > - 