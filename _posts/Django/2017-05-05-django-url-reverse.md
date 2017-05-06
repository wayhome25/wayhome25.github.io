---
layout: post
title: URL Reverse, 아는 사람은 꼭 쓴다는 get_absolute_url()
category: Django
tags: [python, Django, url]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.


- 장고는 urls.py 변경을 통해 '각 뷰에 대한' url이 변경되는 유연한 시스템을 갖고 있다.
- url이 변경 되더라도 url reverse가 변경된 url을 추적한다. (누락의 위험이 적다)

# URL Reverse를 수행하는 4가지 함수

## reverse()
- 리턴형식 : string

```python
from django.core.urlresolvers import reverse

reverse('blog:post_list') # '/blog/'
reverse('blog:post_detail', args=[10]) # '/blog/10/' args 인자로 리스트 지정 필요
reverse('blog:post_detail', kwargs={'id':10}) # '/blog/10/'
reverse('/hello/') # NoReverseMatch 오류 발생
```

## resolve_url()
- 리턴형식 : string
- 내부적으로 reverse() 사용
- reverse() 보다 사용이 간단하다.

```python
from django.shortcuts import resolve_url

resolve_url('blog:post_list') # '/blog/'
resolve_url('blog:post_detail', 10) # '/blog/10/'
resolve_url('blog:post_detail', id=10) # '/blog/10/'
resolve_url('/hello/') # '/hello/' 문자열 그대로 리턴
```


## redirect()
- 리턴형식 : HttpResponseRedirect
- 내부적으로 resolve_url() 사용
- view 함수 내에서 특정 url로 이동 하고자 할 때 사용 (Http Response)

```python
from django.shortcuts import redirect

redirect('blog:post_detail', 10)
# <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/blog/10/">
```

## url template tag
- 내부적으로 reverse() 사용

```html
{% raw %}
<li><a href="{% url 'blog:post_detail' post.id %}">{{ post.title }}</a> </li>
{% endraw %}
```

---


# 모델 클래스 내 get_absolute_url 멤버함수
`사용 강추!`

> 특정 모델에 대한 Detail뷰를 작성할 경우, Detail뷰에 대한 URLConf설정을 하자마자,    
  필히 get_absolute_url설정을 해주세요. 코드가 보다 간결해집니다

- 어떠한 모델에 대해서 detail 뷰를 만들게 되면 get_absolute_url() 멤버 함수를 무조건 선언
- resolve_url(모델 인스턴스), redirect(모델 인스턴스) 를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출
- resolve_url() 함수는 가장 먼저 get_absolute_url 함수의 존재 여부를 체크하고, 존재하면 호출하며 그 리턴값으로 URL을 사용

## get_absolute_url 작성

```python
class Post(models.Model):
    # ... (중략)
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
```

##  get absolute url 활용
- 2, 3, 1 의 순서대로 많이 사용
- 처음부터 get_absolute_url 을 적극적으로 사용하는 연습을 하는 것이 좋음

### 1. url template tag로 활용

```html
{% raw %}
<li><a href="{{ post.get_absolute_url }}">{{ post.title }}</a> </li>
{% endraw %}
```

### 2. resolve_url, redirect를 통한 활용

```python
from django.shortcuts import resolve_url
from django.shortcuts import redirect

resolve_url('blog:post_detail', post.id) # '/blog/105/'
resolve_url(post) # '/blog/105/' 인자의 인스턴스 메소드로 get_absolute_url 있는지 체크해서 리턴

print(redirect('blog:post_detail', post.id))
print(redirect(post))
# <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/blog/105/">
```

### 3. CBV 에서의 활용
- CreateView, UpdateView에 success_url을 제공하지 않는 경우, 해당 model instance의 get_absolute_url 주소로 이동이 가능한지 체크
- 생성, 수정 뒤에 Detail 화면으로 가는 것은 일반적
