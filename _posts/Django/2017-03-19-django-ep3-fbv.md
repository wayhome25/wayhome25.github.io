---
layout: post
title: Django 기본 03 - Function Based View 응답예시 (JSON, 파일다운, 템플릿)
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# view
- view / view 함수
- URLConf에 매핑된 Callable Object
  - 파이썬에는 함수 이외에도 다양한 호출 가능한 객체가 존재함
  - 첫번째 인자로 [HttpRequest](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpRequest) 인스턴스를 받는다.   
  - **필히 [HttpResponse](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse) 인스턴스를 리턴** 해야한다.
- 크게 `Function Based View` (FBV)와 `Class Based View` (CBV)로 구분한다.


-----
# Fucntion Based View

## FBV 예시
1. 직접 문자열로 HTML 형식 리스폰스
2. 템플릿을 통해 HTML 형식 리스폰스
3. JSON 형식 리스폰스
4. 파일 다운로드 리스폰스

## FBV 예시1 - 직접 문자열로 HTML 형식 리스폰스

```python
# myapp/views.py
from django.http import HttpResponse

def post_list1(request):
    name = '공유'
    return HttpResponse('''
                        <h1> hello, </h1>
                        <p>{name}</p>
                        <p>반가워요</p>
                        '''.format(name=name))
```

## FBV 예시2 - 템플릿을 통해 HTML 형식 리스폰스

```python
# myapp/views.py
from django.shortcuts import render

def post_list2(request):
    name = '홍철'
    return render(request, 'dojo/post_list.html', {'name': name})
```

```html
<!-- myapp/templates/myapp/post.list.html -->
{% raw %}
<h1>hello</h1>
<p>{{name}}</p>
<p>반가워요</p>
{% endraw %}
```

## FBV 예시3 - JSON 형식 리스폰스

```python
# myapp/views.py
from django.http import HttpResponse, JsonResponse

def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '장고', 'AWS', 'Azure'],
    }, json_dumps_params = {'ensure_ascii': True})
```

<center>
<figure>
<img src="/assets/post-img/django/json.png" alt="views">
<figcaption>FBV의 json 형식 리스폰스</figcaption>
</figure>
</center>

- 크롬확장프로그램 [JsonView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=ko) 를 통해서 서버에서 전달한 Json 응답을 브라우저에서 읽기 쉽도록 표시

## FBV 예시4 - 파일 다운로드 리스폰스

```python
# myapp/views.py
import os
from django.http import HttpResponse

def excel_download(request):
    # 현재 프로젝트 최상위 (부모폴더) 밑에 있는 'scimagojr-3.xlsx' 파일
    filepath = os.path.join(settings.BASE_DIR, 'scimagojr-3.xlsx')
    filename = os.path.basename(filepath) # 파일명만 반환

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

# settings.py
# 현재 파일의 부모경로, 부모경로를 반환
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

- **os.path.dirname(path)** : 입력받은 파일/디렉터리의 경로를 반환
- **os.path.join(path1[,path2[,...]])** : 해당 OS 형식에 맞도록 입력 받은 경로를 연결
- **os.path.basename(path)** : 입력받은 경로의 기본 이름(base name)을 반환한다. abspath() 함수와 반대되는 기능을 수행
