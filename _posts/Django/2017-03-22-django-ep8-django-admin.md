---
layout: post
title: Django 기본 07 - admin 커스터마이징, Model Admin
category: Django
tags: [python, Django, admin]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# Django Admin
- 장고가 제공하는 기본 앱 (settings.py 내 INSTALLED_APPS 에서 확인 가능)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
]
```
- staff/superuser 계정에 한해 접근 가능 : admin에서 users 목록을 통해서 permissions 수정
- 모델 클래스만 등록하면, `조회/추가/수정/삭제 웹 인터페이스`를 admin에서 제공
- 예를 들어 맛집등록 서비스라면 관리자 맛집 등록은 어드민에서 우선 진행하고, 엔드유저를 위한 인터페이스를 우선적으로 먼저 만들 수 있다. (초기 개발시 시간 절약)

## Model 클래스 등록
- [ModelAdmin objects](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#modeladmin-objects)
- 특정 모델클래스를 admin에 등록하면, 해당 모델을 GUI 환경에서 관리 가능
- admin.py 파일 내에 원하는 모델을 import, register, unregister 진행
- admin.site.unregister 기능은 기본 유저 모델의 등록을 해제하는 등의 용도로 사용  

### Model Admin 등록법 1
- 기본 ModelAdmin으로 등록

```python
# myapp/admin.py
from django.contrib import admin
from blog.models import Post


admin.site.register(Post) # 기본 ModelAdmin으로 등록
```

### Model Admin 등록법 2
- `admin.ModelAdmin` 상속을 통해 커스터마이징이 가능하다.

```python
# myapp/admin.py
from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at' ]

admin.site.register(Post, PostAdmin)
```

### Model Admin 등록법 3
- 장식자(decorator) 형태로 등록이 가능하다. (이런 방식을 더 선호)

```python
# myapp/admin.py
from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['id', 'title']
```

<center>
 <figure>
 <img src="/assets/post-img/django/admin_option_list_link.png" alt="views">
 <figcaption>ModelAdmin 옵션 적용화면</figcaption>
 </figure>
 </center>


## ModelAdmin 옵션
-  [list_display](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display) : Admin 목록에 보여질 필드 목록
- [list_display_links](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display_links) : 목록 내에서 링크로 지정할 필드 목록 (이를 지정하지 않으면, 첫번째 필드에만 링크가 적용)
- [list_editable](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_editable) : 목록 상에서 수정할 필드 목록
- [list_per_page](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page) : 페이지 별로 보여질 최대 갯수 (디폴트 : 100)
- [list_filter](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter) : 필터 옵션을 제공할 필드 목록
- [actions](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.actions) : 목록에서 수행할 action 목록

### 옵션 적용 예시
<center>
 <figure>
 <img src="/assets/post-img/django/model_admin_option.png" alt="views">
 <figcaption></figcaption>
 </figure>
 </center>

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at' ]
    list_display_links = ['id', 'title']
    list_editable = ['author']
    list_per_page = 3
    list_filter = ['author', 'created_at']
```
---
아래 옵션은 장고 form에 대한 이해가 필요

## list_display 옵션
- 모델 인스턴스 필드명/속성명/함수명 뿐만 아니라, ModelAdmin 내 멤버 함수도 지정 가능
- 외래키를 지정한다면, 관련 object의 `__str__()` 값이 노출
- ManyToManyField 미지원

```python
# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at' ]

    def content_size(self, post):
        return mark_safe('<u>{}</u>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

```
<center>
 <figure>
 <img src="/assets/post-img/django/model_admin_option_func.png" alt="views">
 <figcaption>글자수, mark_safe 적용화면</figcaption>
 </figure>
 </center>

## Tag Escape
-  [mark_safe()](https://docs.djangoproject.com/en/1.10/ref/utils/#django.utils.safestring.mark_safe)
- Django 에서는 파이썬 코드/변수를 통해 보여지는 Html Tag 에 대해 Auto Escape 를 수행
- a/img/script 태그 등으로 인한 허용치않은 코드 실행 방지
- 특징 문자열에 한해, 이를 해제하기 위해 autoescape off template tag를 적용하거나, 문자열에 [format_html()](https://docs.djangoproject.com/en/1.10/ref/utils/#django.utils.html.format_html), [format_html_join()](https://docs.djangoproject.com/en/1.10/ref/utils/#django.utils.html.format_html_join), [mark_safe()](https://docs.djangoproject.com/en/1.10/ref/utils/#django.utils.safestring.mark_safe) 적용

## Admin actions
- [Admin actions](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/actions/)
- 대개 선택된 Model Instance 들에 대해 Bulk Update 용도 구현

### 모델에 status 컬럼 추가 후 migration

```python
# myapp/models.py
class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

```

```shell
# migration 진행
$ python3 manage.py makemigrations myapp
$ python3 manage.py migrate
```

### admin.py에 admin actions 추가
- ModelAdmin 클래스내 멤버함수로 action 함수를 구현
- 멤버함수.short_description 을 통해, action 설명 추가
- ModelAdmin actions 내에 등록

```python
# myapp/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at' ]
    actions = ['make_published', 'make_draft']

    # 글자수 컬럼 추가
    def content_size(self, post):
        return mark_safe('<u>{}</u>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    # admin action 추가
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #queryset.update
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count)) #django message framework 활용
    make_published.short_description = '지정 포스팅을 Published 상태로 변경'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') #queryset.update
        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count)) #django message framework 활용
    make_draft.short_description = '지정 포스팅을 draft 상태로 변경'
```

<center>
 <figure>
 <img src="/assets/post-img/django/admin_model_option_actions.png" alt="views">
 <figcaption>admin actions 적용화면</figcaption>
 </figure>
 </center>
