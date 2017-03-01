---
layout: post
title: django 04. 장고 개인 프로젝트 (메모 앱) - 개발과정 기록   
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 04. 장고 개인 프로젝트 (메모 앱)
> 첫 장고 개인 프로젝트 진행 중 새롭게 배운 부분을 정리하였습니다.

## Model 클래스 작성
> DB 연동을 위한 model class를 작성한다.

- 장고 가이드 문서 [Model field reference](https://docs.djangoproject.com/en/1.10/ref/models/fields/#model-field-types) 를 통해 model field의  data type, optiond 을 참고할 수 있다.

- models.py 에 모델 클래스 작성 후, 장고에게 모델을 만들었다는 걸 알려줘야 한다.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

- 클래스 대표 값은 `__str__` 메소드를 통해서 정의한다.

```python
def __str__(self):
      return '%s by %s' % (self.title, self.name)
```
