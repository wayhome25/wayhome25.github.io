---
layout: post
title: 장고 모델 폼 (Model Form)
category: Django
tags: [python, Django, form]
comments: true
---

> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

---

# Model Form

- form 클래스를 상속받은 클래스 (forms.ModelForm)
- form 을 만들 때 model 클래스의 내역 그대로 form을 만든다면, (Model Form)   
  forms.py 에서 form 필드를 중복해서 정의할 필요가 없다
- 모델과 관련된 form 이라면 모델 폼을 사용하는 것이 좋다

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
		fields = ['title', 'content'] # '__all__' 설정시 전체 필드 추가
```

---

## ModelForm.save(commit=True)
- Model Form 클래스에는 .save(self, commit=True) 메소드가 구현되 었음  
- DB 저장 여부를 commit flag를 통해서 결정
- commit=False flag를 통해 함수 호출을 지연

```python
# dojo/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Post
		fields = ['title', 'content']

	''' 내부적으로 구현되어 있음 (멤버변수 인스턴스)
		향후 수정 기능 구현시 활용
	def save(self, commit=True):
		self.instance = Post(**self.cleaned_data)
		if commit:
			self.instance.save()
		return self.instance
	'''
```

### 사용예시
- form.save(commit=False) 를 통해서 DB save 를 지연시켜 중복 save를 방지한다.


```python
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
		if form.is_valid():
			post = form.save(commit=False) # 중복 DB save를 방지
			post.ip = request.META['REMOTE_ADDR'] # ip 필드는 유저로 부터 입력 받지 않고 프로그램으로 채워 넣는다
			post.save()
			return redirect('/dojo/')
	else:
		form = PostForm()
	return render(request, 'dojo/post_form.html',{
		'form': form,
	})
```

---
## ModelForm을 활용한 Model Instance 수정
- 수정 대상이 되는 model instance 를 Model Form 인스턴스 생성시에 instance 인자로서 지정한다

```python
# myapp/views.py
def post_edit(request, id):
	post = get_object_or_404(Post, id=id)

	if request.method == 'POST':
		form = PostModelForm(request.POST, request.FILES, instance=post) # NOTE: instance 인자(수정대상) 지정
		if form.is_valid():
			post = form.save()
			return redirect(post) # NOTE: post 인스턴스의 get_absolute_url 메소드 호출!
	else:
		form = PostModelForm(instance=post)
	return render(request, 'myapp/post_form.html',{
		'form': form,
	})
```


---

## (중요) .cleaned_data 을 끝까지 활용할 것!

### cleaned_data
- .is_valid() 를 통해서 검증에 통과한 값은 `cleaned_data` 변수명으로 `사전타입` 으로 제공된다.

```python
def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES) # NOTE: 인자 순서주의 POST, FILES
		if form.is_valid():
			print(form.cleaned_data) # {'title': '테스트', 'content': '내용'}
		# ... 생략 ...
```

### request.POST['key'] 보다는 form.cleaned_data['key'] 와 같이 사용
- request.POST 데이터는 form instance의 초기 데이터
- 따라서 form clean 함수 등을 통해 변경될 가능성이 있음

```python
# myapp/forms.py
class CommentForm(forms.Form):
	def clean_message(self): # Form 클래스 내 clean 멤버함수를 통해 값 변경이 가능
		return self.cleaned_data.get('message', '').strip() # 좌우 공백 제거


# myapp/views.py
# BAD Case!! - request.POST를 통한 접근
form = CommentForm(request.POST)
if form.is_valid():
	# request.POST : 폼 인스턴스 초기 데이터
	message = request.POST['message']
	comment = Comment(message=message)
	comment.save()
	return redirect(post)

# GOOD Case!! - form.cleaned_data를 통한 접근
form = CommentForm(request.POST)
if form.is_valid():
	# form.cleaned_data : 폼 인스턴스 내에서 clean 함수를 통해 변환되었을 수도 있을 데이터
	message = form.cleaned_data['message']
	comment = Comment(message=message)
	comment.save()
	return redirect(post)
```
