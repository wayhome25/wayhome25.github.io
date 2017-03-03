---
layout: post
title: django 03. 첫번째 장고앱 7 - MTV 연동하기
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 03. 첫번째 장고앱 7 - MTV 연동하기
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## view - template - model 연동

<center>
<figure>
<img src="/assets/post-img/django/mtv.png" alt="">
<figcaption>장고와 MTV</figcaption>
</figure>
</center>

### `urls.py` 수정
root 경로에 views 오브젝트의 index메소드를 연결한다.

```shell
url(r'^$', views.index, name = 'index'),
```

### `views.py` 수정
models 오브젝트의 GuessNumbers 클래스를 import 하고, 데이터를 불러온다.    
불러온 데이터를 템플릿에 딕셔너리 형식으로 전달한다.

- `lottos = GuessNumbers.objects.order_by(‘-update_date’)` 를 통해 작성일 기준 내림차순으로 데이터를 가져올 수 있다.

```python
{% raw %}

from .models import GuessNumbers

def index(request):
    lottos = GuessNumbers.objects.all() #shell에서 하는 것 처럼 데이터를 읽어온다.
    return render(request, 'lotto/default.html', {'lottos': lottos}) # 템플릿 파일 경로 지정
{% endraw %}
```

### `template 파일(defaul.html)` 수정
views에서 불러온 models의 데이터(오브젝트)를 template파일에 적용한다.    
- 반복문을 통해서 필요한 정보를 html에 표시한다.
- [linebreaksbr](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#linebreaks) 속성 통해서 줄바꿈


```html
{% raw %}
<div class="container lotto">
  {% for lotto in lottos %}
  <h2>{{lotto.text}}</h2>
  <p>last update : {{lotto.update_date}} by {{lotto.name}}</p>
  <p>{{lotto.lottos|linebreaksbr}}</p>
  {% endfor %}
</div>
{% endraw %}
```
