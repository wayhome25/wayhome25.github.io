---
layout: post
title: django 06. 두번째 장고앱 12 - generic view 적용하기
category: Django
tags: [python, 파이썬, Django, generic view]
comments: true
---

> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## Class-based View

### Class-based View 특징 - function based view 와의 차이점
- [class-based view 가이드 문서](https://docs.djangoproject.com/en/1.10/topics/class-based-views/)
- GET, POST 와 같은 HTTP 메소드를 별도의 파이썬 메소드로 처리 (가독성이 높아짐)
- 객체 지향의 장점을 적용 가능 (재사용성, Mixin 등)
- 복잡한 구현을 가능하게 해줌

---
## Class-based Generic views

- 웹 개발시 자주 사용하는 기능을 장고에서 미리 제공해 줌 (generic 예시)
  - generic 사용을 위해서는 외부 모듈 적용이 필요하다. `from django.views import generic`
  - `generic.ListView` : index view는 class 전체를 가져와서 object 리스트의 간략한 정보를 화면에 표시한다.
  - `generic.DetailView` : 한 객체를 가지고 거기에 따른 세부 정보를 화면에 표시한다.  

- 코드의 단순화, 빠른 개발을 가능하게 함
- 투표 앱의 index() - 객체 전체 리스트를 화면에 표시
- results(), detail() - 한 객체의 세부 정보를 화면에 표시

---
## generic view 적용하기
- polls/ulrs.py 수정
```python
    # 보통 클래스 뷰의 이름은 대문자로 시작하고 끝에 View가 붙는다 (IndexView, DetailView, ResultsView 등)
    # .as_view() 를 통해서 generic view를 적용할 수 있다.
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
```
- `주의사항`: generic view를 위해서는 매개변수 이름이 `pk`여야 한다.

---
- views.py 수정

```python
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' #파라미터를 무슨 이름으로 넘길 것인가?

    def get_queryset(self): # 메소드 오버라이딩
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # 어느 모델과 연결해서 어느 템플릿으로 넘겨 줄지 정의한다.
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
```
