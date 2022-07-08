# Git 원격저장소 이름(origin) 변경하기



Git를 처음 배우면 가장 먼저 push와 pull에 대해 배운다.

명령어는 `git push <원격저장소 이름> <브랜치 이름>` 으로 배우는데 원격저장소 이름에는 아래와 같이 origin만을 쓴다.

```bash
$ git push origin master
$ git pull origin master
```



구글링해보니 보통 Git에서 Clone을 하게되면 원격저장소의 이름이 origin으로 저장되기 때문에 통상적으로 origin을 사용하는 것 같다.



우선 등록된 원격저장소를 확인하기 위해 `git remote` 명령어를 사용한다.

`git remote -v`를 하면 등록한 원격저장소의 URL주소까지 확인할 수 있다.

```bash
$ git remote
origin

$ git remote -v
origin  https://github.com/mechauk418/TIL.git (fetch)
origin  https://github.com/mechauk418/TIL.git (push)
```



원격저장소의 이름을 바꾸는 명령어는 `git remote rename A B` 이다.

(저장소의 이름을 A->B로 바꾼다.)

```bash
$ git remote rename origin main
Renaming remote references: 100% (1/1), done.
```



 `git remote -v` 명령어를 통해 이름이 변경된 것을 확인할 수 있다.

```bash
$ git remote -v
main    https://github.com/mechauk418/TIL.git (fetch)
main    https://github.com/mechauk418/TIL.git (push)
```

