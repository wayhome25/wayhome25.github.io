---
layout: post
title: django 03. 첫번째 장고앱 1 - MTV, 프로젝트 및 앱 생성
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 03. 첫번째 장고앱 - 로또 만들기, 프로젝트 및 앱 생성
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## Django and MTV
- MTV
  - Model
  - Template
  - View

  <center>
  <figure>
  <img src="/assets/post-img/django/mtv.png" alt="">
  <figcaption>장고와 MTV</figcaption>
  </figure>
  </center>

- `Routing` (-urls.py) : URL 파싱 후 View 에 전달
- `View` :
  - URL 라우팅 규칙을 처리하는 오브젝트 - URL 디스패처   
    (MVC의 V와 상관이 없다. Template이 오히려 V에 가깝다. Controller도 아니다. Controller의 역할은 장고 자체가 수행한다.)
  - Model로 부터 데이터를 수집 (데이터는 오브젝트(Dictionary) 형태로 전달)
  - 수집한 데이터 오브젝트는 Template으로 처리
- `Template` :
  - html, presentation layer 담당
- `Model` : Model 오브젝트는 DB 조작을 쉽게 해준다. ORM (Object Relational Model)
- `DB` : Data 저장소, persistent 하게 데이터를 읽고, 쓰는데 Model을 사용한다.

<center>
 <figure>
 <img src="/assets/post-img/django/django_overview.png" alt="views">
 <figcaption></figcaption>
 </figure>
 </center>
- 참고자료출처 : [AskDjango](https://nomade.kr/vod/django/53/)

## 프로젝트 및 앱 생성
1. 프로젝트용 가상환경 (virtualenv) 설치
2. 가상환경 실행
3. 설치된 패키지 확인
4. 장고 설치
5. 프로젝트 생성
6. setting.py 수정
7. app 생성
8. settingp.py 등록
9. server 실행

```
<!-- 1. 프로젝트용 가상환경 (virtualenv) 설치 -->
$ python3 -m venv lotto

<!-- 2. 가상환경 (virtualenv) 실행 -->
$ source lotto/bin/activate

<!-- 3. 설치된 패키지 확인 -->
$ pip freeze

<!-- 4. 장고 설치 -->
$ pip install django==1.10

<!-- 홈 디렉토리 이동 -->
$ cd ~

<!-- 5. 원하는 폴더에서 프로젝트 생성 -->
$ django-admin startproject lotto

<!-- 6. setting.py 수정  -->
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
<!-- 관리를 편하게 하기 위해서 설정하는 부분  -->

<!-- 7. app 생성 -->
$ python manage.py startapp mylotto

<!-- 8. setting.py 등록 -->
INSTALLED_APPS = [
    'mylotto',  /*admin 위에 등록해야한다*/
    .....
]

<!-- 9. 서버 실행 -->
$ python manage.py runserver
Starting development server at http://127.0.0.1:8000/

```

- 서버 실행시 `Error: That port is already in use.` 에러가 발생하는 경우,    
  아래 명령어를 통해서 해결할 수 있다. [참고](http://stackoverflow.com/questions/20239232/error-that-port-is-already-in-use)

```shell
$ sudo lsof -t -i tcp:8000 | xargs kill -9
```
