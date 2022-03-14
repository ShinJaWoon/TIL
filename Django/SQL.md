# SQL

## Database

> ### DB 데이터 베이스
>
> - 체계화된 데이터의 모임
> - 여러 사람이 공유하고 사용할 목적의 통합 관리되는 정보의 집합
> - 몇 개의 자료 파일을 조직적으로 통합하여, 자료 항목의 중복을 없애고, 자료를 구조화하여 기억시켜 놓은 자료의 집합체
>
> ### 장점
>
> > - 데이터 중복 최소화
> > - 데이터 무결성 (정확한 정보 보장)
> > - 데이터 일관성
> > - 데이터 독립성 (물리적 / 논리적)
> > - 데이터 표준화
> > - 데이터 보안 유지
>
> ### RDB 관계형 데이터 베이스
>
> > - Relational Database
> > - key 와 value 들의 간단한 관계(relation)를 표 형태로 정리한 데이터 베이스
> >
> > #### 용어 정리
> >
> > > - 스키마(schema): 자료의 구조, 표현방법, 관계 등 전반적인 명세
> > > - 테이블(table): 열(컬럼/필드)와 행(레코드/값)의 보델을 사용해 조직된 데이터 요소들의 집합
> > > - 기본키(Primary Key): 각 행의 고유값, 반드시 설정.
>
> ### RDBMS
>
> > - 관계형 데이터베이스 관리 시스템
> > - Relational Database Management System



## RDBMS

### SQLite

> #### Data Type
>
> > - INTERGER: 0, 1, 2, 3, 4, 6, 8 바이트에 저장된 부호 있는 정수
> > - TEXT
> > - BLOB: 입력된 데이터 그대로 저장
> > - REAL: 8바이트 부동 소수점 실수
> > - NUMERIC
> > - NULL
>
> ```bash
> $ sqlite3 tutorial.sqlite3
> ```
>
> 

### CRUD

> #### CREATE
>
> > - **CREATE**
> >
> >   ```sqlite
> >   CREATE TABLE classmates (
> >     name TEXT NOT NULL,
> >     age INT NOT NULL,
> >     address TEXT NOT NULL
> >   );
> >   
> >   -- id 열을 생성 시 INSERT를 할 때 id 값도 넣어줘야 한다.
> >   -- PRIMARY KEY는 반드시 INTEGER로 만들어야 함
> >   CREATE TABLE classmates (
> >     id INTEGER PRIMARY KEY, 
> >     name TEXT NOT NULL,
> >     age INT NOT NULL,
> >     address TEXT NOT NULL
> >   );
> >   
> >   -- id에 AUTOINCREMENT를 붙이면 id 재활용을 하지 않는다.
> >   CREATE TABLE classmates (
> >     id INTEGER PRIMARY KEY AUTOINCREMENT, 
> >     name TEXT NOT NULL,
> >   
> >   );
> >   
> >   DROP TABLE classmates;
> >   -- 테이블 삭제
> >   ```
> >
> >   - id 에 PRIMARY KEY를 할당하지 않아도 조회시 rowid를 보면 id를 볼 수는 있다. 즉, 항상 id는 자동으로 생성된다.
> >   - **PRIMARY KEY**는 반드시 **INTEGER**로 만들어야 함 (**INT는 불가!)**
> >   - NOT NULL 이 있을 경우 값을 비워둘 수 없음, 없으면 NULL이 들어감
> >
> > - **INSERT** : 테이블에 단일 행 삽입
> >
> >   ```sqlite
> >   INSERT INTO <테이블이름> (<칼럼1>, <칼럼2>, ...) VALUES(<값1>, <값2>, ...);
> >   ```
> >
> >   - 모든 열에 대한 데이터가 있을 경우 column 명시 필요 없음
> >
> >   ```sqlite
> >   INSERT INTO classmates VALUES
> >   ('홍길동', 30, '서울'),
> >   ('김하나', 30, '대전'),
> >   ('이둘둘', 26, '대구'),
> >   ('박셋셋', 29, '부산'),
> >   ('최넷넷', 28, '인천');
> >     
> >   ```
>
> #### READ
>
> > - **SELECT**
> >
> >   - 테이블에서 데이터를 조회
> >   - 다양한 절(clause)와 함께 사용
> >   - **SELECT - clause**
> >     - LIMIT : 쿼리에서 반환되는 행 수 제한. 특정 행부터 시작하기 위한 OFFSET 키워드와 함께 사용하기도 한다.
> >     - WHERE: 쿼리에서 반환된 행에 대한 특정 검색 조건 지정
> >     - SELECT DISTINCT: 조회 결과에서 중복 행 제거
> >
> >   ```sqlite
> >   SELECT <칼럼1, 칼럼2> FROM <테이블>;
> >     
> >   -- *은 전체를 의미
> >   SELECT * FROM <테이블>;
> >   ```
> >
> >   - 특정 칼럼만 조회
> >
> >   ```sqlite
> >   SELECT <칼럼1, 칼럼2, ...> FROM <테이블> LIMIT <조회할 행 개수>;
> >   SELECT <칼럼1, 칼럼2, ...> FROM <테이블> LIMIT <조회할 행 개수> OFFSET <시작할 위치 -1>;
> >   SELECT rowid, name FROM classmates LIMIT 1 OFFSET 1;
> >   ```
> >
> >   - OFFSET은 **0부터 시작**함을 주의
> >
> >   ```sqlite
> >   SELECT <칼럼1, 칼럼2> FROM <테이블> WHERE <조건>;
> >   SELECT rowid, name FROM classmates WHERE address = '서울';
> >   ```
> >
> >   ```sqlite
> >   SELECT DISTINCT age FROM classmates;
> >   --age에 중복을 없애고 조회
> >   ```
> >
> >   
>
> #### DELETE
>
> > - **DELETE**
> >
> >   ```sqlite
> >   DELETE FROM <테이블이름> WHERE <조건>;
> >   ```
> >
> >   - SQLite는 삭제한 id를 재활용. (장고는 재활용을 하지 않음)
> >   - id 재활용을 하지 않으려면 CREATE를 할 때 AUTOINCREMENT 속성을 붙임
> >
> > - **TRUNCATE**
> >
> >   - DDL (DML이 아님)
> >   - 초기화하면 id도 초기화 (AUTOINCREMENT를 써도 초기화됨)
>
> #### UPDATE
>
> > - **UPDATE**
> >
> >   ```sqlite
> >   UPDATE <테이블이름> SET <컬럼1>=<값1>, <컬럼2>=<값2>, ... WHERE <조건>;
> >   ```
> >
> >   

