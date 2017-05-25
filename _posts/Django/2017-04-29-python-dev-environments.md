---
layout: post
title: 매번 찾아보는 python 개발환경 세팅 (pyenv, virtualenv, autoenv) + django 프로젝트 및 앱 생성하기
category: Django
tags: [python, Django, pyenv, virtualenv, autoenv]
comments: true
---

# 목차
프로젝트별 버전관리, 패키지 의존성 관리를 위해서 pyenv, virtualenv, autoenv 를 활용한다.

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [목차](#목차)
* [들어가기](#들어가기)
* [1. pyenv](#1-pyenv)
  * [pyenv 설치](#pyenv-설치)
  * [pyenv를 활용한 python 설치](#pyenv를-활용한-python-설치)
* [2. virtualenv](#2-virtualenv)
  * [virtualenv 설치](#virtualenv-설치)
  * [가상환경 추가 및 실행](#가상환경-추가-및-실행)
  * [가상환경 위에 django 및 패키지 설치](#가상환경-위에-django-및-패키지-설치)
  * [requirement.txt](#requirementtxt)
* [3. autoenv](#3-autoenv)
  * [autoenv 설치](#autoenv-설치)
  * [.env 파일 작성 및 실행](#env-파일-작성-및-실행)
* [4. django 프로젝트 생성](#4-django-프로젝트-생성)
* [5. django 프로젝트 app 생성](#5-django-프로젝트-app-생성)
* [reference](#reference)

<!-- tocstop -->
---

# 들어가기

django로 연습 프로젝트를 만들다 보면 항상 처음에 아래 2가지를 진행하게 된다.

1. python 개발환경 세팅
2. django 프로젝트 및 app 생성

명령어를 외우지 못해서 매번 찾아보게 되는데, 이번 기회에 참고하기 쉽도록 정리해두려고 한다.

---

# 1. pyenv
- pyenv (파이썬 버전관리 프로그램) 를 활용하여 원하는 파이썬 버전을 설치한다.

## pyenv 설치
- 파이썬 버전관리 프로그램 (Simple Python Version Management)
- [pyenv 설치](https://github.com/pyenv/pyenv#homebrew-on-mac-os-x)

```shell
# 설치
$ brew update
$ brew install pyenv

#~/.zshrc - zsh을 사용하는 경우
$ atom ~/.zshrc # atom을 통해서 파일에 아래 내용 입력

export PYENV_ROOT=/usr/local/var/pyenv
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

$ source ~/.zshrc #재실행
$ exec "$SHELL" # shell 재실행
```

## pyenv를 활용한 python 설치
- 파이썬 설치 전 필요 패키지 설치
	- https://github.com/yyuu/pyenv/wiki/Common-build-problems

```shell
$ pyenv version
$ pyenv install --list # 설치 가능한 패키지 목록 (파이썬 버전별 목록)
$ pyenv install 3.6.0 # python 설치
$ pyenv shell 3.6.0 # pyhotn 3.6.0으로 shell 실행 > autoenv를 사용하면 별도 지정이 필요 없음
$ python --version
```

- pyenv global 설정을 통해서 기본으로 실행될 python 버전을 설정 가능하다.
(시스템 python에는 영향 없음)

```shell
$ pyenv global 3.5.3
$ python --version
# Python 3.5.3

$ pyenv global system
$ python --version
#Python 2.7.10
```

---

# 2. virtualenv
- virtualenv(독립된 개발환경을 제공해주는 프로그램) 를 활용하여 가상 개발환경을 구축한다.
- 가상환경 위에서 원하는 버전의 django 및 패키지를 설치한다.

## virtualenv 설치
- [virtualenv 설치](https://github.com/pyenv/pyenv-virtualenv)

```shell
# brew로 설치
$ brew install pyenv-virtualenv

# 설치 후 .zshrc 파일에 아래 내용 추가
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## 가상환경 추가 및 실행

```shell
$ pyenv virtualenv 3.6.0 css-3.6.0 # css-3.6.0 이라는 가상환경을 추가
$ pyenv versions # 가상환경 리스트 확인 - .pyenv 폴더 안에 존재

# 가상환경 실행 및 종료
$ pyenv activate css-3.6.0
$ pyenv deactivate
```

## 가상환경 위에 django 및 패키지 설치

```shell
$ pip install django==1.10 # django 설치
$ pip install jupyter # jupyter 설치
$ pip freeze # 설치한 패키지 리스트 확인

# 유용한 패키지 예시

$ pip install django-extensions # settings.py 내 INSTALLED_APPS에 django_extensions 추가 필요
$ pip install "ipython[notebook]"
$ python manage.py shell_plus # 익스텐션 앱을 설치하면 shell_plus 사용가능, 필요한 모델을 자동 import 해줘서 편리함
$ python manage.py shell_plus --notebook # jupyter notebook을 통해서 djnago shell을 사용하면 좀더 친숙한 UI로 볼 수 있고, 이미지 결과를 확인 할 수 있다. 입력 이력을 로그로 남길 수 있음
```

## requirement.txt

- 필요한 라이브러리(ipython, django 등)를 설치하여 개발환경 세팅 후 requirements.txt를 만든다.
- requirements.txt가 있다면 다음 명령을 통해 동일한 파이썬 패키지들을 한번에 설치할 수 있다.

```shell
$ pip3 freeze > requirements.txt  # 패키지 목록을 txt 파일로 만들기
$ pip3 install -r requirements.txt  # 한번에 패키지 설치
```

---

# 3. autoenv
## (추가) local에 가상환경 설정
- pyenv local 명령을 통해서 원하는 디렉토리에 가상환경을 지정할 수 있다. (자동 on/off) 따라서 별도로 아래의 **autoenv를 설치할 필요가 없다!**
- 사용할 폴더로 이동 후 아래 명령을 시행하면 .python-version 파일이 생성된다.

```python
pyenv local fc-python(가상환경이름)
pyenv global <가상환경이름> # 기본으로 사용할 환경 설정
```

## autoenv
- autoenv를 설치하고 프로젝트 폴더에 .env 파일을 만들어 자동으로 가상환경이 실행되도록 만든다.
- autoenv : Directory-based environments, 폴더 안에 .env 파일이 있으면 해당 폴더에 들어갈 때 자동으로 가상환경이 실행된다.

## autoenv 설치
- [autoenv 설치](https://github.com/kennethreitz/autoenv)

```shell
$ brew install autoenv # 설치 (Using Homebrew)
$ echo "source $(brew --prefix autoenv)/activate.sh" >> ~/.zshrc
$ exec "$SHELL" # 재실행
```

## .env 파일 작성 및 실행

```shell
# 프로젝트 폴더로 이동 후
$ touch .env
$ vim .env

# .env 파일에 아래 내용 입력   
$ pyenv activate css-3.6.0 # 원하는 가상환경 이름 (virtualenv로 생성한) 을 입력
$ cd ./ # 나갔다가 다시 들어오면 virtualenv 환경이 켜짐
```

---

# 4. django 프로젝트 생성

```shell
$ django-admin startproject mysite .
# 점 .은 현재 디렉토리에 장고를 설치하라고 스크립트에게 알려준다
```

- setting.py 설정 수정

```shell
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

---

# 5. django 프로젝트 app 생성

```shell
$ python manage.py startapp myapp
```
- setting.py 에 생성한 app 등록

```shell
INSTALLED_APPS = [
    ...
    'myapp',
]
```

---

# reference

- [파이썬 개발환경 세팅하기 – pyenv & virtualenv & autoenv](https://milooy.wordpress.com/2015/07/31/python-set-environments/)
- [pyenv + virtualenv + autoenv 를 통한 Python 개발 환경 구축하기](https://dobest.io/how-to-set-python-dev-env/)
