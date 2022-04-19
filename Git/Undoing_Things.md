## Undoing Things



### git restore

> ```bash
> git restore <파일명>
> ```
>
> - 이미 추적당하는 add 된 파일을 내린다.
> - add 된 파일을 수정 전으로 되돌림
> - 수정했던 내용은 다 사라진다.

### git rm --cached

> ```bash
> git rm --cached <파일명>
> ```
>
> - 새로운 파일을 add 했을 때, 추적당하지 않도록 바꾸고 내린다.
> - 커밋이 없을 때.

### git restore -- staged

> ```bash
> git restore -- staged <파일명>
> ```
>
> - 새로운 파일을 add 했을 때, 추적당하지 않도록 바꾸고 내린다.
> - 커밋이 있을 때.





### git commit --amend

> ```bash
> git commit --amend 
> git commit --amend -m '변경할 커밋 메세지'
> ```
>
> 
>
> 1. 마지막 커밋 후 수정이 없을 때, 커밋 메세지만 수정
> 2. Staging Area에 새로 올라온 내용이 있을 때, 커밋 덮어쓰기
>
> - vim 모드에서 `i`로 끼워넣기로 바꾼다.
> - `esc`로 끼워넣기 기능에서 나오기
> - `:wq` 로 저장



### git reset

> ```bash
> git reset <옵션> <취소가고자 하는 커밋 ID>
> ```
>
> - 옵션
>
>   1. `--soft`
>      - 돌아가려는 커밋으로 돌아가고
>      - commit 전 상태로 돌아간다. (add 된 상태는 유지)
>   2. `--mixed`
>      - 돌아가려는 커밋으로 돌아가고
>      - add 전으로 돌아간다.
>   3. `--hard`
>      - 돌아가려는 커밋으로 돌아가고
>      - 커밋된 파일들을 모두 삭제
>      - 단, 추적당하지 않는 파일은 상관없음.
>
> - 이미 삭제한 커밋으로 돌아가려면
>
>   ```bash
>   git reflog
>   이전 삭제한 로그를 보여준다.
>   
>   git reset --hard <복구하고자 하는 커밋ID>
>   ```
>
>   



### git revert

> ```bash
> git revert <취소하고자 하는 커밋 ID>
> ```
>
> - 이전 커밋을 취소하되, 이전 커밋을 취소한다는 새로운 커밋을 새로 만든다.
> - 단 커밋된 파일들이 삭제된다.
> - 띄어쓰기를 통해 여러 커밋을 한번에 되돌리기 가능하다.





## 협업 Workflow

### Feature Branch Workflow

> - 소유권이 있는 프로젝트
>
> - 각 인원이 clone
>
> - 브랜치를 각각 생성
>
>   ```bash
>   git switch -c <브랜치명>
>   ^ 브랜치를 생성하고 이동
>   ```
>
> - 각 인원은 각자의 브랜치에 push
>
>   ```bash
>   git push origin <브랜치명>
>   ```
>
> - 머지
>
> - 각 브랜치 삭제
>
> - 각 인원은 마스터 브랜치 pull
>
>   ```bash
>   git switch master
>   git pull orgin master
>   git brach
>   ^ 브랜치 목록 확인
>   git branch -d <삭제할 브랜치명>
>   ```
>
>   

### Forking Workflow

> - 소유권이 없는 프로젝트
>
> - fork를 통해 프로젝트를 복사해온다. (서로 다른 프로젝트)
>
> - 복제한 프로젝트를 clone 받는다.
>
> - 원본 원격저장소와 동기화를 위해 새로운 리모트주소 생성
>
>   ```bash
>   git remote add upstream <원본URL>
>   ```
>
> - 기능 구현 후 clone 받은 origin (복제한 브랜치)에 push