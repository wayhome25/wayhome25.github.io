---
layout: post
title: Django 기본 06 - shell, Jupyter Notebook, ipython
category: Django
tags: [python, Django, shell]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# Django Shell
- 장고 프로젝트 설정이 로딩된 파이썬 쉘
- 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 접근 불가
- 프로젝트 내의 각종 모듈 패키지를 활용하기 위해서는 장고 shell를 통해서 접근해야한다.
- 장고 쉘 실행방법
```shell
$ python3 manage.py shell
```

## Jupyter Notebook
- `django-extensions` 설치
```shell
$ pip install django-extensions
```
- settings.py 내 INSTALLED_APPS에 `django_extensions` 추가 (장고 익스텐션은 장고 app 구조로 되어있어서 현재 프로젝트 내에서 해당 앱을 활성화시켜야 한다)
```python
INSTALLED_APPS = [
  'django_extensions',
]
```
- `ipython, jupyter notebook` 설치
```shell
$ pip3 install "ipython[notebook]"
```

### shell_plus
```shell
$ python3 manage.py shell_plus
```
- 익스텐션 앱을 설치하면 shell_plus 사용가능, 필요한 모델을 자동 import 해줘서 편리함

<center>
 <figure>
 <img src="/assets/post-img/django/shell_plus.png" alt="views">
 <figcaption>shell_plus 실행시 필요한 모델은 자동 import한다.</figcaption>
 </figure>
 </center>

### jupyter notebook
```shell
$ python manage.py shell_plus --notebook
```
- jupyter notebook을 통해서 djnago shell을 사용하면 좀더 친숙한 UI로 볼 수 있고, 이미지 결과를 확인 할 수 있다. 입력 이력을 로그로 남길 수 있다.
- 초반에는 jupyter notebook 을 사용하는 것을 추천한다.

<center>
 <figure>
 <img src="/assets/post-img/django/jupyter_notebook.png" alt="views">
 <figcaption></figcaption>
 </figure>
 </center>
