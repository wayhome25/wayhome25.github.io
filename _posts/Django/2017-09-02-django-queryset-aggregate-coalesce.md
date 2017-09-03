---
layout: post
title: Django - Coalesce를 사용하여 aggregate가 None을 반환하는 것을 방지하기
category: Django
tags: [django, annotate, aggregate, Coalesce]
comments: true
---
<br>

django의 aggregate를 활용하면 원하는 필드의 합계, 평균, 최대, 최소값을 구하는 등의 작업을 쉽게 할 수 있다. [참고 : django aggregation](https://docs.djangoproject.com/ko/1.11/topics/db/aggregation/) 예를 들면 아래의 코드를 통해서
WishBook 모델에서 2017년 8월에 생성된 레코드를 필터링하고 price 필드의 합을 구할 수 있다.

```python
>> WishBook.objects.filter(created_at__year='2017', created_at__month='08').aggregate(total=Sum('price'))
# {'total': 85210}
```

문제는 필터링을 할 때 조건에 맞는 레코드가 없는 경우 Sum, Max 등의 결과는 None을 리턴하게 된다. (Count는 0을 리턴한다.)

```python
>> WishBook.objects.filter(created_at__year='2017', created_at__month='09').aggregate(total=Count('price'))
# {'total': 0}

>> WishBook.objects.filter(created_at__year='2017', created_at__month='09').aggregate(total=Sum('price'))
# {'total': None}
```

None을 리터하게되면 필터링 결과값이 없을 때 아래와 같이 표시되는 문제가 발생한다.

![before](https://i.imgur.com/U7slYy6.png)

이를 해결하려면 크게 2가지 방법을 사용할 수 있다.

- 1) **A or B를 활용하여 A가 null 인 경우 B를 리턴하기**
- 별도의 임포트가 필요하지 않다.

```python
total_price = WishBook.objects.filter(created_at__year='2017', created_at__month='09').aggregate(total=Sum('price'))['total'] or 0
```

- 2) **Coalesce(A, B, C..)를 활용하여 왼쪽부터 인자값을 검사하고 null이 아닌 첫번째 값을 리턴하기**
- [Coalesce](https://docs.djangoproject.com/ko/1.11/ref/models/database-functions/#coalesce)는 Django 1.8 부터 지원되고, django.db.models.functions에서 임포트하여 사용할 수 있다.
- 위의 1) 방법은 별도의 임포트가 필요 없기 때문에 간편하고, 2) 방법은 null일 가능성이 있는 후보들이 여러개일때 사용하면 편리하겠다는 생각이 든다.

```python
from django.db.models.functions import Coalesce

total_price = cls.objects.filter(created_at__year=year, created_at__month=month).aggregate(total=Coalesce(Sum('price'), 0))['total']
```

Coalesce는 [SQL COALESCE](https://docs.microsoft.com/ko-kr/sql/t-sql/language-elements/coalesce-transact-sql) 함수와 동일한 기능을 한다고 한다. Coalesce(a, b, c, d, 0)와 같이 2개 이상의 인자를 받고, 왼쪽부터 차례대로 검사하여 null이 아닌 첫번째 값을 리턴한다. 이 경우 a, b, c, d 가 모두 None인 경우 마지막 값인 0을 리턴한다.

Django 공식문서를 보면 아래와 같이 활용이 가능하다.

```python
>>> # Get a screen name from least to most public
>>> from django.db.models import Sum, Value as V
>>> from django.db.models.functions import Coalesce
>>> Author.objects.create(name='Margaret Smith', goes_by='Maggie')
>>> author = Author.objects.annotate(
...    screen_name=Coalesce('alias', 'goes_by', 'name')).get()
>>> print(author.screen_name)
Maggie

>>> # Prevent an aggregate Sum() from returning None
>>> aggregated = Author.objects.aggregate(
...    combined_age=Coalesce(Sum('age'), V(0)),
...    combined_age_default=Sum('age'))
>>> print(aggregated['combined_age'])
0
>>> print(aggregated['combined_age_default'])
None
```
