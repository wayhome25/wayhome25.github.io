---
layout: post
title: django 06. 두번째 장고앱 3 - shell로 모델 조작하기
category: Django
tags: [python, 파이썬, Django, shell]
comments: true
---
# django 06. 두번째 장고앱 3 - Shell로 모델 조작하기
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       

## models.py 코드 - Question 모델클래스

```python
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model): # 항상 Model 클래스를 상속받는다
    #pk 는 자동으로 생성
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 날짜가 최근 24시간 이내 작성된거라면 True를 리턴한다.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

## Shell을 사용하여 Question 클래스 모델에 데이터를 추가, 저장한다.

- 모델클래스에 `__Str__` 메소드를 오버라이딩하여 해당 클래스의 대표 이름 값을 설정할 수 있다.
- timedelta 클래스 : 시간의 연산을 가능하게 해주는 클래스 (datetime 모듈의 클래스)

```
>>> python manage.py shell #shell 실행
>>> from polls.models import Question, Chice #모델클래스 임포트
>>> from django.utils import timezone #타임존 모듈 임포트
>>> q = Question(question_text='최고의 고기는?', pub_date = timezone.now()) # 데이터추가
>>> q.save() # 데이터 저장
>>> q.objects.all() # 모델 데이터 전체 출력
```

### 모델클래스.objects.filter()
- 복수 검색, range 검색, 부분 검색, 범위 검색
- 조건에 맞는 데이터를 리스트로 가져온다. (하나가 나오더라도 리스트로 감싼다)
- 검색 조건 :

```
>>> Question.objects.filter(id=1)
<QuerySet [<Question: 최고의 고기는?>]> # 리스트로 출력

>>> Question.objects.filter(pk=1) # id=1 과 동일
>>> Question.objects.filter(question_text__startswith = '최') # question_text가 '최'로 시작하는 데이터
```

## models.py 코드 - Choice 모델클래스

```python
from django.db import models
from django.utils import timezone
import datetime

class Choice(models.Model):
    # 질문을 삭제 했을 때 연관 항목을 어떻게 할지 설정 - 자동 삭제
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
```

## Shell을 사용하여 Choice 클래스 모델에 데이터를 추가, 저장한다.
- Question 클래스 모델과는 다른 방식으로 데이터를 추가한다.
- `Choice는 Question 오브젝트에 연관 지어진 오브젝트이다.`
- choice_set을 Question 오브젝트로 부터 만들어줘야 한다. (소문자 주의)

```
>>> q
<Question: 최고의 고기는?>
>>> q.choice_set.all() # 모델 설계시에 이미 연결을 했기 때문에 choice_set이 존재한다.
<QuerySet []>
>>> q.choice_set.create() #q(최고의 고기라는 데이터)에 연결된 choice 오브젝트 1개를 만든다.
>>> q.choice_set.create(choice_text = '돼지')
>>> q.choice_set.create(choice_text = '닭')
>>> q.choice_set.create(choice_text = '소')

>>> q.choice_set.all()
<QuerySet [<Choice: 돼지>, <Choice: 치킨>, <Choice: 소>]>

>>> Choice.objects.all() # 이렇게는 연관성을 알 수 없어서 잘 사용하지 않는다.
<QuerySet [<Choice: 돼지>, <Choice: 치킨>, <Choice: 소>, <Choice: 짜장>, <Choice: 짬뽕>]>
```
