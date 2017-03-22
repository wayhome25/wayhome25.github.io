---
layout: post
title: django 04. 장고 개인 프로젝트 1 - 개발과정 기록   
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 04. 장고 개인 프로젝트 (메모 앱)
> 첫 장고 개인 프로젝트 진행 중 새롭게 배운 부분을 정리하였습니다.

## 결과물
- <http://siwabada.pythonanywhere.com/>


## 장고 프로젝트 준비

- 가상환경(virtualenv) 설치 및 장고 설치
- 프로젝트 및 app 생성 (setting.py 수정)


## Model 클래스 작성
> DB 연동을 위한 model class를 작성한다.

- 모델 내에 모델 클래스 작성 (models.py)후, 장고에 migrate - DB 테이블과 유사
- admin superuser 등록 후, admin.py에 모델 클래스 등록
- 장고 가이드 문서 [Model field reference](https://docs.djangoproject.com/en/1.10/ref/models/fields/#model-field-types) 를 통해 model field의  data type, optiond 을 참고할 수 있다.
- models.py 에 모델 클래스 작성 후, 장고에게 모델을 만들었다는 걸 알려줘야 한다.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

- 클래스 대표 값은 `__str__` 메소드를 통해서 정의한다.

```python
def __str__(self):
      return '%s by %s' % (self.title, self.name)
```

- 작성 시간은 `timezone 모듈`을 사용한다. (models.py 코드예시)

```python
from django.db import models
from django.utils import timezone

# Create your models here.
class Memos(models.Model):
    name = models.CharField(max_length = 20, db_column='이름')
    title = models.CharField(max_length = 50, db_column='제목')
    text = models.TextField(max_length = 150, db_column='내용', help_text='메모 내용은 150자 이내로 입력 가능합니다.')
    update_date = models.DateTimeField()
    priority = models.BooleanField(db_column='중요')

    def generate(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s by %s' % (self.title, self.name)
```



## views와 템플릿, 템플릿과 정적파일 연동

- 템플릿 폴더 및 html 파일 작성 후, views와 연동
- 템플릿 html 파일과 static css 파일 연동
- static 파일 작성 후 장고에게 알려준다 - collectstatic
- 템플릿 파일(html) 경로 : memo_app/template/memo_app/default.html
- 정적 파일(css) 경로 : memo_app/static/css/default-style.css

## MTV 연동하기
- view에 model 클래스를 import 하고 데이터 불러오기
- view에서 불러온 model 클래스 데이터를 template파일에 for문으로 적용하기

## 입력 - form 만들기, post 처리
- app 폴더 내부에 forms.py 작성, 모델 클래스 추가
- form.html 템플릿 작성
- urls.py 추가 후에 view 와 연결(forms.py 데이터 가져오기), view와 템플릿 연결
- post 분기 처리를 위한 views.py 수정

## 수정 - modify 처리
> 가이드 문서 찾아보고 적용 하느라 오래걸렸다..ㅠㅠ 조만간 이런때도 있었지 하고 추억하는 날이 오겠지!

### url 패턴 추가 (urls.py)
> primary key를 url 일부분으로 갖는 url 패턴 추가

```python
urlpatterns = [
    ...
    url(r'^(?P<memokey>[0-9]+)/modify/$', views.modify, name='modify_memo'),
]
```
### view에 modify 메소드 추가 (views.py)
> 클래스 PostForm import 필요
> 수정하는 화면 / 수정후 저장하는 POST request 분기 필요
> 기존에 존재하는 데이터는 form = PostForm(instance = memo) 를 통해 다시 가져올 수 있음

```python
from .forms import PostForm

def modify(request, memokey): #memokey 변수를 url에서 가져온다
    if request.method == "POST":
        #수정 저장
        memo = Memos.objects.get(pk = memokey)
        form = PostForm(request.POST, instance=memo) # 새로 입력된 인스턴스 데이터를 form 인스턴스에 새로 담는다.
        if form.is_valid():
             form.save() # 변경한 form을 저장한다 (수정, 업데이트)
             return redirect('index')
    else:
        #수정 입력
        memo = Memos.objects.get(pk = memokey) # 특정 데이터를 인스턴스에 담는다.
        form = PostForm(instance = memo) # 기존에 존재하는 데이터를 가져온다. (수정화면에 내용 포함)
        return render(request, 'memo_app/modify.html', {'memo' : memo, 'form' : form})
```

### modify.html 탬플릿 추가
> 인스터스로 가져온 form을 그대로 표시한다. (입력화면과 동일)

```html
{% raw %}
<form method="POST" class="post-form">
  {%csrf_token%}
  {{form.as_ul}}
  <button type="submit" class="save btn btn-default">저장</button>
</form>
{% endraw %}
```

### 각 데이터의 primary key를 url로 받도록 처리

```html
{% raw %}
<a href="{% url 'modify_memo' memokey=memo.pk %}" class="btn btn-primary modify" role="button">수정</a>
{% endraw %}
```

## 삭제 - delete 처리
### url 패턴 추가 (urls.py)
> primary key를 url 일부분으로 갖는 url 패턴 추가

```python
urlpatterns = [
    ...
    url(r'^(?P<memokey>[0-9]+)/delete/$', views.delete, name='delete_memo'),
]
```
### view에 delete 메소드 추가 (views.py)
> memokey 를 primary key로 갖는 특정 데이터를 인스턴스로 받고, 해당 인스턴스 데이터를 삭제

```python
def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    memo.delete()
    return redirect('index')
```

### 각 데이터의 primary key를 url로 받도록 처리
> 삭제버튼 클릭시 confirm 결과에 따라 submit을 취소 할 수 있다.

```html
{% raw %}
<a href="{% url 'delete_memo' memokey=memo.pk %}" class="btn btn-default del" role="button" onclick="return confirm('정말 삭제하시겠습니까?')">삭제</a>
{% endraw %}
```
