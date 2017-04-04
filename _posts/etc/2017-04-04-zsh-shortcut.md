---
layout: post
title: zsh, bash 단축키
tags: [단축키, zsh]
category: etc
comments: true
---

zsh에서 ipython 등을 실행하여 간단하게 코드를 작성하는 경우가 많다.    
그때마다 줄 전체를 삭제 한다던지 줄의 맨 앞으로 이동 하는 등의 간단한 동작도 원하는 대로 잘 되지 않아서 불편했었다. 검색해보니 bash, zsh에도 편리하게 명령어를 편집할 수 있도록 shortcut이 존재한다는 것을 알았다.    
[Shortcuts to improve your bash & zsh productivity](http://www.geekmind.net/2011/01/shortcuts-to-improve-your-bash-zsh.html)


## 자주 사용하는 명령어

| shorcut           | Action                             |
|-------------------|------------------------------------|
| CTRL + A          | 라인 맨 앞으로 이동                |
| CTRL + E (end-of-line)          | 라인 맨 끝으로 이동                |
| CTRL + 좌우방향키 | 단어 단위로 이동                   |
| CTRL + U          | 라인 전체 삭제 (라인시작~커서위치) |
| CTRL + K ( kill-line)          | 라인 전체 삭제 (커서위치~라인 끝)  |
| CTRL + W          | 커서 앞 단어 삭제  |
| CTRL + R          | 이력 검색 (CTRL + G : 종료)        |
| CTRL + _          | 실행취소                           |


## 모든 검색어 보기
- zsh에서 `bindkey` 명령을 통해 사용할 수 있는 단축키 리스트를 확인할 수 있다.

```shell
❯ bindkey
"^@" set-mark-command
"^A" beginning-of-line
"^B" backward-char
"^D" delete-char-or-list
"^E" end-of-line
"^F" forward-char
"^G" send-break
"^H" backward-delete-char
"^I" fzf-completion
"^J" accept-line
"^K" kill-line
"^L" clear-screen
...
...
...
```
