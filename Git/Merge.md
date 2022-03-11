```bash
$ git branch  : 브랜치 목록 확인
$ git branch <브랜치이름> : 새로운 브랜치 생성
$ git branch -d <브랜치이름> : 병합된 특정 브랜치 삭제
$ git branch -D <브랜치이름> : 강제 삭제
$ git switch <브랜치이름> : 다른 브랜치로 이동
$ git switch -c <브랜치이름> : 브랜치 생성과 동시에 이동

$ git log --oneline --all --graph
```

```bash
$ git merge <병합할브랜치이름> : 메인 브랜치로 이동후 머지해야함
```



### 1. fast-forward

> - master가 branch로 단순히 이동하는 결과
> - branch를 머지할 때 master에 변화가 없는 경우 가능

### 2. 3-way merge (merge commit)

> - mater에 변화가 있을 경우 master와 branch를 연결하는 새로운 머지 커밋이 생성

### 3. merge conflict

> - 머지하는 두 브랜치에서 같은 부분을 동시 수정하고 머지하면 자동으로 머지 불가
> - 동일 파일이더라도 서로 다른 부분을 수정했다면 충돌 없음