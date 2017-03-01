---
layout: post
title: django 03. 첫번째 장고앱 6 - shell을 이용한 장고 관리
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 03. 첫번째 장고앱 6 - shell 이용한 장고 관리
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## shell을 이용한 장고 관리
- 터미널에서 `$ python manage.py shell` 입력
- 장고의 기능을 그대로 사용 가능

### 모델클래스명.objects.all()
모델 클래스의 오브젝트를 리스트로 모두 가져온다.

```shell
$ python manage.py shell
>>> from mylotto.models import GuessNumbers
>>> import datetime
>>> GuessNumbers.objects.all()

<QuerySet [<GuessNumbers: siwa - 당첨기원!>, <GuessNumbers: sunshine - 2등도 좋아!>, <GuessNumbers: monkey - 3등도 좋지~>]>
```

### 모델클래스명.objects.get()
모델 클래스의 특정 오브젝트를 가져온다. `.save()`를 통해서 DB에 저장할 수 있다.

```shell
>>> GuessNumbers.objects.get(name = 'siwa')
<GuessNumbers: siwa - 당첨기원!>

>>> g = GuessNumbers.objects.get(name = 'siwa')
>>> g.name
'siwa'
>>> g.name = 'siwaaaaaa'
>>> g.generate()
>>> g.save()
```
