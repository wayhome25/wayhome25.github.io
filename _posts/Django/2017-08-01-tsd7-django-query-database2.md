---
layout: post
title: Django - 쿼리 표현식, DB 트랜잭션
category: Django
tags: [python, Django, orm, database]
comments: true
---
> [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) 7장을 읽고 정리한 내용입니다.     
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

# 7장 쿼리와 데이터베이스 레이어

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
