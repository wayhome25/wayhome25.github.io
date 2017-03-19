---
layout: post
title: Django 기본 04 - Class Based View 응답예시 (JSON, 템플릿)
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.


# Class Based View (CBV)
- `django.views.generic` : 뷰 사용패턴을 일반화 시켜놓은 뷰의 모음
- `.as_view()` : 클래스함수를 통해, FBV를 생성해주는 클래스
- **FBV로 구현한 view는 CBV로도 구현 할 수는 있다.** 하지만 CBV는 패턴화 되어 있는 뷰를 처리할 때 효율적으로 처리 할 수 있다. (적은 코드로 뷰를 구현할 수 있음)
- 공부할 때 처음에는 `함수기반 뷰(FBV)` 로 구현을 많이 해보고 나서, `클래스기반 뷰(CBV)`를 사용하는 것이 좋다. (FBV를 충분히 이해하지 않은 상태에서 CBV를 사용하면 나중에 코드가 산으로 갈 위험이 있다.)

## FBV 예시
1. 직접 문자열로 HTML 형식 리스폰스
2. 템플릿을 통해 HTML 형식 리스폰스
3. JSON 형식 리스폰스
4. 파일 다운로드 리스폰스


## 직접 문자열로 HTML 형식 리스폰스

```python
from django.http import HttpResponse
from django.views.generic import View

class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
                <h1> hello, </h1>
                <p>{name}</p>
                <p>반가워요</p>
                '''

post_list1 = PostListView1.as_view()
```

## 템플릿을 통해 HTML 형식 리스폰스

```python
from django.views.generic import View, TemplateView

class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()
```

## JSON 형식 리스폰스

```python
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView

class PostListView3(View):
    def get(self,request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': True})

    def get_data(self):
        return{
            'message' : '안녕 파이썬 장고',
            'items' : ['파이썬', '장고', 'AWS', 'Azure'],
        }

post_list3 = PostListView3.as_view()
```
