## DOM

### DOM (Document Object Model)

> #### 개념
>
> > - Document - 문서 한 장 (HTML) / 문서를 조작한다.
> > - 
>
> #### 선택 (Select)
>
> > - `document.querySelector(selector)`
> >   - 제공한 CSS selector를 만족하는 첫 번째 element 객체 반환
> >   - 없으면 null
> > - `document.querySelectorAll(selector)`
> >   - 지정된 selector에 일치하는 NodeList를 반환
> >   - 실시간 반영 X
> >
> > - `HTMLCollection` & `NodeList`
> >   - Live Collection - DOM의 변경사항 실시간으로 반영
>
> #### 변경 (Manipulation)
>
> > ##### 추가
> >
> > - `document.createElement()`
> >   - 작성한 태그 명의 HTML 요소를 생성하여 반환
> > - `Element.append()`
> >   - 특정 Node의 자식 NodeList 중 마지막 자식 다음 Node 객체나 DOMString 삽입
> >   - 여러개 추가 가능
> >   - 반환값 없음
> > - `Node.appendChild()`
> >   - 한 Node를 NodeList 중 마지막 자식으로 삽입
> >   - 한번에 하나만 추가 가능
> >   - Node 객체만 허용
> > - `Node.innerText`
> >   - 최종 스타일링이 적용된 모습으로 표현
> >   - 그대로 나온다.
> > - `Element.innerHTML`
> >   - HTML 태그를 적용하여 마크업 한 모습을 반환
> >   - XSS 공격에 취약 - 사용자가 입력시 스크릡트를 코드에 삽입하여 엑세스 제어를 우회 또는 정보 탈취
> >
> > ##### 삭제
> >
> > - `ChildNode.remove()`
> >   - Node 제거
> > - `Node.removeChild()`
> >   - DOM에서 자식 Node를 제거 및 제거된 노드를 반환
> >
> > ##### 속성
> >
> > - `Element.setAttribute(name, value)`
> >   - name=value 속성을 추가
> >   - 둘 다 문자열로 입력
> >   - 속성이 이미 존재하면 갱신
> > - `Element.getAttribute(attributeName)`
> >   - 해당 요소의 지정된 속성을 문자열로 반환
> > - `Element.style.속성 = '속성값'`
> >   - 간단하게 스타일링 가능
> > - `Element.classList.add('추가할class')`
> >   - 클래스 추가





### Event

> #### Event 개념
>
> > - 네트워크 활동이나 사용자와의 상호작용과 같은 사건의 발생을 알리기 위한 객체
> > - 마우스 클릭, 마우스를 올리는 것, 키보드 입력 등
> > - 특정 메서드 호출 (`Element.click()`) 으로도 만들 수 있음
>
> #### Event handler
>
> > - `EventTarget.addEventListener(type, listener[, options])`
> > - `대상.addEventListener(이벤트, 할 일)`
> >   - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
> >   - 이벤트를 지원하는 모든 객체 (Element, Document, Window 등)를 대상으로 가능
> >   - type
> >     - 반응할 이벤트 유형
> >     - 대소문자 구분 문자열
> >   - listener
> >     - 이벤트 발생 시 알림을 받는 객체
> >     - EventListener 인터페이스 혹은 콜백 함수여야 함
>
> #### Event 취소
>
> > - `event.preventDefault()`
> > - 현재 이벤트의 기본 동작을 중단