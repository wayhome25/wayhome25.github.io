---
layout: post
title: SSH 접속시 iterm2 zsh 테마 바꾸기
category: etc
tags: [ssh, iterm2 theme, iterm2, zsh]
comments: true
---

ssh 접속시 터미널 테마가 똑같으면 내가 로컬에 있는지 서버에 접속해있는지 헷갈릴 때가 있다.    
간단한 설정을 통해서 ssh 접속시 zsh 테마가 바뀌도록 할 수 있었다.

### Profile 만들기
- iterm2-Preferences-profile 메뉴에서 2개의 프로필을 만든다.
- 평소에 사용할 프로필 (Default) 컬러 테마는 Solarized Dark

![screen 16](https://i.imgur.com/4GpPDwE.png)

- ssh 접속시 사용할 프로필 (SSH) 컬러 테마는 Dracula 로 각각 설정했다.

![screen 17](https://i.imgur.com/NLVHL20.png)

### ~/.oh-my-zsh/custom 경로에 iTerm2-ssh.zsh 파일 추가하기
- `vim ~/.oh-my-zsh/custom/iTerm2-ssh.zsh` 를 입력하고 해당 파일에 아래 내용을 추가한다.

```shell
function tabc() {
  NAME=$1; if [ -z "$NAME" ]; then NAME="Default"; fi
  echo -e "\033]50;SetProfile=$NAME\a"
}

function tab-reset() {
    NAME="Default" # Default 라는 이름의 프로필 생성필요
    echo -e "\033]50;SetProfile=$NAME\a"
}

function colorssh() {
    if [[ -n "$ITERM_SESSION_ID" ]]; then
        trap "tab-reset" INT EXIT
        if [[ "$*" =~ "web*|production|ec2-.*compute-1|stage" ]]; then
            tabc SSH   # SSH 라는 이름의 프로필 생성필요
        fi
    fi
    ssh $*
}
compdef _ssh tabc=ssh

alias ssh="colorssh"
```

### 변경내용 확인하기
- 터미널을 재시작하고
- ssh 명령어 뒤에 아래와 같은 문자열이 오면 ssh 접속시 컬러 테마가 Dracula로 바뀌는 것을 확인할 수 있다.

```shell
> ssh web *
> ssh ec2-.*compute-1
> ssh production
> ssh stage
```

### 참고자료
- https://github.com/hectorleiva/iterm2-ssh-color-scheme
- https://coderwall.com/p/t7a-tq/change-terminal-color-when-ssh-from-os-x
