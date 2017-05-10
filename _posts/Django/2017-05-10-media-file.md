---
layout: post
title: 장고 미디어 파일 (Media Files) - 사진업로드, 파일서빙
category: Django
tags: [python, Django, media files]
comments: true
---

> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

---


# 미디어 파일 (Media File)

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->
## 목차
* [static and media Files](#static-and-media-files)
* [media files 전달 및 저장 (settings.py)](#media-files-전달-및-저장-settingspy)
* [FileField / ImageField (models.py)](#filefield-imagefield-modelspy)
	* [Pillow](#pillow)
* [파일 업로드시의 form enctype, 템플릿내 media url 처리 (template)](#파일-업로드시의-form-enctype-템플릿내-media-url-처리-template)
	* [form enctype](#form-enctype)
	* [template 내 media url 처리](#template-내-media-url-처리)
* [파일 저장경로](#파일-저장경로)
	* [upload_to 필드옵션을 통한 파일 저장경로 수정 (models.py)](#upload_to-필드옵션을-통한-파일-저장경로-수정-modelspy)
* [개발환경에서의 media 파일서빙 (urls.py)](#개발환경에서의-media-파일서빙-urlspy)

<!-- tocstop -->

## static and media Files
- __static files__ : `개발 리소스` 로서의 정적인 파일 (js, css, image etc)
	- 앱 단위로 저장/서빙
	- 프로젝트 단위로 저장/서빙
- __media files__ : 유저가 `업로드` 한 모든 정적인 파일 (image, pdf etc)
	- `프로젝트 단위로` 저장/서빙

## media files 전달 및 저장 (settings.py)
1. view : HttpRequest.FILES를 통해 파일이 전달되고,
2. view : settings.MEDIA_ROOT 디렉토리 하단에 파일 저장

- __관련 settings 예시__

```python
# mysite/settings.py

# 각 media 파일에 대한 URL Prefix
MEDIA_URL = '/media/' # 항상 / 로 끝나도록 설정
# MEDIA_URL = 'http://static.myservice.com/media/' 다른 서버로 media 파일 복사시

# 업로드된 파일을 저장할 디렉토리 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## FileField / ImageField (models.py)
- models.FileField : 파일 저장을 지원하는 모델 필드
- models.ImageField : 이미지 저장을 지원하는 모델 필드 (FileField 상속)
- 제출된 파일, 이미지는 settings.MEDIA_ROOT 경로에 파일을 저장하고,    
  DB 필드에는 settings.MEDIA_ROOT 내 저장된 하위 경로를 저장

- __관련 model필드 예시__

```python
# blog/models.py

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	photo = models.ImageField(blank=True)
```

### Pillow
- PIL(Python Image Library)의 일종, 파이썬으로 이미지들을 처리하고 싶을 때 사용
- Pillow는 PIL 프로젝트에서 fork 되어서 나온 라이브러리로, PIL이 python 3를 지원하지 않기 때문에 pillow를 많이 사용하는 추세
- 이미지관련 width, height, format, resize 작업을 수행

```shell
$ pip install pillow
```

---

## 파일 업로드시의 form enctype, 템플릿내 media url 처리 (template)

### form enctype
- template html의 form에서 유저가 파일을 업로드 하기 위해서는 몇 가지 설정이 필요하다.
1. __form method__ : 반드시 POST 로 설정이 필요하다.
2. __form enctype__ : multipart/form-data 로 설정이 필요하다.

```html
{% raw %}
<form method='post' action='' enctype="multipart/form-data">
	{% csrf_token %}
	<table>
		{{ form.as_table }}
	</table>
	<input type="submit">
</form>
{% endraw %}
```

### template 내 media url 처리
- settings.MEDIA_URL 설정은 언제라도 변경될 수 있다.
- 따라서 ImageField, FileField 의 .url 속성을 사용하는게 좋다 (settings.MEDIA_URL이 prefix로 붙음)
- 참고로 .path 속성은 파일시스템 상의 절대경로 (settings.MEDIA_ROOT 가 Prefix로 붙음)

```html
{% raw %}
<h2>{{ post.title }}</h2>
{% if post.photo %}
path :{{ post.photo.path }} # /Users/nickname/documents/practice/media/jeju_pic.png
url : {{ post.photo.url }} # /media/jeju_pic.png
<img src="{{ post.photo.url }}" alt="">
{% endif %}
{% endraw %}
```

---

## 파일 저장경로
- 저장경로 : `settings.MEDIA_ROOT/파일명` 경로에 저장
- DB : 파일명이 string으로 저장

### upload_to 필드옵션을 통한 파일 저장경로 수정 (models.py)
- 한 디렉토리에 파일이 몰릴 경우, OS 파일 찾기 기능이 저하된다.
- 디렉토리 depth가 깊어지는 것은 성능에 큰 영향이 없다.
- 대책 예시 : 업로드 시간대 별로 다른 디렉토리에 저장

```python
# blog/models.py

from django.db import models

class Post(models.Model):
	profile_pic = models.ImageField(upload_to="blog/profile_pic")
	# 저장경로 : MEDIA_ROOT/blog/profile_pic/xxxx.jpg 경로에 저장
	# DB필드 : 'MEDIA_URL/blog/profile_pic/xxxx.jpg' 문자열 저장
	photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
	# 저장경로 : MEDIA_ROOT/blog/2017/05/10/xxxx.jpg 경로에 저장
	# DB필드 : 'MEDIA_URL/blog/2017/05/10/xxxx.jpg' 문자열 저장
```

---

## 개발환경에서의 media 파일서빙 (urls.py)
- static 파일과는 다르게 개발서버에서 기본 서빙 미지원
- 개발 편의성 목적으로 서빙 rule 추가 가능
- settings.DEBUG = False 일때는 static 함수에서 빈 리스트 리턴

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
