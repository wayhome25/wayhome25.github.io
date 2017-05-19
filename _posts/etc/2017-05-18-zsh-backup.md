---
layout: post
title: 기본 셸을 zsh로 변경, .zshrc 백업을 위한 심볼릭 링크파일 생성  
category: etc
comments: true
---

# 기본 셸 변경
## zsh

<http://theyearlyprophet.com/love-your-terminal.html>  
bash와 비슷하게 동작하는 셸로, 사용성이 좋다.

### 리눅스

```
sudo apt-get install zsh
curl -L http://install.ohmyz.sh | sh
chsh -s `which zsh`
```

### 맥

```
brew install zsh zsh-completions
curl -L http://install.ohmyz.sh | sh
chsh -s `which zsh`
```


- **`chsh: /usr/local/bin/zsh: non-standard shell` 오류 발생할 경우**


```
sudo vim /etc/shells
맨 아래에 `which zsh`했을때의 결과를 추가 후 저장
```

- **현재 shell 확인법** : echo $SHELL

---


# 백업을 위한 심볼릭 링크파일 생성
- root 폴더내의 원본 설정 파일을 드롭박스 settings 폴더 안으로 옮긴다
- 해당 원본파일에 대한 심볼릭 링크 파일을 root 폴더내에 만든다. (바로가기 같은 것)
- -s 옵션 : 심볼릭 링크파일을 생성
- [링크파일 생성](http://webdir.tistory.com/148)

```shell
❯ mv .zshrc ~/Dropbox/settings # 원본을 Dropbox/settings/ 폴더로 이동
❯ ln -s ~/Dropbox/settings/.zshrc ~/ # 심볼릭 링크파일 생성
```

- root 폴더의 .zshrc는 Dropbox 원본을 가르키고 있으며, 수정시 Dropbox 내의 파일이 함께 수정된다.
