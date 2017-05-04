---
layout: post
title: Queryset을 활용한 아주 간단한 필터검색 구현
category: Django
tags: [python, Django, 검색, Queryset]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.



## 검색을 위한 form 추가 (template)

```html
<!-- post_list.html -->

{% raw %}
<form action="" method="get">
  <input type="text" name="q" value="{{ q }}">
  <input type="submit" value="검색">
</form>
{% endraw %}
```


## input text에 따른 필터링 조회처리 (view)

```python
# blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링

    return render(request, 'blog/post_list.html', {
        'post_list' : qs,
        'q' : q,
    })

```

## 결과화면

![스크린샷 2017-05-04 오후 12.30.11](http://i.imgur.com/n2m6qms.png)
