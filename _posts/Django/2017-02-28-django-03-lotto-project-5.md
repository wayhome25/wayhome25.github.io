---
layout: post
title: django 03. 첫번째 장고앱 5 - VIEWS와 템플릿, 정적파일 연동
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 03. 첫번째 장고앱 5 - VIEWS와 템플릿, 정적파일 연동
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## views와 템플릿 연동
- `urls.py` 수정 (위치 : 프로젝트 폴더 - mysite)

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lotto/$', views.index, name = 'index'),
]
```

- `views.py` 수정 (위치 : 앱 폴더 - mylotto)

```python
def index(request):
    return render(request, 'lotto/default.html', {}) # 템플릿 파일 경로 지정
```

- 템플릿 폴더 및 html 템플릿 파일 작성
  - 경로 : `mylotto/templates/lotto/default.html` (app 폴더 내)
  - 장고 사이트에 여러 어플리케이션 등록 가능, 나중에 중복생성하지 않기 위해서 템플릿을 위 경로에 작성
  - http://127.0.0.1:8000/lotto/ 를 통해서 템플릿 연동 완성!

- `static` 파일 연동하는 방법
  - static 폴더 경로 : `mylotto/static/css/lotto.css` (app 폴더 내)
  - 템플릿 html 파일 내에서 css 연동 (\ 무시)

  ```html
    {% raw %}
    <!DOCTYPE html>
    {% load staticfiles %}
    ...
    ...
    <link rel="stylesheet" href="{% static 'css/lotto.css'%}">
    {% endraw %}
  ```
  - 장고에게 static 파일이 (css) 생겼다는 걸 알려준다.

  ```
  python manage.py collectstatic
  ```
