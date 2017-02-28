---
layout: post
title: django 03. 첫번째 장고앱 4 - 장고 테스트 코드 작성
category: Django
tags: [python, 파이썬, Django, 테스트]
comments: true
---
# django 03. 첫번째 장고앱 4 - 장고 테스트 코드 작성
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## 장고 테스트 코드 작성
GuessNumbers 모델 클래스의 generate 메소드를 테스트 해본다.  

### test.py 활용 (위치 : app 폴더 - mylotto)
- 모델 클래스 GuessNumbers의 generate 메소드를 테스트 하기 위해 test.py 파일에 아래와 같이 테스트 코드를 작성한다.

```python
from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='monkey', text='1등만세!')
        g.generate()
        print(g.update_date)
        print(g.lottos)
        self.assertTrue(len(g.lottos) > 20) #성공실패 테스트 루틴은 assert 메소드를 사용한다.

```

- test.py 실행방법 `$ python manage.py test`

```
$ python manage.py test

Creating test database for alias 'default'...
2017-02-28 10:23:22.635449+00:00
[4, 14, 16, 22, 28, 33]
[11, 12, 16, 23, 28, 42]
[1, 2, 14, 30, 38, 42]
[6, 7, 14, 25, 27, 43]
[15, 19, 24, 26, 35, 39]

.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```
