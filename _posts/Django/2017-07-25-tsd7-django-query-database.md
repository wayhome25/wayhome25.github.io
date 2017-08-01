---
layout: post
title: Django - ORM, 쿼리셋, 예외처리
category: Django
tags: [python, Django, orm, database]
comments: true
---
> [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) 7장을 읽고 정리한 내용입니다.     
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

# 7장 쿼리와 데이터베이스 레이어

- 장고에서는 여러 종류의 데이터를 데이터베이스 종류와는 독립적인 형태로 객체화 한다. (ORM)
- 그리고 생성된 객체에는 상호 작용할 수 있는 메서드 세트를 제공한다. (Model Manager)
- ORM은 훌륭하지만 때때로 예상과 다른 현상이 발생하기도 한다.
- Django 이용방법을 배운다는 것은 이런 예상과는 다른 현상을 이해해 나가는 과정이라고 할 수 있다.
- Chapter7 에서는 ORM이 예상과 다르게 동작하는 다양한 경우들을 살펴본다.

## ORM, QuerySet

### ORM이 뭔가요? (Object Relational Mapping)
- OOP 언어와 데이터를 다루는 RDBMS 와의 상이한 시스템을 매핑하여, 데이터 관련 OOP 프로그래밍을 쉽게 하도록 도와주는 기술
- Model Class를 통해서 객체를 만들고 이 객체를 통해서 DB에 접근한다.
- ~~SQL을 몰라도 데이터를 알고싶다!~~
![Django-Models](http://i.imgur.com/cxaR4rT.png)
출처 [The Django Book](https://djangobook.com/tutorials/django-overview/)

### 쿼리셋 (QuerySet)이 뭔가요?
```python
>>> from .models import Book
>>> Book.objects.all() # Book 모델(테이블)의 모든 데이터를 가져오기
<QuerySet [<Book: 책 제목1>, <Book: 책 제목2>]>
```
- objects : Model Manager,  DB와 Django Model 사이의 Query Operation(질의연산) 인터페이스 역할
- objects를 사용하여 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체가 QuerySet

### 참고자료
- [Django ORM 왜 어렵게 느껴질까?](https://www.slideshare.net/perhapsspy/django-orm-67523180)
- [QnA blog using Django - ORM, 회원가입, 로그인/로그아웃](https://www.slideshare.net/DustinJunginSeoul/qna-blog-using-django-orm)
- [Making queries (공식문서)](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
- [QuerySet API reference (공식문서)](https://docs.djangoproject.com/en/1.11/ref/models/querysets/)

---

## 7.1 단일 객체에서 get_object_or_404() 이용하기
- 상세 페이지 view에서는 get() 대신에 get_object_or_404()를 이용하자
- 왜요? try-except 블록으로 예외처리를 할 필요가 없습니다
- 단, get_object_or_404()는 뷰에서만 사용하자!

```python
>>> Book.objects.get(title="없는 책")
DoesNotExist: Book matching query does not exist.

>>> from django.shortcuts import get_object_or_404
>>> get_object_or_404(Book, title="없는 책")
Http404: No Book matches the given query.
```

---

## 7.2 예외를 일으킬 수 있는 쿼리를 주의하자
- get_object_or_404()를 사용하면 예외처리가 필요없다.
- 하지만, 그외의 경우에는 try-except를 이용한 예외처리가 필요하다. 아래의 예외 처리 팁 몇 가지를 살펴보자.  


### 7.2.1 ObjectDoesNotExist vs DoesNotExist
- ObjectDoesNotExist : 모든 모델 객체에서 이용 가능 (import 필요)
- DoesNotExist : 특정 모델에서만 이용 가능

```python
from django.core.exceptions import ObjectDoesNotExist

from flavors.models import flavor
from store.exceptions import OutOfStock

def list_flavor_line_item(sku):
  try:
    return Flavor.objects.get(sku=sku, quantity__gt=0)
  except Flavor.DoesNotExist:
    msg = "{} 재고가 없습니다. ".format(sku)
    raise OutOfStock(msg)

def list_any_line_item(model, sku):
  try:
    return model.objects.get(sku=sku, quantity__gt=0)
  except ObjectDoesNotExist:
    msg = "{} 재고가 없습니다.".format(sku)
    raise OutOfStock(msg)
```

### 7.2.2 여러 개의 객체가 반환되었을 때
- 쿼리가 하나 이상의 객체를 반환할 수 있다면 MultipleObjectsReturned 예외처리를 통해 에러로그를 남기거나 원하는 방향으로 처리할 수 있다.

```python
from flavors.models import Flavor
from store.exceptions import OutOfStock, CorruptedDatabase

def list_flavor_line_item(sku):
  try:
    return Flavor.objects.get(sku=sku, quantity__gt=0)
  except Flavor.DoesNotExist:
    msg = "{} 재고가 없습니다.".format(sku)
    raise OutOfStock(msg)
  except Flavor.MultipleObjectsReturned:
    msg = "여러개의 아이템이 SKU {}를 갖고 있습니다. 고쳐주세요!"
    raise CorruptedDatabase(msg)
```

---

## 7.3 쿼리를 좀 더 명확하게 하기 위해 지연 연산 이용하기
- ORM을 활용할 때는 코드를 명확하게 작성해야 유지보수가 편해진다.
- **나쁜예시**

```python
# 절대 따라하지 말자!
from django.models import Q

from promos.models import Promo

def fun_function(**kwargs):
  """유효한 아이스크림 프로모션 찾기"""
  # 너무 길게 작성된 쿼리 체인이 화면이나 페이지를 넘겨 버리게 되므로 좋지 않다.
  return Promo.objects.active().filter(Q(name__startswith=name)|Q(description__icontains=name))
```

> Promo 모델 중에서 active 메소드로 리턴된 레코드 중에서 name 값이 name으로 시작하거나, description 값 중에 name이 포함되어 있는 레코드를 모두 가져와줘!

- **지연연산 (Lazy Evaluation)** 을 활용하여 장고 코드를 좀 더 깔끔하게 만들 수 있다.
- 지연연산?
  - 데이터가 정말로 필요하기 전 까지는 장고가 SQL을 호출하지 않는 특징
  - 따라서 ORM 메소드와 함수를 얼마든지 연결해서 코드를 쓸 수 있다.
  - 한 줄에 길게 쓰는 대신에 여러줄에 나눠서 쓰면 **가독성을 엄청나게 향상시키며, 유지보수를 쉽게 해준다.**
- **수정 후**

```python
from django.models import Q

from promos.models import Promo

def fun_function(**kwargs):
  """유효한 아이스크림 프로모션 찾기"""
  results = Promo.objects.active()
  results = results.filter(
              Q(name__startswith=name)|
              Q(description__icontains=name)
              )             
  results = results.exclude(status='melted')
  results = results.select_related('flavors')
  return results
```
> - Promo 모델 중에서 active 메소드로 리턴된 모든 레코드
> - 그 중에서 name 값이 name으로 시작하거나, description 값 중에 name이 포함되어 있는 모든 레코드
> - 그 중에서 status가 'melted'인 레코드는 제외
> - Foreign Key 항목인 flavors도 함께 가져와서 리턴
