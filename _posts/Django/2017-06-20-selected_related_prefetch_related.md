---
layout: post
title: django 쿼리셋 수정을 통한 웹서비스 성능 개선 - select_related, prefetch_related  
category: Django
tags: [python, Django, queryset]
comments: true
---
> 개인적인 연습 내용을 정리한 글입니다.      
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

# 쿼리셋 수정을 통한 웹서비스 성능 개선

## 들어가기
웹서비스에 있어서 데이터페이스는 성능에 많은 영향을 미친다.       
절대적으로 SQL 갯수를 줄이고, 각 SQL의 성능 및 처리속도 최적화가 필요하다.       

리스트 조회 페이지를 만들때 `Post.objects.all()` 과 같은 queryset을 자주 활용했었다.
이번에 [인스타그램st 프로젝트](https://github.com/wayhome25/Instagram)를 진행하며 데이터 조회시 몇개의 SQL 쿼리가 발생할까? 중복은 없을까? 궁금해졌다.       
[**django-debug-toolbar**](http://django-debug-toolbar.readthedocs.io/en/stable/) 를 활용해서 페이지 로딩시 발생하는 쿼리를 확인해보았는데, 결과가 충격적이었다.       
**고작 글 9개를 조회하고 화면에 출력하는데, `28개의 쿼리문이 발생하고 그 중에 26개는 중복이었다.`** (부들부들..)       

이를 해결하기 위해서 다음과 같은 메소드를 활용하였다.
- [select_related()](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#select-related)
  - ForeignKey, OneToOneField 관계에서 활용
  - ForeignKey/OneToOneField 관계에서 Lazy하게 쿼리하지 않고, DB단에서 INNER JOIN 으로 쿼리할 수 있다.
- [prefetch_related()](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#prefetch-related)
  - ManyToManyField, ForeignKey의 reverse relation 에서 활용
  - 각 관계 별로 DB 쿼리를 수행하고, 파이썬 단에서 조인을 수행한다.

**수정 결과는 대만족! `28개의 쿼리문이 5개로 줄어들고 중복은 모두 삭제되었다.`**      
아래는 내가 겪었던 문제와, 이를 해결하는 과정을 정리한 내용이다.

---

## models
- 각 모델은 다양한 필드 (1:N 관계, 1:1 관계, M:N 관계) 갖고 있다.

```python
# models.py
class Post(models.Model):
    #...생략...
    author = models.ForeignKey(settings.AUTH_USER_MODEL) # auth.User
    tag_set = models.ManyToManyField('Tag', blank=True)


class Tag(models.Model):
    # Tag:Post = M:N
    name = models.CharField(max_length=140, unique=True)


class User(AbstractUser):
    #...생략...
    # User:Post = 1:N
    # User:Profile = 1:1


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, unique=True)
```

## views

### 수정 전
- 평소처럼 Post.objects.all() 를 활용하여 post_list 를 가져오고 이를 contenxt 객체로 template에 전달했다.

```python
# views.py

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })
```


## template
- 전달한 post_list는 다음과 같이 템플릿에서 활용하였다.
- [**django-debug-toolbar**](http://django-debug-toolbar.readthedocs.io/en/stable/) 를 활용해서 페이지 로딩시 발생하는 쿼리를 확인하니, Post 모델에서 User 모델/Tag 모델로 접근하면서 중복되는 DB 작업이 발생하는 것을 확인할 수 있었다.

```html
{% raw %}
{% for post in post_list %}
<!-- post_list가 10개라고 가정하면 -->
<ul>
  <li>{{ post.author.profile.nickname }}</li>
  <!-- 1. post 인스턴스별로 post와 N:1 관계인 author 모델에 접근 -->
  <!-- 2. author 모델과 1:1 관계인 profile 모델에 접근하여 중복 작업이 발생한다 -->
  <!-- 총 20번의 중복 발생 -->
  <li>{{ post.content }}</li>
  <li>{% for tag in post.tag_set.all %} {{ tag.name }} {% endfor %}</li>
  <!-- 3. post 인스턴스별로 post와 N:M 관계인 tag 모델에 접근 -->
  <!-- 추가적으로 10번의 중복 발생 -->
</ul>
{% endfor %}
{% endraw %}
```

### 문제상황

![1](http://i.imgur.com/SOXAHCo.png)
<center><figcaption>post 갯수가 늘어날수록 중복도 어마어마하게 늘어난다</figcaption></center>


---

# 쿼리셋 수정 및 성능 개선과정

- 위와 같은 중복 DB 접근 문제를 해결하기 위해서 [select_related](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#select-related), [prefetch_related](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#prefetch-related) 를 활용하였다.


## 수정 1
- Post.objects.select_related('author').all() 사용
- 28개-> 20개로 쿼리문으로 줄어들었다 (17개 중복)
- (참고) post 인스턴스 갯수 : 9개


```python
# views.py

def post_list(request):
    post_list = Post.objects.select_related('author').all()
    # 첫 DB 쿼리시 author record까지 로딩

    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })
```

```html
{% raw %}
{% for post in post_list %}
<!-- post_list가 10개라고 가정하면 -->
<ul>
  <li>{{ post.author.profile.nickname }}</li>
  <!-- 1. (개선 전) post 인스턴스별로 post와 N:1 관계인 author 모델에 접근 -->
  <!-- 1. (개선 후) 첫 DB 쿼리시에 author record까지 로딩했기 때문에 추가 DB 없음 -->
  <!-- 2. author 모델과 1:1 관계인 profile 모델에 접근하여 중복 작업이 발생한다 -->
  <!-- 총 10번의 중복 발생 -->
  <li>{{ post.content }}</li>
  <li>{% for tag in post.tag_set.all %} {{ tag.name }} {% endfor %}</li>
  <!-- 3. post 인스턴스별로 post와 N:M 관계인 tag 모델에 접근 -->
  <!-- 추가적으로 10번의 중복 발생 -->
</ul>
{% endfor %}
{% endraw %}
```

![2](http://i.imgur.com/oZ9JY8l.png)
<center><figcaption>첫 DB 쿼리시 .select_related('author')를 통해 author record를 함께 로딩한다.</figcaption></center>

## 수정 2
- Post.objects.prefetch_related('tag_set').select_related('author').all()사용
- 28->20->13개로 쿼리문으로 줄어들었다 (9개 중복)
- (참고) post 인스턴스 갯수 : 9개


```python
# views.py

def post_list(request):
    post_list = Post.objects.prefetch_related('tag_set').select_related('author').all()
    # 첫 DB 쿼리시 tag_set, author record 까지 로딩

    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })
```

```html
{% raw %}
{% for post in post_list %}
<!-- post_list가 10개라고 가정하면 -->
<ul>
  <li>{{ post.author.profile.nickname }}</li>
  <!-- 1. (개선 전) post 인스턴스별로 post와 N:1 관계인 author 모델에 접근 -->
  <!-- 1. (개선 후) 첫 DB 쿼리시에 author record까지 로딩했기 때문에 추가 DB 없음 -->
  <!-- 2. author 모델과 1:1 관계인 profile 모델에 접근하여 중복 작업이 발생한다 -->
  <!-- 총 10번의 중복 발생 -->
  <li>{{ post.content }}</li>
  <li>{% for tag in post.tag_set.all %} {{ tag.name }} {% endfor %}</li>
  <!-- 3. (개선 전) post 인스턴스별로 post와 N:M 관계인 tag 모델에 접근 -->
  <!-- 3. (개선 후) 첫 DB 쿼리시에 tag_set record까지 로딩했기 때문에 추가 DB 없음 -->
</ul>
{% endfor %}
{% endraw %}
```

![3](http://i.imgur.com/kbBe14B.png)
<center><figcaption>초기 DB 쿼리시 tag_set, author record를 함께 로딩한다.</figcaption></center>


## 수정 3
- Post.objects.prefetch_related('tag_set').select_related('author__profile').all() 사용
- `28->20->13->5개로 쿼리문으로 줄어들었다 (중복없음)`
- (참고) post 인스턴스 갯수 : 9개

![4](http://i.imgur.com/Col4HTd.png)
<center><figcaption>초기 DB 쿼리시 tag_set, author, author과 1:1 관계인 profile record를 함께 로딩한다.</figcaption></center>

```python
def post_list(request):
    post_list = Post.objects.prefetch_related('tag_set').select_related('author__profile').all()
    # 첫 DB 쿼리시 tag_set, author, author과 1:1 관계인 profile record까지 로딩

    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })
```


```html
{% raw %}
{% for post in post_list %}
<!-- post_list가 10개라고 가정하면 -->
<ul>
  <li>{{ post.author.profile.nickname }}</li>
  <!-- 1. (개선 전) post 인스턴스별로 post와 N:1 관계인 author 모델에 접근 -->
  <!-- 1. (개선 후) 첫 DB 쿼리시에 author record까지 로딩했기 때문에 추가 DB 없음 -->
  <!-- 2. (개선 전) author 모델과 1:1 관계인 profile 모델에 접근하여 중복 작업이 발생한다 -->
  <!-- 2. (개선 후) 첫 DB 쿼리시에 author 과 1:1 관계인 profile record 로딩했기 때문에 추가 DB 없음-->
  <li>{{ post.content }}</li>
  <li>{% for tag in post.tag_set.all %} {{ tag.name }} {% endfor %}</li>
  <!-- 3. (개선 전) post 인스턴스별로 post와 N:M 관계인 tag 모델에 접근 -->
  <!-- 3. (개선 후)  첫 DB 쿼리시에 tag_set record까지 로딩했기 때문에 추가 DB 없음 -->
</ul>
{% endfor %}
{% endraw %}
```

## 결론
그동안 너무 당연하게 모델.objects.all()를 사용하여 전체 DB를 조회하고 활용했었다.     
이번 기회를 통해서 상황에 맞는 queryset을 사용하지 않으면 **엄청난 중복이 발생하고, 이는 속도저하로 연결된다는 것을 알게되었다.**         
사실 [AskDjango](https://nomade.kr/vod/django/39/)에서 관련된 강의를 들었을 때는 '아 이런게 있구나' 하고 넘어갔던 내용이다.
역시 필요성이 생기니 정보에 대해 접근하는 태도가 달라지는 것 같다.     
그리고 덤으로 [django-debug-toolbar](http://django-debug-toolbar.readthedocs.io/en/stable/) 활용 방법을 찾은 것 같다. 이렇게 유용할 줄이야!

## reference
- [(AskDjango 강의) Relation QuerySet 성능 높이기 - selected_related, prefetch_related](https://nomade.kr/vod/django/39/)
- [(raccoony님의 블로그) Django에서 쿼리셋 효과적으로 사용하기](http://raccoonyy.github.io/using-django-querysets-effectively-translate/index.html)
