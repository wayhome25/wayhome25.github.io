---
layout: post
title: git 도구 - stashing 과 cleaning  
category: git
tags: [git]
comments: true
---
> [Pro Git Book](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Stashing%EA%B3%BC-Cleaning) 을 읽고 주요 내용을 정리합니다.

# Stashing
- 어떤 작업 중에 급한 일이 생겨 다른 브랜치로 변경해야한다. 그런데 현재 하던 작업이 진행중이어서 커밋을 하기에는 애매하다.
- 커밋하지 않고, 나중에 다시 돌아와서 작업을 이어서 하고 싶을 때는 `git stash` 명령을 사용해서 해결
- stash 명령 적용대상
	1. Modified + Tracked 상태인 파일 (한번이라도 add를 한 적이 있는 파일)
	2. Staging Area에 있는 파일

## git stash
- git stash 명령을 실행하면 스택에 새로운 Stash가 만들어지고 커밋하기 애매한 작업중인 파일의 상태가 저장된다.
- 그리고 워킹 디렉토리는 깨끗해진다.
- `git stash list` 명령을 사용해서 저장한 Stash 목록을 확인할 수 있다.

```shell
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

## git stash apply
- `git stash apply` 명령을 실행하여 Stash 내용을 다시 적용할 수 있다.
- `git stash apply stash@{2}` 처럼 원하는 Stash 를 골라서 적용하는 것도 가능하다. (이름이 없으면 가장 최근 Stash 적용)
- `git stash apply --index` 옵션을 통해서 Staged 상태까지 적용할 수 있다.
- `git stash -u` 옵셔능ㄹ 통해서 untracked 파일도 함께 저장할 수 있다.

## git stash drop
- `git stash drop stash@{2}` 명령을 사용하여 해당 Stash를 제거한다.
- `git stash pop`이라는 명령도 있는데 이 명령은 Stash를 적용하고 나서 바로 스택에서 제거해준다.

## git stash branch
- `git stash branch` 명령을 실행하면 Stash 할 당시의 커밋을 Checkout 한 후 새로운 브랜치를 만들고 여기에 적용한다. 이 모든 것이 성공하면 Stash를 삭제한다.

# git clean
- 워킹 디렉토리 안의 추적하고 있지 않은 모든 파일을 지운다.
- `git clean -n` 옵션을 통해서 가상으로 실행해보고 어떤 파일들이 지워질지 알 수 있다.
- git clean 명령은 추적 중이지 않은 파일만 지우는 게 기본 동작이다. .gitignore`에 명시했거나 해서 무시되는 파일은 지우지 않는다.
