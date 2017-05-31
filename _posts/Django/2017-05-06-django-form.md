---
layout: post
title: 장고 폼 (form)
category: Django
tags: [python, Django, form]
comments: true
---

> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

---

# form
- 장고의 가장 큰 Feature 중 하나
- Model 클래스와 유사하게 `Form 클래스`를 정의

## 주요역할 (custom form class)
- 입력폼 html 생성 : as_table(), as_p(), as_ul() 기본 제공
- 입력폼 값 검증 (validation)
- 검증에 통과한 값을 `사전타입`으로 제공 (cleaned_data)

## Form vs Model Form (폼과 모델폼의 차이점)
- Form (일반 폼) : 직접 필드 정의, 위젯 설정이 필요
- Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성

```python
from django import forms
from .models import Post

# Form (일반 폼)
class PostForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)

# Model Form (모델 폼)
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
```


## Form Fields
- [공식문서](https://docs.djangoproject.com/en/1.10/ref/forms/fields/)
- Model Fields 와 유사
	- Model Fields : DB Field 듣을 파이썬 클래스화
	- Form Fields : HTML Form Field 들을 파이썬 클래스화

---

# 단계별 구현

## django style
**폼 처리 시에 _같은 URL (같은 view)_ 에서 GET/POST로 나눠서 처리**

```python
def post_new(request):
	if request.method == 'POST':
		pass

	else:
		pass
```

- GET 방식 request
	- 입력폼을 보여준다
- POST 방식 request
	- 데이터를 입력 받아서 검증 (validation)
	- 검증 성공 시 : 해당 데이터를 저장하고 success URL로 이동
	- 검증 실패 시 : 오류 메시지와 함께 입력폼을 다시 보여준다


## Step 0. Model class 정의

```python
# myapp/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

	def get_absolute_url(self): # redirect시 활용
        return reverse('myapp:post_detail', args=[self.id])
```

## Step 1. Form class 정의

```python
# myapp/forms.py
from django import forms

class PostForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=form.Textarea)

	# ModelForm.save 인터페이스를 흉내내어 구현
	def save(self, commit=True):
		post = Post(**self.cleaned_data)
		if commit:
			post.save()
		return post
```

---

## Step 2. form 필드 별로 유효성 검사 함수 추가 적용  
- 기본 유효성 검사는 값의 유무  
- form 에서는 리턴값을 따로 처리하지 않고, `forms.ValidationError` 예외발생 유무로 처리
- `validators 는 form 보다 Model 에 적용하는게 좋다.`

```python
# myapp/forms.py
from django import forms

def min_length_3_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('3글자 이상 입력해주세요')


class PostForm(forms.Form):
	title = forms.CharField(validators=[min_length_3_validator]) # 한줄 문자입력창, 커스텀 validators 옵션 지정 가능
```

### 참고 (models.py)

- model class 정의시에 validators 옵션 적용 가능
- 아래와 같이 `model에 validators 를 정의하는 것을 권장` (Model Form에 그대로 적용 가능)
- admin 사이트에서도 validator 동작 (admin도 Model Form을 생성하여 사용하기 때문)

```python
from django import forms
from django.db import models


def min_length_3_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('3글자 이상 입력해주세요')

class Post(models.Model):
	title = models.CharField(max_length=100, validators=[min_length_3_validator])
```

---

## Step 3. view 함수 내에서 form 인스턴스 생성

```python
# myapp/views.py
from django.shortcuts import render
from .forms import PostForm

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
	else:
		form = PostForm()
	return render(request, 'dojo/post_form.html',{
		'form': form,
	})

```



---

## Step 4. POST 요청에 한해 입력값 유효성 검증 및 저장처리

```python
def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
		if form.is_valid(): # form의 모든 validators 호출 유효성 검증 수행
		# 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
		# 검증에 실패시 form.error 에 오류 정보를 저장
		'''
		# 저장방법1) - 가장 일반적인 방법
		post = Post()
		post.title = form.cleaned_data['title']
		post.content = form.cleaned_data['content']
		post.save()

		# 저장방법2)
		post = Post(title = form.cleaned_data['title'],
					content = form.cleaned_data['content'])
		post.save()

		# 저장방법3)
		post = Post.objects.create(title = form.cleaned_data['title'],
									content = form.cleaned_data['content'])

		# 저장방법4)
		post = Post.objects.create(**form.cleaned_data) # unpack 을 통해 방법3과 같이 저장
		'''

		# 저장방법5)
		post = form.save() # PostForm 클래스에 정의된 save() 메소드 호출
		return redirect(post) # Model 클래스에 정의된 get_absolute_url() 메소드 호출
	else:
		form = PostForm()
		return render(request, 'dojo/post_form.html',{
		'form': form, 	# 검증에 실패시 form.error 에 오류 정보를 저장하여 함께 렌더링
		})
```

---

## Step 5. 템플릿을 통해 HTML 폼 생성
- GET 요청, POST 요청이지만 유효성 검증에 실패시, form 인스턴스를 통해 html 폼 출력
- 오류메시지가 있다면 함께 출력

```html
{% raw %}
<form action="" method="post">
	{% csrf_token %}
	<table>
		{{ form.as_table }}
	</table>
	<input type="submit">
</form>
{% endraw %}
```
