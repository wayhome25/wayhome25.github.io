---
layout: post
title: django 06. 두번째 장고앱 15 - admin page customize
category: Django
tags: [python, 파이썬, Django, 인증]
comments: true
---
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)

> 장고의 admin 페이지를 필요에 따라 수정한다.

## admin.py 수정
- admin 페이지의 특정 model object의 필드 순서를 조정한다. - fields

```python
from django.contrib import admin
from .models import Question

# admin 수정을 위해서 admin.ModelAdmin을 상속받는 클래스를 만든다.
class QuestionAdmin(admin.ModelAdmin):
    # 표시할 필드의 순서를 조정한다.
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

<center>
 <figure>
 <img src="/assets/post-img/django/admin1.png" alt="views">
 <figcaption>model object의 필드순서 조정</figcaption>
 </figure>
 </center>


## polls/admin.py 수정 2
- 각 필드를 구분하는 대표제목을 설정한다. - fieldsets

```python
class QuestionAdmin(admin.ModelAdmin):
    # 각 필드를 구분하는 대표제목을 설정한다. (리스트 내 튜플)
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
```


## polls/admin.py 수정 3
- Question 모델과 `ForeignKey` 로 연결되어 있는 Choice 모델을 Question 모델 안에서 (Inline) 표시한다.

```python
class ChoiceInline(admin.TabularInline):
    model = Choice # 어느 모델을 가져올 것인지
    extra = 1 # 여분 작성 항목은 몇개를 기본으로 표시할 것인지


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # 해당 클래스를 인라인으로 추가한다.

admin.site.register(Question, QuestionAdmin)
```

<center>
<figure>
<img src="/assets/post-img/django/admin2.png" alt="views">
<figcaption>인라인 구현화면</figcaption>
</figure>
</center>


## polls/admin.py 수정4
- 모델의 오브젝트 표시 방법 변경 - list_display (전에는 `__str__` 항목으로 표시)

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
```

<center>
<figure>
<img src="/assets/post-img/django/admin3.png" alt="views">
<figcaption>오브젝트 표시방법 변경</figcaption>
</figure>
</center>


## 정렬, 검색 및 필터기능 추가
- 모델의 오브젝트를 정렬하는 기능을 추가 - .admin_order_field
- 모델의 오브젝트 검색 기능 추가 - search_fields, list_filter
- model.py 수정

```python
class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
```

- admin.py 수정

```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_filter = ['pub_date']
    search_fields = ['question_text']
```

<center>
 <figure>
 <img src="/assets/post-img/django/admin4.png" alt="views">
 <figcaption>정렬, 검색 및 필터기능 추가</figcaption>
 </figure>
 </center>
