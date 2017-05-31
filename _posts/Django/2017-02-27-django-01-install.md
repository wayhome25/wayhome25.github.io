---
layout: post
title: django 01. 파이썬 설치 및 환경설정
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 01. 파이썬 설치 및 환경설정
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## 파이썬 3 설치 - Mac OS
- 기본버전은Python2이므로Python3 별도다운로드및설치
- https://www.python.org/downloads/
- Python3 최신버전다운로드(2016년12월3.5.2) 및설치


## 가상환경 설치 및 사용 - virtualenv
- virtualenv은 프로젝트 별로 다른 환경을 사용할 수 있게 한다.
- 가상환경 [장고걸스 참고](https://tutorial.djangogirls.org/ko/django_installation/)
> 장고를 설치하기 전에, 개발 환경을 깔끔하게 관리하는데 큰 도움이 되는 도구를 설치해보겠습니다. 이 단계를 건너뛸 수 있지만, 한번 직접 해보는 것을 추천합니다. 제대로 설치해야 나중에 문제가 발생하지 않거든요!
>
자, 이제부터 가상 환경(virtualenv라고 불러요)을 만들어보겠습니다. Virtualenv는 프로젝트 기초 전부를 Python/Django와 분리시켜줍니다. 다시 말해 웹사이트가 변경되어도 개발 중인 것에 영향을 미치지 않다는 것입니다. 어때요, 깔끔하죠?

### 가상환경 설치

```
mkdir djangogirls
cd djangogirls

python3 -m venv [원하는 이름 (ex. myenv)]
```

### 가상환경 실행
- 가상환경 실행 후에는 콘솔 프롬프트에 (myenv - 설정한 이름)이 표시된다.
- 가상 환경을 시작하고 나면 python이라고만 해도 지정한 버전의 파이썬이 실행되기 때문에 python3 대신 python이라고 입력해도 된다.

```
source myenv/bin/activate

(myvenv) C:\Users\Name\djangogirls>
```

## django 설치 및 테스트  
- 장고설치  [장고걸스 참고](https://tutorial.djangogirls.org/ko/django_installation/)
> 이제 virtualenv 가 시작되었으니, pip를 이용해 장고를 설치할 수 있어요. 콘솔에서 pip install django==1.10를 실행해보세요. (조심하세요. 이퀄기호가 두 개예요: ==).

### 장고 설치

```
pip install django==1.10
```

### 첫번째 django 프로젝트 만들기
> [장고걸스 참고](https://tutorial.djangogirls.org/ko/django_start_project/)

- 장고 프로젝트 생성 :  장고의 기본 골격을 만들어주는 스크립트를 실행
- 장고에서는 디렉토리나 파일 이름이 매우 중요하다. 따라서 경로와 이름을 임의로 변경해서는 안된다. 장고는 중요한 것들을 찾을 수 있게 특정한 구조를 유지해야한다.
- 모든 것은 `가상환경(virtualenv)` 안에서 진행해야 한다.
  - 콘솔창에서 접두어로 (myvenv)가 안보인다면 먼저 virtualenv를 활성화해야 한다.
  - virtualenv 실행방법 (위의 가상환경 실행 참고)

- 원하는 폴더로 이동하여 프로젝트 생성 (점 .은 현재 디렉토리에 장고를 설치하라고 스크립트에게 알려준다)

```
(myvenv) ~/djangogirls$ django-admin startproject mysite .
```

- 생성한 프로젝트 폴더의 구성
  - `manage.py` : 파일 또한 스크립트인데, 사이트 관리를 도와주는 역할을 합니다. 이 스크립트로 다른 설치 작업 없이, 컴퓨터에서 웹 서버를 시작할 수 있습니다.
  - `settings.py` : 웹사이트 설정이 있는 파일입니다.
  - `urls.py` : urlresolver가 사용하는 패턴 목록을 포함

```
djangogirls
├───manage.py
└───mysite
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

### 설정 변경
- `settings.py` 내용 변경

```
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

### 서버 실행

```
python manage.py migrate
$ python manage.py runserver

# 브라우저에서 127.0.0.1:8000 확인
```
<center>
<figure>
<img src="/assets/post-img/django/first-django.png" alt="">
<figcaption>장고프로젝트 서버 실행 화면</figcaption>
</figure>
</center>


## 아톰 패키지 설치

- 편리한 개발을 위해 아톰 에디터에서 별도의 패키지를 설치한다.
- File –Settings –Package 아래  install 에들어가서아래패키지를설치
  - autocomplete-python
  - script
- atom에서 cmd + i 단축키를 통해 파이썬을 실행할 수 있음
- [한글 입력시 발생하는 문제 해결 방법](https://blog.chann.kr/how-to-use-python3-in-atom/)
