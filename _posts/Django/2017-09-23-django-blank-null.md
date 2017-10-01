---
layout: post
title: (번역) Django Tips &#35;8 Blank or Null?
category: Django
tags: [django, model, blank, null, field, migration]
comments: true
---
<br>

> 장고를 공부하면서 많은 도움을 받고 있는 [simple is better than complex](https://simpleisbetterthancomplex.com/)의 [Django Tips #8 Blank or Null?](https://simpleisbetterthancomplex.com/tips/2016/07/25/django-tip-8-blank-or-null.html) 번역글입니다. 기분좋게 선뜻 번역을 허락해준 [Vitor](https://github.com/vitorfs)에게 감사드립니다.

<br>
![featured-post-image](https://i.imgur.com/sky2CPv.jpg)
<br>

장고 모델 API는 많은 개발자들이 헷갈려하는  **null** 과 **blank** 라는 2가지 비슷한 옵션을 제공한다. 내가 처음 장고를 시작했을 때, 나는 둘의 차이점에 대해서 설명할 수 없었고 항상 둘 다 사용하곤 했다. 그리고 때때로 부적절하게 사용하기도 했다.

이름에서 알 수 있는 것 처럼 이 두가지는 거의 비슷한 역할을 하지만 차이점도 있다.

- **Null** : DB와 관련되어 있다. (database-related) 주어진 데이터베이스 컬럼이 null 값을 가질 것인지 아닌지를 정의한다.
- **Blank** : 유효성과 관련되어 있다. (validation-related) `form.is_valid()`가 호출될 때 폼 유효성 검사에 사용된다.

그러므로 즉, `null=True, blank=False` 옵션을 가진 필드를 정의하는 것에는 문제가 없다. 이는 DB레벨에서는 해당 필드가 **NULL** 될 수 있지만, application 레벨에서는 **required** 필드인 것을 의미한다.

자, 개발자들이 가장 실수하는 부분은 `CharField`, `TextField`와 같은 문자열 기반 필드에 `null=True`를 정의하는 것이다. 이 같은 실수를 피해야한다. 그렇지 않으면 "데이터 없음"에 대해 두 가지 값, 즉 **None** 과 **빈 문자열** 을 갖게된다. "데이터 없음"에 대해 두 가지 값을 갖는 것은 중복이다. 그리고 Null이 아닌 빈 문자열을 사용하는 것이 장고 컨벤션이다.

따라서 만약 문자열 기반 모델 필드를 "nullable" 하게 만들고 싶다면 다음과 같이 하자.

```python
class Person(models.Model):
  name = models.CharField(max_length=255)  # 필수
  bio = models.TextField(max_length=500, blank=True)  # 선택 (null=True를 넣지 말자)
  birth_date = models.DateField(null=True, blank=True)  # 선택 (여기서는 null=True를 넣을 수 있다.)
```

null과 blank 옵션의 티폴트 값은 **False** 이다.

또한 특별한 케이스가 있는데, 만약 `BooleanField`에 NULL 값을 받고 싶다면, `NullBooleanField`를 대신 사용하자.