### 기타 SQL 명령어

> #### Aggregate function
>
> > - SELECT 구문에서 사용
> >
> > - 여러 행으로 부터 계산을 수행하여 단일 값 반환
> >
> > - 종류
> >
> >   - COUNT : 그룹의 항목 수
> >   - AVG : 평균
> >   - MAX: 최댓값
> >   - MIN: 최솟값
> >   - SUM: 총합
> >
> >   ```sqlite
> >   SELECT AVG(age) FROM users WHERE age >= 30;
> >   -- 나이가 30 이상인 사람들의 나이의 평균
> >   
> >   SELECT first_name, MAX(balance) FROM users;
> >   -- balance 가 최댓값인 사람의 이름
> >   ```
> >
> >   
>
> #### LIKE operator
>
> > ##### wildcards
> >
> > > - `%` : 0개 이상의 문자. 문자열이 있을 수도, 없을 수도 있음
> > >   - `2%` : 2로 시작하는 값
> > >   - `%2` : 2로 끝나는 값
> > >   - `%2%` : 2가 들어가는 값
> > > - `_` : 반드시 해당 자리에 단일 문자가 들어감
> > >   - `1___` : 1로 시작하고 총 4자리인 값
> > >   - `2_%_%`: 2로 시작하고 적어도 3자리인 값
> >
> > ##### LIKE
> >
> > > ```sqlite
> > > SELECT * FROM users WHERE age LIKE '2_'
> > > -- 20대인 사람을 조회
> > > ```
>
> #### ORDER BY
>
> > - 특정 컬럼을 기준으로 데이터를 정렬해서 조회
> >
> > - SELECT 구문에서 사용
> >
> >   - ASC - 오름차순 (default)
> >   - DESC - 내림차순
> >
> >   ```sqlite
> >   SELECT * FROM <테이블이름> ORDER BY <컬럼1> ASC;
> >   SELECT * FROM <테이블이름> ORDER BY <컬럼1>, <컬럼2> DESC;
> >   -- 컬럼1 은 오름차순, 컬럼 2는 내림차순
> >   -- 컬럼마다 설정해야한다.
> >   ```
>
> #### GROUP BY
>
> > - 지정한 기준에 따라 행 세트를 그룹으로 결합
> >
> > - 데이터를 요약할 때 주로 사용
> >
> > - SELECT 구문에서 사용
> >
> > - WHERE 절 뒤에 작성해야 함
> >
> >   ```sqlite
> >   SELECT <컬럼1>, Aggregate_function(<컬럼2>) FROM <테이블이름> GROUP BY <컬럼1>, <컬럼2>
> >   SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
> >   -- AS를 활용하여 COUNT(*) 에 대한 컬럼명을 바꾸어 그룹화 할 수 있다.
> >   ```
>
> #### ALTER TABLE
>
> > - table 이름 변경
> >
> > - 테이블에 새로운 column 추가
> >
> > - 테이블에 column 삭제
> >
> > - column 이름 수정
> >
> >   ```sqlite
> >   -- 테이블 이름 변경
> >   ALTER TABLE <기존 테이블이름> RENAME TO <새 테이블이름>
> >   
> >   -- 새로운 column 추가
> >   ALTER TABLE <테이블이름> ADD COLUMN <컬럼 이름> <데이터 타입>
> >   -- 기존 레코드에는 새로 추가하는 필드에 대한 정보가 없으므로 NOT NULL 사용 불가
> >   ALTER TABLE <테이블이름> ADD COLUMN <컬럼 이름> <데이터 타입> NOT NULL DEFAULT <디폴트값>
> >   
> >   -- 컬럼 삭제
> >   ALTER TABLE <테이블이름> DROP COLUMN <컬럼 이름> <데이터 타입>
> >   
> >   -- 컬럼 이름 변경
> >   ALTER TABLE <테이블이름> RENAME COLUMN <현재 컬럼이름> TO <새 컬럼이름>
> >   
> >   ```
> >
> >   

