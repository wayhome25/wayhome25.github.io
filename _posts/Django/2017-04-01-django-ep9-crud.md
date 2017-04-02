---
layout: post
title: Django 기본 08 - 모델 queryset을 통한 CRUD, django-debug-toolbar, requirements.txt
category: Django
tags: [python, Django, admin]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# Model Manager
- 데이터베이스 질의 인터페이스를 제공
- 디폴트 Manager로서 `모델클래스.objects` 가 제공된다.

```shell
# 장고 shell 실행1 - 필요한 모듈을 자동으로 import 하고 jupyter notebook 실행
$ python3 manage.py shell_plus --notebook

# 장고 shell 실행1 - 필요한 모듈을 자동으로 import 하고 shell_plus 실행
$ python3 manage.py shell_plus

# Post 모델의 기본 모델 메니저
$ Post.objects
<django.db.models.manager.Manager at 0x107466f28>
```
- [Model Manager](https://docs.djangoproject.com/en/1.10/topics/db/managers/)를 통해 해당 모델 클래스의 DB 데이터를 추가, 조회, 수정, 삭제 (CRUD)가 가능하다.

```shell
ModelCls.objects.all() # 특정 모델의 전체 데이터 조회 ModelCls.objects.all().order_by('-id')[:10] # 특정 모델의 최근 10개 데이터 조회 ModelCls.objects.create(title="New Title") # 특정 모델의 새 Row 저장
```


## QuerySet
- SQL을 생성해주는 인터페이스
- queryset을 통하여 별도로 SQL을 작성할 필요 없이 DB로 부터 데이터를 가져오고 추가, 수정, 삭제가 가능하다.
- Model Manager를 통해 해당 Model에 대한 QuerySet을 획득한다.
  - Post.objects.all() : "SELECT * FROM post..." 와 같은 SQL문 생성
  - Post.objects.create() : "INSERT INTO post VALUES(...)" 와 같은 SQL문 생성
- `Chaining`을 지원한다.
- connection 모듈을 통해 queryset으로 만들어진 실제 sql문을 shell에서 확인할 수 있다.

```shell
from django.db import connection

ModelCls.objects.all().order_by('-id')[:10]
connection.queries[-1]
# {'sql': 'SELECT "blog_post"."id", "blog_post"."status", "blog_post"."author", "blog_post"."title", "blog_post"."content", "blog_post"."tags", "blog_post"."lnglat", "blog_post"."created_at", "blog_post"."updated_at" FROM "blog_post" ORDER BY "blog_post"."id" DESC LIMIT 10', 'time': '0.000'}
```
---
# DB 데이터 조회 (Retrieve)

## AND 조건 (filter)
- chaining, Lazy

```python
# chaining을 통해 조건1~3 이 적용된 queryset을 마지막에 리턴
queryset = 모델클래스명.objects.all()
queryset = queryset.filter(조건필드1=조건값1, 조건필드2=조건값2)
queryset = queryset.filter(조건필드3=조건값3)


for model_instance in queryset:
    print(model_instance) # 화면에 출력할 때 DB에 쿼리 (lazy)
```
- i = ignore_case (대소문자 구별 X) []

```python
# 필터링 (qs1 = qs2)
qs1 = Post.objects.filter(title__icontains='1', title__endswith='3') # i = ignore_case (대소문자 구별 X)
qs2 = Post.objects.filter(title__icontains='1').filter(title__endswith='3') # 체이닝
```

## 제외조건 (exclude)

```python
# 제목에 '테스트'를 포함한 record를 제외한 전체
Post.objects.all().exclude(title__icontains='test')

# 제목에 1을 포함하지만 3으로 끝나지 않는 record
Post.objects.filter(title__icontains='1').exclude(title__endswith='3')
```

## OR 조건 (filter)
- [Complex lookups with Q objects](https://docs.djangoproject.com/en/1.10/topics/db/queries/#complex-lookups-with-q-objects) : or 조건을 사용하기 위해서는 Q 객체 import가 필요하다.

```python
from django.db.models import Q

모델클래스명.objects.all().filter(Q(조건필드1=조건값1) | Q(조건필드2=조건값2)) # or 조건
모델클래스명.objects.all().filter(Q(조건필드1=조건값1) & Q(조건필드2=조건값2)) # and 조건
```

## filter을 활용한 간단 검색 구현
- 포스팅 1000개 한꺼번에 만들기

```python
import random
for i in range(1000):
    status = random.choice(['d', 'p', 'w'])
    Post.objects.create(author="몽키", title="제목 #{}".format(i), content="테스트 내용 #{}".format(i), status=status)

# 모델 클래스의 오브젝트 갯수확인
Post.objects.all().count()
```

- filter를 통한 검색 구현  

```python
# myapp/views.py
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
})

# blog/templates/blog/post_list.html

<form action="" method="get">
<input type="text" name="q" /> <input type="submit" value="검색" />
</form>
```

## 특정필드 기준 정렬조건 (Meta.ordering)
- queryset의 기본 정렬은 모델 클래스 내부의 [Meta.ordering](https://docs.djangoproject.com/en/1.10/ref/models/options/#ordering) 설정을 따른다.

```python
# myapp/models.py
#
class Post(models.Model):
  ....
  class Meta:
    ordering = ['-id'] # id 필드 기준 내림차순 정렬, 미지정시 임의 정렬
```

- 모델 Meta.ordering 을 무시하고 직접 정렬조건 지정도 가능하다.

```python
queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청
queryset = queryset.order_by('-field1') # 지정 필드 내림차순 요청
queryset = queryset.order_by('field2', 'field3') # 1차기준, 2차기준
```

## 범위 조건 (슬라이싱)

```python
queryset = queryset[:10] # 현재 queryset에서 처음10개만 가져오는 조건을 추가한 queryset
queryset = queryset[10:20] # 현재 queryset에서 처음10번째부터 20번째까지를 가져오는 조건을 추가한 queryset

# 리스트 슬라이싱과 거의 유사하나, 역순 슬라이싱은 지원하지 않음
queryset = queryset[-10:] # AssertionError 예외 발생

# 이때는 먼저 특정 필드 기준으로 내림차순 정렬을 먼저 수행한 뒤, 슬라이싱
queryset = queryset.order_by('-id')[:10]
```

## 지정 조건 (get, first, last)
- 지정 조건으로 DB로부터 데이터 Fetch

### queryset.get
- 해당 조건에 해당되는 데이터가 1개임을 기대
  - 0개 : 모델클래스명.DoesNotExist 예외 발생
  - 1개 : 정상처리
  - 2개 : 모델클래스명.MultipleObjectsReturned 예외 발생

```python
# 지정 조건의 데이터 Row를 순회
for model_instance in queryset:
    print(model_instance)

# 특정 조건의 데이터 Row 1개 Fetch (1개!! 2개이상말고 1개!! 0개말고 1개!!) model_instance = queryset.get(id=1)
model_instance = queryset.get(title='my title')
```

### queryset.first(), queryset.last()
- 지정 조건 내에서 첫번째/마지막 데이터 Row를 Fetch
- 지정 조건에 맞는 데이터 Row가 없더라도, DoesNotExist 예외가 발 생하지 않고, None을 반환

```python
model_instance = queryset.first() # model instance 또는 None
model_instance = queryset.last() # model instance 또는 None
```

# DB 데이터 추가 (Create)
- 추가시에 필수필드 (필드 정의 시에, blank=True, null=True 혹은 디폴트값이 지정되지 않은 필드) 를 모두 지정해야한다. IntegrityError 발생
- shell에서 `모델명??` 을 통해서 해당 모델의 상세 필드옵션을 확인할 수 있다.

```shell
In [2]: Post??
Init signature: Post(*args, **kwargs)
Source:
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='제목')
    origin = models.CharField(max_length=200,  blank=True, null=True, verbose_name='원본 URL')
    video_url = models.CharField(max_length=100, blank=True, null=True, verbose_name='YouTube 링크')
    video_key = models.CharField(max_length=12, null=True, blank=True)
    video_time = models.IntegerField(null=True, blank=True)
    video_url2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='YouTube 링크2')
    video_key2 = models.CharField(max_length=12, null=True, blank=True)
    video_time2 = models.IntegerField(null=True, blank=True)
    text = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
```

## 방법1. 각 Model Instance 의 save 함수를 통해 저장

```python
model_instance = Post(author=User.objects.all()[0], title='title', text='content')
model_instance.save()

```

## 방법2. 각 Model Manager의 create 함수를 통해 저장

```python
new_post = Post.objects.create(author=User.objects.get(id=1), title='title', text='content')
```

- .save(), .create() 실행시 DB에 INSERT SQL이 전달된다.

---
# DB 데이터 수정 (Update)

## 방법1. 각 Model Instance 속성을 변경하고, save 함수를 통해 저장
- 각 Model인스턴스 별로 SQL 수행
- 다수 Row에 대해서 수행 시 성능저하

```python
post_instance = Post.objects.get(id=66)
post_instance.title = 'edit title' # title 수정
post_instance.save()

queryset = Post.objects.all()
for post in queryset:
    post.tags = 'Python, Django'
    post.save() # 각 Model Instance 별로 DB에 update 요청 - 성능저하
```

## 방법2. QuerySet의 update 함수에 업데이트할 속성값을 지정하여 일괄 수정
- 하나의 SQL 로서 동작하므로, 동작이 빠르다.

```python
queryset = Post.objects.all()
queryset.update(title='test title') # 일괄 update 요청
```
---
# DB 데이터 삭제 (Delete)

## 방법1. 각 Model Instance의 delete 함수를 호출하여 삭제
- 각 Model인스턴스 별로 SQL 수행
- 다수 Row에 대해서 수행 시 성능저하

```python
post_instance = Post.objects.get(id=66)
post_instance.delete()

queryset = Post.objects.all()
    for post in queryset:
    post.delete() # 각 Model Instance 별로 DB에 delete 요청 - 성능저하
```

## 방법2.  QuerySet의 delete 함수를 호출하여, 관련 데이터를 삭제
- 하나의 SQL로 동작하므로 동작이 빠르다.

```python
queryset = Post.objects.all()
queryset.delete() # 일괄 delete 요청
```
---
# 웹소비스 반응속도에 미치는 DB의 영향
- DB : 아주 중요
  - DB로 전달/실행되는 SQL 갯수 줄이기 (그래서 일괄 처리가 성능이 좋음)
  - 각 SQL의 성능/처리속도 최적화 필요
- 로직의 복잡도 : 중요
- 프로그래밍 언어의 종류 : 대개는 미미

---

# django-debug-toolbar
- [사이트](http://django-debug-toolbar.readthedocs.io/en/stable/)
- 현재 request/response 에 대한 다양한 디버깅 정보를 보여준다.
- SQLPanel을 통해 각 요청 처리시에 발생한 SQL 내역 확인 가능 (from django.db import connection 모듈 사용보다 간편)
- 웹서비스 성능과 직결 = 응답속도

## 설치

```shell
pip3 install django-debug-toolbar
```

```python
# mysite/settings.py

INSTALLED_APPS = [..., "debug_toolbar"]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware", ...]
INTERNAL_IPS = ["127.0.0.1"]

# mysite/urls.py
from django.conf import settings
from django.conf.urls import include, url
  # 중략 ...

if settings.DEBUG: # setting.py의 DEBUG = True인 경우
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

```

- 주의 : 해당 페이지의 템플릿에 <body> 태그가 있어야 함

---
# 코드를 통한 SQL 내역 확인
- settings.DEBUG=True 시에만 쿼리 실행내역을 메모리에 누적

```python
from django.db import connection
from blog.models import Post

print(Post.objects.all())

for query in connection.queries:
    print(query)
```
---
# requirements.txt 작성
- 지금까지 사용한 라이브러리 목록 정리

```shell
# vim requirements.txt
On branch master
Changes not staged for commit:
  1 django==1.10.5
  2 django-debug-toolbar
  3 django-extensions
  4 ipython[notebook]
```

- 나중에 필요할 때 requirements.txt를 사용하여 필요한 라이브러리를 한번에 설치할 수 있다.
- 개발환경 셋업에 아주 유용함

```shell
$ pip3 install -r requirements.txt
```
