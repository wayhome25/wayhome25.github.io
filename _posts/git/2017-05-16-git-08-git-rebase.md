---
layout: post
title: git 도구 - 커밋 수정, 삭제 rebase
category: git
tags: [git]
comments: true
---
> [Pro Git Book](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%ED%9E%88%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%8B%A8%EC%9E%A5%ED%95%98%EA%B8%B0) 을 읽고 주요 내용을 정리합니다.


## 마지막(가장 최근) 커밋 수정하기
- 커밋 메시지를 수정하려면 아래 명령을 사용한다.

```shell
$ git commit --amend
```
- 커밋 파일을 추가하거나 삭제하려면 `git add` 명령으로 Staging Area에 넣거나 `git rm` 명령으로 추적하는 파일 삭제한다. 그리고 `git commit --amend` 명령으로 커밋하면 된다. 이 명령은 현 Staging Area의 내용을 이용해서 수정한다.

## 과거 커밋 메시지 여러개 수정하기
- git rebase 를통해서 어느 시점부터 HEAD 까지의 커밋을 한번에 Rebase 한다.
- 이미 중앙서버에 Push 한 커밋은 절대 고치지 말아야 한다. Push 한 커밋을 Rebase 하면 결국 같은 내용을 두 번 Push 하는 것이기 때문이다.

```shell
$ git rebase -i HEAD~3 # HEAD에서 부터 최근 3개의 커밋 표시한다
```
- 특정 커밋에서 실행을 멈추게 하려면 스크립트를 수정해야 한다. `pick`이라는 단어를 'edit’로 수정하면 그 커밋에서 멈춘다.
- `git commit --amend` 를 통해서 멈춘 커밋의 이전 커밋 메시지를 수정할 수 있다.
- 커밋 메시지를 수정하고 텍스트 편집기를 종료하고 나서 `git rebase --continue` 명령을 실행한다.
- 다른 것도 pick을 edit로 수정해서 이 작업을 몇 번이든 반복할 수 있다


## 커밋 삭제, 순서 바꾸기, 합치기
- 대화형 Rebase 도구로 커밋 전체를 삭제하거나 순서를 조정하거나, 합칠 수 있다.
- 커밋 리스트에서 삭제하고 싶은 커밋을 삭제하고, 순서를 변경하면 그대로 적용된다.

```shell
# 대화형 Rebase 실행
$ git rebase -i HEAD~3 # HEAD에서 부터 최근 3개의 커밋 표시한다
```
- squash를 입력하면 Git은 해당 커밋과 바로 이전 커밋을 합칠 것이고 커밋 메시지도 Merge 한다.
- 저장하고 나서 편집기를 종료하면 Git은 3개의 커밋 메시지를 Merge 할 수 있도록 에디터를 바로 실행해준다.

## 모든 커밋에서 특정 파일 제거하기
- `git filter-branch --tree-filter`명령을 통해서 passwords.txt 같은 파일을 히스토리에서 삭제할 수 있다.

```shell
$ git filter-branch --tree-filter 'rm -f passwords.txt' HEAD
```
