---
layout: post
title: 장고 쿼리셋 합치기
category: Django
tags: [django, queryset]
comments: true
---

> 앞으로 가벼운 마음으로 블로그를 하기로 결심했으니 기념으로 짧은 글을 올려보자

쿼리셋 2개를 합치고 싶을때는 간단하게 `|`를 사용하면 된다. 대신 같은 모델에서 나온 쿼리셋만 합칠 수 있다.

```python
q3 = q1 | q2
```

- Django 1.11부터는 [qs.union()](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#union)메소드를 이용할 수 있다. 그 밖에도 쿼리셋간의 합집합, 교집합, 차집합을 만들 수 있는 메소드가 추가되었다. (intersection(), difference())
- [itertools.chain](https://docs.python.org/3/library/itertools.html#itertools.chain)을 사용하는 방법도 있다.
