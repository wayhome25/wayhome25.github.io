---
layout: post
title: Django 사용자 정의 필터 (Custom Template Filter)를 활용하여 인스타그램 해시태그 링크 구현하기  
category: Django
tags: [python, Django, 사용자정의필터]
comments: true
---
> 개인적인 연습 내용을 정리한 글입니다.      
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

# 장고 Custom Template Filter 활용하기

## 목차
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [장고 Custom Template Filter 활용하기](#장고-custom-template-filter-활용하기)
  * [들어가기](#들어가기)
  * [Model](#model)
  * [view](#view)
  * [template](#template)
* [custom template filter 적용하기](#custom-template-filter-적용하기)
  * [1. 장고 프로젝트 app 내에 templatetags 폴더 (패키지) 만들기](#1-장고-프로젝트-app-내에-templatetags-폴더-패키지-만들기)
  * [2. 사용자 정의 템플릿 필터 (모듈) 작성하기](#2-사용자-정의-템플릿-필터-모듈-작성하기)
  * [3. template 내에 해당 모듈을 load 하고, 원하는 field에 필터 적용하기](#3-template-내에-해당-모듈을-load-하고-원하는-field에-필터-적용하기)
  * [결과물](#결과물)
  * [결론, 느낀점](#결론-느낀점)

<!-- tocstop -->

## 들어가기
요즘 연습중인 [인스타그램st 프로젝트](https://github.com/wayhome25/Instagram) 를 진행하며     
실제 인스타그램 처럼 본문의 해시태그 문자열을 링크 처리하고,       
해당 링크를 클릭하면 태그 내용이 포함된 모든 post list를 검색 결과로 보여주는 기능을 구현하고 싶었다.      

![스크린샷 2017-06-22 오후 10.38.36](http://i.imgur.com/qR2o9ut.jpg)
<center><figcaption>내가 원하는 것</figcaption></center>
<br>



여러가지 방법을 고민하고 시도해보았는데, 생각도 못했던 오류들이 다양하게 발생했다.     
(편집 화면에서 html tag가 그대로 노출되는 등)    
그냥 다른 기능구현으로 넘어갈까 싶었지만 꼭 필요한 기능이라고 생각해서 열심히 찾아보았다.        
결과적으로 **[custom template filter](https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/)를 활용하여 DB 내용에 직접적인 영향을 미치지 않고**, 깔끔하게 해결할 수 있었다!

## Model
- Post와 Tag 모델은 ManyToMany 관계를 갖고 있다.
- content에 입력된 문자열 중에서 해시태그 형태 (#태그명)를 가진 문자열을 따로 추출하여 Tag 모델에 저장하도록 구현하였다.
- 자세한 코드는 [github](https://github.com/wayhome25/Instagram/blob/master/project/post/models.py) 에서 확인 가능하다.

```python
class Post(models.Model):
  #...생략...
  content = models.CharField(max_length=140, help_text="최대 140자 입력 가능")
  tag_set = models.ManyToManyField('Tag', blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)
```

## view
- queryset을 활용하여 Post 모델의 모든 인스턴스를 가져온다. (post_list)
- 이를 contenxt 객체로 템플릿에 넘겨준다.

```python
def post_list(request):
    post_list = Post.objects.prefetch_related('tag_set').select_related('author__profile').all()

    #...생략...

    return render(request, 'post/post_list.html', {
        'post_list': post_list,
    })
```

## template
- 현재는 post.content의 문자열이 그대로 출력되고 있는 상태
- post.content 내부의 문자열에서 특정 문자열을 추출하여 원하는대로 수정하려면 'custom filter'가 필요하다.

```html
{% raw %}
<!-- ...생략... -->
{% for post in post_list %}
<ul>
  <li>{{ post.author.profile.nickname }}</li>
  <li><img src="{{ post.photo.url }}" alt="{{ post.author }}'s photo"></li>
  <li>{{ post.content }}</li>
  <!-- post.content 내부의 문자열에서 특정 문자열을 추출하여 원하는대로 수정하려면 'custom filter'가 필요하다-->
</ul>
{% endfor %}
{% endraw %}
```
<br>

---
# custom template filter 적용하기

[Django 공식문서](https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/) 를 찾아보면, 사용자 정의 템플릿 필터를 만드는 과정은 크게 3가지로 나뉜다.

1. 장고 프로젝트 app 내에 templatetags 폴더 (패키지) 만들기
2. 사용자 정의 템플릿 필터 (모듈) 작성하기
3. template 내에 해당 모듈을 load 하고, 원하는 field에 필터 적용하기


## 1. 장고 프로젝트 app 내에 templatetags 폴더 (패키지) 만들기
- 일반적으로 custom template tags, filters 를 정의하는 곳이 Django app 디렉토리 안이다.
- 작성하려는 사용자 정의 필터가 진행중인 프로젝트 앱과 연관성이 있다면, 해당 앱 디렉토리 하단에 `templatetags` 폴더를 추가한다.     
  (modles.py, views.py 와 동일한 level에 추가한다.)
- 폴더 작성 후 해당 폴더 내에 `__init__.py` 라는 이름의 빈 파일을 추가한다. (내용은 없어도 괜찮다.)
- 이 파일의 역할은 해당 폴더가 파이썬 패키지 라는 것을 명시하는 것이다.
- templatetags 폴더(패키지)을 추가하고 나서는 터미널로 돌아가 서버를 재시작 해야 정상적으로 적용된다.

```python
# 폴더구조 예시
post/
    __init__.py
    models.py
    templatetags/
        __init__.py
        post_extras.py # 앞으로 작성할 사용자 정의 템플릿 필터 파일예시
    views.py
```

## 2. 사용자 정의 템플릿 필터 (모듈) 작성하기
- templatetags 폴더 아래에 원하는 이름으로 .py 파일을 추가한다.
- 여기서는 post_extras.py 라는 이름을 사용하였다. 해당 파일에는 사용자 정의 필터 함수를 작성할 것이다.
- 우선은 상단에 아래와 같은 코드를 추가한다. register는 유효한 tag library를 만들기 위한 모듈 레벨의 인스턴스 객체이다.

```python
# post_extras.py
from django import template

register = template.Library()
```

- 그리고 `add_link` 라는 이름의 함수를 정의한다. (이것이 바로 template에서 사용할 사용자 정의 필터의 이름이다.)
- 해당 필터 함수는 `post|add_link` 와 같이 활용될 수 있다. 이때 post 객체는 add_link 함수의 파라미터로 전달된다.

```python
# post_extras.py
@register.filter
def add_link(value):
    content = value.content # 전달된 value 객체의 content 멤버변수를 가져온다.
    tags = value.tag_set.all() # 전달된 value 객체의 tag_set 전체를 가져오는 queryset을 리턴한다.

    # tags의 각각의 인스턴를(tag)를 순회하며, content 내에서 해당 문자열을 => 링크를 포함한 문자열로 replace 한다.
    for tag in tags:
        content = re.sub(r'\#'+tag.name+r'\b', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content)
    return content # 원하는 문자열로 치환이 완료된 content를 리턴한다.
```

## 3. template 내에 해당 모듈을 load 하고, 원하는 field에 필터 적용하기
- 우선 템플릿 상단에 사용할 모듈을 load한다.
- 여기서는 사용자 정의 필터가 포함된 모듈인 post_extras.py 를 load 한다.

```html
{% raw %}
<!-- post_list.html -->
{% load post_extras %}  <!-- custom filter 추가 -->
{% endraw %}
```

- `post|add_link` 와 같이, 원하는 부분에 사용자 정의 필드인 add_link 를 적용할 수 있다.
- 여기서는 post 인스턴스 객체를 add_link 함수의 파라미터로 받아서 정의된 작업을 진행한 이후에 content를 리턴한다.

```html
<!-- post_list.html -->
{% raw %}
{% for post in post_list %}
<ul>
  <!-- ...생략... -->
  <li>{{ post.author.profile.nickname }}</li>
  <li><img src="{{ post.photo.url }}" alt="{{ post.author }}'s photo"></li>
  <li>{{ post|add_link|safe }}</li>
  <!-- post 인스턴스 객체에 'add_link' 사용자정의 필터를 적용하였다 -->
  <!-- 참고) 내장 필터인 safe 필터를 사용하여, tag escape를 방지할 수 있다. -->
</ul>
{% endfor %}
{% endraw %}
```

## 결과물
- 사용자 정의 템플릿 필터를 사용하면 템플릿 랜더링 시에 원하는 대로 DB를 조작할 수 있다. (줄바꿈 추가하기, 필터링, html escape 처리 등)
- 좋은 점은 DB의 원본 데이터에는 영향을 미치지 않는다는 점이다.
- css 작업 전이라 아직 수수하지만 결과물은 아래와 같다. 해시태그 링크를 클릭하면 해당 해시태그를 가진 모든 post list가 화면에 출력 되도록 구현하였다. (이 부분에 대한 코드는 [github](https://github.com/wayhome25/Instagram) 에서 확인 가능하다.)

<br>
![스크린샷 2017-06-23 오전 12.47.21](http://i.imgur.com/3ojyWZi.jpg)
<center><figcaption>아직 아름답지는 않지만.. 원하는건 구현했다! </figcaption></center>
<br>
## 결론, 느낀점  
- 처음에는 다른 방법으로 고민을 많이해서 문제 해결에 시간이 많이 걸렸다.
- Post 모델에 메소드를 구현하고, 직접 content 필드 내의 문자열을 수정했더니 DB 자체에 a 태그가 포함되는 문제가 발생했다.
- 이걸 포기하지 않고 추가적으로 발생하는 문제를 계속 해결하려다 보니까 점점 시간만 흐르고 구렁텅이에 빠지는 기분이 들었다.
- 너무 하나를 고집하기 보다, 다른 방법을 생각해보는 자세도 필요한 것 같다.  
- 혼자서 조금이라도 고민하고 나서 검색하면 해결책을 찾을 가능성이 높아진다.
- 다른 일을 하고 있을 때 (ex. 식사중), 의외로 좋은 아이디어가 떠오르는 경우가 있다.
