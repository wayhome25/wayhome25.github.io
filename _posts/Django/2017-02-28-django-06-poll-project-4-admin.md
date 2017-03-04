---
layout: post
title: django 06. 두번째 장고앱 4 - admin 페이지 사용하기
category: Django
tags: [python, 파이썬, Django, shell]
comments: true
---
# django 06. 두번째 장고앱 4 - admin 페이지 사용하기
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       

## admin 페이지를 통해서 모델 클래스에 데이터를 추가, 저장한다.

### superuser 생성 및 admin.py 등록

1. `manage.py createsuperuser` 명령어를 통해서 계정 생성
2. `admin.py`에 모델클래스 추가

```python
from .models import Question, Choice


admin.site.register(Question)
admin.site.register(Choice)
```

## admin 사이트에서 데이터 등록
- admin 사이트에서 Question 모델 클래스와 Choice 모델 클래스에 데이터를 추가한다. (http://127.0.0.1:8000/admin/)
- Choice 모델클래스는 Question id를 foreignKey로 갖고 있기 때문에 데이터 입력시 Question 데이터가 선택지로 나온다.

```python
question = models.foreignKey(Question, on_delete = models.CASCADE)
```

<center>
<figure>
<img src="/assets/post-img/django/admin-choice.png" alt="admin-choice">
<figcaption>admin 데이터 입력화면</figcaption>
</figure>
</center>
