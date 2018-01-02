---
layout: post
title: update_fields - 어떤 필드를 저장할지 지정하기
category: Django
tags: [django, model, update_fields]
comments: true
---

만약 save() 메소드 호출시에 update_fields 라는 키워드 인자로 필드 이름 리스트가 함께 전달 된다면, 해당 필드 목록만 업데이트 될 것이다. 당신이 하나의 필드 혹은 몇개의 필드만 업데이트 하려고 할 때 유용하게 사용될 수 있다. 그리고 DB의 모든 모델 필드가 업데이트 되는걸 막음으로써 약간의 성능적인 이점도 있다.

```python
product.name = 'Name changed again'
product.save(update_fields=['name'])
```

update_fields 전달인자는 모든 반복가능한 문자열을 포함할 수 있다. update_fields=[]와 같이 빈 update_fields를 포함하면 save 메소드는 아무것도 수행하지 않고 생략된다. update_fields=None 의 경우에는 모든 필드에 대해서 업데이트를 수행한다.

update_fields를 지정함으로써 업데이트를 강제할 수 있다.

지연 모델 로딩([only()](https://docs.djangoproject.com/ko/2.0/ref/models/querysets/#django.db.models.query.QuerySet.only) 혹은 [defer()](https://docs.djangoproject.com/ko/2.0/ref/models/querysets/#defer))을 통해서 가져온 모델을 저장할때, DB로부터 로딩된 필드만 업데이트 된다. 사실상 이 경우 자동 update_fields 가 지정된다. 만약 당신이 지연된 필드에 새로운 값을 지정하거나 수정을 한다면, 해당 필드는 updated fields에 자동으로 지정될 것이다.


- 참고
  - [Specifying which fields to save](https://docs.djangoproject.com/ko/2.0/ref/models/instances/#specifying-which-fields-to-save)
  - [facebook Django 그룹](https://www.facebook.com/groups/django/permalink/629063510463485)
