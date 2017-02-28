---
layout: post
title: django 03. 첫번째 장고앱 2 - urls.py 와 views.py 수정
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 03. 첫번째 장고앱 2 - urls.py 와 views.py 수정
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## urls.py와 views.py 수정

### urls.py 수정 (프로젝트 폴더 - mysite)

- `__init.py__` : 해당 파일이 있는 폴더가 `module` 이라는 의미
- `setting.py` : 장고 setting
- `urls.py` : url 규칙
  - 모듈 및 url 추가 예시

  ```python
  from mylotto import views
  # mylotto app모듈 추가

  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      # url(r'^$', views.index),
      # 정규표현식 ^시작 $끝
      # 아무것도 url을 입력하지 않았을 때, mylotto의 views의 index 메소드를 실행해라
      url(r'^hello/$', views.index, name='hello'),
      # /hello url로 접속했을 때 mylotto의 views의 index 메소드를 실행해라
  ]
  ```

### url 패턴 작성을 위한 정규표현식(regex) [참고(장고걸스)](https://tutorial.djangogirls.org/ko/django_urls/)

```
^ 문자열이 시작할 때
$ 문자열이 끝날 때
\d 숫자
+ 바로 앞에 나오는 항목이 계속 나올 때
() 패턴의 부분을 저장할 때
```

- 이외에 url 정의는 문자적으로 만들 수 있다.
- 예시 :  http://www.mysite.com/post/12345/ 여기에서 12345는 글 번호를 의미

뷰마다 모든 글 번호을 작성하는 것은 정말 힘든 일이 될 거에요. 정규 표현식으로 url과 매칭되는 글 번호를 뽑을 수 있는 패턴을 만들 수 있어요. 이렇게 말이죠.    
`^post/(\d+)/$` 어떤 뜻인지 하나씩 나누어 어떤 뜻인지 알아볼게요.

- `^post/`는 장고에게 url 시작점에 (오른쪽부터) post/가 있다는 것을 말해 줍니다.
- `(\d+)`는 숫자(한 개 또는 여러개) 가 있다는 뜻입니다. 내가 뽑아내고자 글 번호가 되겠지요.
- `/`는 장고에게 /뒤에 문자가 있음을 말해 줍니다.
- `$`는 URL의 끝이 방금 전에 있던 /로 끝나야 매칭될 수 있다는 것을 나타냅니다.

### views.py 수정 (앱폴더 - mylotto)
- views 에 index 메소드 추가
- `HttpResponse` 모듈 import


```python
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>로또앱 index!</h1>')
```


### 요약
- `urls.py`에 url 규칙을 넣어준다. (정규표현식)
- 장고에 웹서버가 하나 있고, 브라우저에서 입력한 주소를 프로젝트 폴더의 urls.py에서 패턴을 분석한다.    
- 맞는 패턴이 있으면 해당하는 메소드를 실행한다.
