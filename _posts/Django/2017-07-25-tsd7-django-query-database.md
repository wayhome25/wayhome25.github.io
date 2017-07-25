---
layout: post
title: two scoops of django - 장고 쿼리와 데이터베이스 레이어
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

> #### ORM이 뭔가요? (Object Relational Mapping)
> - OOP 언어와 데이터를 다루는 RDBMS 와의 상이한 시스템을 매핑하여, 데이터 관련 OOP 프로그래밍을 쉽게 하도록 도와주는 기술
> - Model Class를 통해서 객체를 만들고 이 객체를 통해서 DB에 접근한다.
> - ~~SQL을 몰라도 데이터를 알고싶다!~~
> ![Django-Models](http://i.imgur.com/cxaR4rT.png)
> 출처 [The Django Book](https://djangobook.com/tutorials/django-overview/)
>        
> #### 쿼리셋 (QuerySet)이 뭔가요?
>```python
> >>> from .models import Book
> >>> Book.objects.all() # Book 모델(테이블)의 모든 데이터를 가져오기
> <QuerySet [<Book: 책 제목1>, <Book: 책 제목2>]>
>```
> - objects : Model Manager,  DB와 Django Model 사이의 Query Operation(질의연산) 인터페이스 역할
> - objects를 사용하여 다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체가 QuerySet
>
> #### 참고자료
> - [Django ORM 왜 어렵게 느껴질까?](https://www.slideshare.net/perhapsspy/django-orm-67523180)
> - [QnA blog using Django - ORM, 회원가입, 로그인/로그아웃](https://www.slideshare.net/DustinJunginSeoul/qna-blog-using-django-orm)
> - [Making queries (공식문서)](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
> - [QuerySet API reference (공식문서)](https://docs.djangoproject.com/en/1.11/ref/models/querysets/)

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

---

## 7.4 고급 쿼리 도구 이용하기
- 장고의 ORM은 강력하지만 모든 경우를 완벽하게 처리할 수 있지는 않다.
- 따라서 장고의 고급 쿼리 도구를 이용하여 데이터베이스를 통한 데이터 가공을 시도할 수 있다.
- 고급 쿼리도구를 사용하면 파이썬을 통한 데이터 가공보다 성능이 좋고 안전하다.

### 7.4.1 쿼리 표현식
- 쿼리 표현식을 꼭 익혀두자. 프로젝트의 안전성과 성능을 대폭 향상시켜 줄 것이다.
- [Query Expressions (공식문서)](https://docs.djangoproject.com/en/1.11/ref/models/expressions/)
- **나쁜예제**
  - 모든 고객 레코드에 대해서 for loop가 돌고있다. => 매우 느리고, 메모리 소모가 크다
  - 경합상황 (race condition)에 직면할 가능성이 크다. => 데이터 분실 우려
  > 경합상황 : 다중 프로그래밍 시스템이나 다중 처리기 시스템에서 두 명령어가 동시에 같은 기억 장소를 액세스할 때 그들 사이의 경쟁에 의해 수행 결과를 예측할 수 없게 되는 것.

```python
# 절대 따라하지 말 것
from models.customers import Customer

customers = []
for customer in Customer.objects.iterator():
  if customer.scoops_ordered> customer.store_visits:
    customers.append(customer)
```

- **수정 후**
  - 쿼리표현식을 통해서 코드들이 서로 경합을 펼치는 상황을 피할 수 있다.

```python
from django.db.models import F
from models.customers import Customer

customers = Customer.objects.filter(scoops_ordered__gt=F('store_visits'))
```

- 위 코드 쿼리표현식 중 [F() expressions](https://docs.djangoproject.com/en/1.11/ref/models/expressions/#f-expressions)의 기능
  - 파이썬이 아닌 데이터베이스 자체 내애서 해당 조건을 비교하는 기능을 가진다.
  - 경합조건을 피할 수 있다.[Avoiding race conditions using F](https://docs.djangoproject.com/en/1.10/ref/models/expressions/#avoiding-race-conditions-using-f)
  - 위 코드에서 내부적으로 다음과 같은 SQL문을 생성한다.  

```sql
SELECT * from customers_customer where scoops_ordered > store_visits
```

![스크린샷 2017-07-25 오후 4.49.31](http://i.imgur.com/fd11dGS.png)
[출처 - school of web](http://schoolofweb.net/blog/posts/%EB%82%98%EC%9D%98-%EC%B2%AB-django-%EC%95%B1-%EB%A7%8C%EB%93%A4%EA%B8%B0-part-4-1/)

### 7.4.2 데이터베이스 함수들
- 장고 1.8 부터 일반적인 데이터베이스 함수를 이용할 수 있다.
- UPPER(), LOWER(), COALESCE(), CONCAT(), LENGTH(), SUBSTR()
- 저자가 가장 좋아하는 기능이다. 왜냐하면
  - 쉽고 간결하다.
  - 성능이 굉장히 향상된다. (파이썬으로 데이터 처리속도 < 데이터베이스 내에서 데이터 처리속도)
  - 데이터베이스 함수는 장고 ORM의 쿼리 표현식이기도 하다.
- [Database Functions (공식문서)](https://docs.djangoproject.com/en/1.11/ref/models/database-functions/)

---

## 7.5 필수 불가결한 상황이 아니라면 로우 SQL은 지양하자
- ORM은 생산성이 높다.
- ORM은 단순 쿼리를 만들어 내는 것에 더해서 모델에 대한 접근, 업데이트를 할 때 유효성 검사와 보안을 제공한다.
- 로우 SQL을 사용하면 앱의 이식성이 떨어질 수 있고, 다른 종류의 DB로 마이그레이션이 어려울 수 있다.
- 그럼 언제 로우 SQL을 사용하나요?
  => SQL을 직접 이용함으로써 코드가 월등히 간결해지고, 단축되는 경우에만 사용하자.

---

## 7.6 필요에 따라 인덱스를 이용하자
- 모델의 필드 옵션으로 db_index를 추가하면 해당 필드에 대해서 Database index가 생성된다.
- 처음에는 인덱스 없이 시작하고 필요에 따라서 하나하나 추가하는 것을 추천한다.
  - 인덱스가 빈번하게 이용될 때 (쿼리의 10~25% 사이) => 생성된 SQL 문에서 WHERE 절과 ORDER_BY 절을 세심하게 살펴보기
  - 인덱싱을 통해서 성능이 향상되는지 테스트 가능할 때
- PostgreSQL의 경우 [pg_stat_activity](http://blog.gaerae.com/2015/09/postgresql-pg-stat-activity.html) 를 통해서 어떤 인덱스가 사용 중인지 확인 가능하다.

---

## 7.7 트랜잭션 (Transactions)
<br>
![스크린샷 2017-07-25 오후 7.40.46](http://i.imgur.com/ICRjz9A.png)

- Transaction : (명사) 처리, 처리과정
> 컴퓨터 과학분야에 트랜잭션은 "쪼개질 수 없는 업무처리의 단위"를 의미

- 데이터베이스 충돌을 해결하기 위해서 둘 또는 그 이상의 데이터베이스 업데이트를 **단일화된 작업** 으로 처리하는 기법
- 하나의 수정작업(update)가 실패하면 트랜젝션 상의 모든 업데이트가 실패 이전 상태로 복구된다.

<br>
![acid](http://i.imgur.com/vZGwKQp.gif)

- 트랜젝션의 특성 (ACID)
  - 원자성 (Atomic)
  - 일관성 (Consistent)
  - 독립성 (Isolated)
  - 지속성 (Durable)
- 장고는 1.8 부터 사용하기 쉬운 트랜잭션 메커니즘을 제공

> **데코레이터(decorator)를 이용한 트랜잭션 예시** ([출처](https://blueshw.github.io/2016/01/16/2016-01-16-django-migration/))

```python
from django.db import transaction

@transaction.atomic
def transaction_test1(arg1, arg2):
    # start transaction
    a.save()

    b.save()
    # end transaction
```

> **with 명령어를 이용한 트랜잭션 예시** ([출처](https://blueshw.github.io/2016/01/16/2016-01-16-django-migration/))

```python
from django.db import transaction
def transaction_test2(arg1, arg2):

    a.save()    # 항상 save 처리됨, 예외가 발생할 경우 에러 발생

    with transaction.atomic():
        # start transaction
        b.save()
        c.save()
        # end transaction
```

- [참고 - 트랜잭션이란 도대체 뭐란 말인가!](http://egloos.zum.com/springmvc/v/495798)
- [참고 - 장고 트랜잭션 활용](https://blueshw.github.io/2016/01/16/2016-01-16-django-migration/)
- [참고 - 트랜잭션](http://www.incodom.kr/%ED%8A%B8%EB%9E%9C%EC%9E%AD%EC%85%98)

### 7.7.1 각각의 HTTP 요청을 트랜잭션으로 처리하라
- 아래와 같은 설정을 통해서 **읽기 데이터를 포함한 모든 요청이 트랜잭션으로** 처리되게 할 수 있다.
  - 장점 : 뷰에서의 모든 데이터베이스 쿼리가 보호되는 안정성을 얻을 수 있다.
  - 단점 : 성능 저하를 가져올 수 있다.
- 쓰기 작업이 많은 프로젝트의 초기 구성에서 데이터베이스 무결성을 유지하는데 효과적인 구성
- 특정 루틴을 설정에서 제외시키고 싶다면 뷰 함수에서 transaction.non_atomic_requests()로 데코레이팅한다.
- 의료정보나 금융 정보를 다루는 프로젝트의 경우 트랜잭션 무결성 보다는 이벤트 일관성에 초점을 맞추어 구성하게 된다.

```python
# settings/base.py

DATABASE = {
  'default': {
    #...생략
    'ATOMIC_REQUESTS': True,
  }
}
```

### 7.7.2 명시적인 트랜잭션 선언
- 사이트 성능을 개선하는 방법 중 하나
- 트랜젝션에서 어떤 뷰와 비지니스 로직이 하나로 엮여 있는지 명시해 주는 것 (개발 시간이 오래 걸림)
- 대부분의 사이트는 ATOMIC_REQUESTS 설정으로 충분하다.
- 트랜잭션이 필요한 장고 ORM 구분
- 독립적인 ORM 메서드 호출은 이미 내부적으로 트랜잭션을 이용하고 있다. 대신 여러 ORM 메서드 들을 뷰나 함수 내에서 호출할 때 트랜잭션을 이용하는게 좋다.

|       목적      |                                 ORM 메서드                                 | 트랜잭션을 이용? |
|:---------------:|:--------------------------------------------------------------------------:|:-------------------------:|
|   데이터 생성     | .create(), .bulk_create(), .get_or_create()                                |             O             |
| 데이터 가져오기   | .get(), .filter(), .count(), .iterate(), .exist(), .exclude() 등 |             X             |
| 데이터 수정하기    | .update()                                                                  |             O             |
|  데이터 지우기    | .delete()                                                                  |             O             |


### 7.7.3 django.http.StreamingHttpResponse와 트랜잭션
- 뷰가 django.http.StreamingHttpResponse를 반환한다면 중간에 트랜잭션 에러를 처리하기는 불가능하다.
- 이를 해결하려면 아래와 같은 방법이 있다.
  - 'ATOMIC_REQUESTS'설정을 False 로 설정하고 명시적 트랜잭션 선언을 검토
  - 해당 뷰를 django.db.transaction.non_atomic_requests 데코레이터로 감싸기

### 7.7.4 MySQL 에서의 트랜잭션
- MySQL 데이터베이스 타입에 따라서 트랜잭션 지원 여부가 달라진다. (InnoDB - 지원함,  MyISAM - 지원안함)
- 트랜잭션을 지원하지 않는다면, ATOMIC_REQUESTS 설정에 상관없이 항상 오토커밋 모드로 작동한다.
