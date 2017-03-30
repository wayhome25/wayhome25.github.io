---
layout: post
title: django 06. 두번째 장고앱 2 - 모델만들기
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 06. 두번째 장고앱 2 - 모델만들기
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       


## 모델 만들기
- django는 model이 Database를 저장한다.
- ORM (Object Relational Mapping) : 오브젝트와 데이터베이스를 연결하여 데이터베이스의 CRUD를 쉽게 할 수 있게 함

### 데이터베이스 모델링
- 보통 요구사항 분석이 끝나면 데이터베이스 모델링, 즉 데이터베이스 설계를 하게 된다.
- 여기서 choice 모델의 fk(foreign key) 는 Question 모델의 id를 그대로 가져온다.

<center>
<figure>
<img src="/assets/post-img/django/poll-model.png" alt="poll-model">
<figcaption>모델 구현계획</figcaption>
</figure>
</center>

### models.py 작성 -  필드 세팅
- 앱폴더(polls) 내의 models.py 에 설계한 모델 클래스를 추가
- 모델 클래스 들은 항상 models.Model 클래스를 상속 받는다.

```python
from django.db import models

# Create your models here.
class Question(models.Model): # 항상 Model 클래스를 상속받는다
    #pk 는 자동으로 생성
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # 질문을 삭제 했을 때 연관 항목을 어떻게 할지 설정 - 자동 삭제
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
```

## 모델을 DB에 반영하기
- 아래 명령어를 통해 모델을 DB에 반영한다.
- $ python manage.py makemigrations
- $ python manage.py migrate

```shell
$ python manage.py makemigrations
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK
```
