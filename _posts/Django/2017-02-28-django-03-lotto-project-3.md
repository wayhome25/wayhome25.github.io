---
layout: post
title: django 03. 첫번째 장고앱 3 - MODEL 클래스 만들기, admin site 에 Model 등록
category: Django
tags: [python, 파이썬, Django, model]
comments: true
---
# django 03. 첫번째 장고앱 3 - MODEL 클래스 만들기, admin site 에 Model 등록
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

##  MODEL 클래스 만들기
장고는 모델과 데이터베이스를 연결해서 데이터베이스에 영구적으로 데이터를 저장하게 되는데 이를 `ORM ( Object – Relational Mapping)`이라고 합니다.

- Model은 M(model)T(template)V(view)의 M
- DB에 데이터를 저장하거나 불러오기 위해서 모델을 사용한다.
- 모델은 클래스로 만들어 준다.   
- models.py 작성 후, 장고에게 모델을 만들었다는 걸 알려준다.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

- models.py 내에 GuessNumbers 클래스 작성 예시

```python
from django.db import models
from djang.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model): #슈퍼클래스 models의 하위클래스 Model을 상속받는다.
    # 필요한 데이터 정의
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255, default = '[1, 2, 3, 4, 5, 6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(defaul = 5)
    update_date = models.DateTimeField()

    # 메소드 정의
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46)) #[1, 2, 3.....44, 45]
        for _ in range(0, self.num_lotto): # self.num_lotto 수만큼 반복해서 아래를 수행한다.
            random.shuffle(origin) # origin 리스트 순서를 섞는다.
            guess = origin[:6] #index번호 0부터 5 까지를 뽑아낸다.
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()
        self.save() # 오브젝트를 db에 저장
```

## admin site 에 Model 등록하기
어드민을 이용하여 model에 있는 데이터 확인하기

- http://127.0.0.1:8000/admin/ 접속
- 로그인을 위한 슈퍼유저(superuser) 생성

```
$ python manage.py createsuperuser
```

- `admin.py` 에 GuessNumbers 모델 클래스 등록
- 모델 클래스 등록 후, 어드민 사이트에 재접속하면 해당 모델 클래스 확인 가능


```
from mylotto.models import GuessNumbers

admin.site.register(GuessNumbers)
```
- 어드민 사이트에서 데이터 추가

<center>
<figure>
<img src="/assets/post-img/django/register.png" alt="">
<figcaption>어드민 사이트 - 모델 클래스 데이터 등록 화면</figcaption>
</figure>
</center>

- 해당 모델 클래스(GuessNumbers)에 `__str__` 메소드를 추가하여 어드민 내 표시방법 변경

```python
def __str__(self):
    return '%s - %s' % (self.name, self.text)
```
