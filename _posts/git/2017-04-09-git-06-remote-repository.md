---
layout: post
title: 생활코딩 git 07 - github clone, git remote, pull
category: git
tags: [git]
comments: true
---
> [생활코딩-git](https://opentutorials.org/module/2676) 수업을 듣고 중요 내용을 정리합니다.   

# 원격저장소
> 원격저장소는 소스코드와 버전을 백업하고, 다른 사람과 협업을 하기 위한 핵심적인 기능입니다. 여기서는 원격저장소에 대해서 알아봅니다

- local repository & remote repository
- 원격저장소의 중요한 의미 2가지
  - 소스코드를 백업한다.
  - 다른사람과 협업한다.
- 혼자서 작업하는 경우 원격 저장소를 사용하는 이유는 크게 많지는 않다. 왜냐하면 대안이 있기 때문이다. (드롭박스, 구글 드라이브와 같은 클라우드 스토리지 서비스)

# 원격 저장소를 지역 저장소로 복제
> 여기서는 github.com이라는 서비스를 소개하고, 이 서비스를 이용해서 이미 존재하고 있는 오픈소스의 원격저장소의 내용을 내 컴퓨터의 지역저장소로 가져오는 방법에 대해서 알아봅니다. 이 과정에서 git의 소스코드와 이 소스코드의 첫번째 커밋의 내용도 알아봅니다.

- git의 소스코드를 지역저장소로 가져오기

```shell
git clone https://github.com/git/git.git 폴더이름
```

- 로그를 거꾸로 출력하기

```shell
git log --reverse
```

- git의 첫번째 커밋으로 체크아웃하기

```shell
git checkout e83c5163316f89bfbde7d9ab23ca2e25604af290
```

## 원격 저장소 만들기
- 원격 저장소의 별명을 설정할 수 있다. (저장소 주소가 길기 때문에)
- 여러개의 원격 저장소를 로컬저장소로 저장할 수 있다.

### remote 저장소 설정
```shell
# 원격 저장소의 이름(별명)을 각각 origin , memo 지정한다.
❯ git remote add origin https://github.com/wayhome25/gitfth.git
❯ git remote add memo https://github.com/wayhome25/memo.git
❯ git remote
memo
origin


# 로컬저장소를 origin 원격저장소의 master 브랜치로 연결하여 push한다.
# 처음에 한번만 -u 설정을 하면 앞으로 git push 만 입력해도 origin의 master 브랜치로 push한다.
❯ git push -u origin master
```
### remote 저장소 변경
```shell
# 현재 원격 저장소 상태 확인
❯ git remote -v
# 변경하고자 하는 원격저장소 설정
❯ git remote set-url origin https://github.com/wayhome25/fastcampus_school
```


- 이미 존재하는 원격 저장소를 새로운 로컬 저장소에 연결할 수 있다.
- 별도의 remote 설정없이 clone을 통해서 원격 저장소와 연결된다.

```shell
❯ git clone https://github.com/wayhome25/gitfth.git .
❯ git remote -v
origin	https://github.com/wayhome25/gitfth.git (fetch)
origin	https://github.com/wayhome25/gitfth.git (push)
```


# 원격 저장소와 지역 저장소의 동기화 방법
> 하나의 원격저장소를 중심으로 두개의 지역저장소가 소스코드를 동기화하는 방법에 대해서 알아봅니다.

- 동기화의 효용
  - 협업을 할 때
  - 여러대의 컴퓨터에서 작업할 때 (집에서 작업하다가 회사에서 작업을 계속 하는 등)
- 모든 저장소들은 버전에 대한 모든 정보를 각자 갖고 있다.
- 어떤 작업을 하기 전에는 git pull, 작업이 끝나면 git push를 하는 것을 습관화 시켜야한다.

```shell
# 집에서 (git_home/ 폴더)
git add f1.txt
git commit f1.txt
git push

# 회사에서 (git_office/ 폴더)
git pull
git add f1.txt
git commit f1.txt
git push
```
