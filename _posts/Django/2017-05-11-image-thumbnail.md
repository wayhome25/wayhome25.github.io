---
layout: post
title: 썸네일 만들기 (PILKit, imagekit) ImageSpecField, ProcessedImageField
category: Django
tags: [python, Django, thumbnail]
comments: true
---

> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

---


## 웹/앱에서 많이 쓰이는 이미지 포맷
- 이미지 용량을 줄이려면 메타데이터를 제거하고, 적절한 크기로 리사이징, 가급적 JPG 포맷 사용
1. JPEG : 손실압축 포맷, **파일 크기가 작음**, 압축률은 **60~80%가 적절**, 사진 이미지 유용
2. PNG : 투명채널 지원, 문자가 있는 이미지 유용
3. GIF : 256색 지원, 움짤 이미지

## 파이썬 이미지 처리 라이브러리
- PIL > Pillow > PILKit(라이브러리) > django-imagekit(앱)
1. **PIL** : 09년 이후 업데이트가 없음
2. **Pillow** : Pillow는 PIL 프로젝트에서 fork 되어서 나온 라이브러리로, PIL이 python 3를 지원하지 않기 때문에 pillow를 많이 사용하는 추세 (ImageField 사용시 필수)
3. **PILKit** : PIL, Pillow를 좀 더 쓰기 쉽도록 도와주는 라이브러리
4. **(참고) django-imagekit** : 이미지 썸네일 helper 장고 앱 (실제 이미지 처리시에는 PILKit 이 사용됨)
	- 설치 후, settings.INSTALLED_APPS에 imagekit 추가 필요

---

# PILKit
- PIL, Pillow를 좀 더 쓰기 쉽도록 도와주는 라이브러리
- pip install pilkit 으로 설치
- 다양한 Processors 지원
	- Thumbnail
	- Resize
	- Crop 등

## PILKit을 활용한 썸네일 생성, 저장 예시

```python
from PIL import Image #Pillow
from pilkit.processors import Thumbnail

processor = Thumbnail(width=300, height=300)
mountain_image = Image.open("mountain.jpg")

thumb_image = processor.process(mountain_image)
thumb_image.save("sample-300x300.jpg", quality=60)
```

---

# imagekit
- 이미지 썸네일 helper **장고 앱** (실제 이미지 처리시에는 PILKit 이 사용됨)

## 설치

```shell
$ pip install pillow # django-imagekit 사용을 위해서 사전 설치 필요
$ pip install pilkit # django-imagekit 사용을 위해서 사전 설치 필요
$ pip install django-imagekit

# pip 설치 후, settings.INSTALLED_APPS에 imagekit 추가 필요
```


## 활용 1. 원본 ImageField로 부터  생성 (원본o, 썸네일o) - ImageSpecField
- `ImageSpecField` 는 form에서는 렌더링 되지 않음

```python
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

class Post(models.Model):
	photo = models.ImageField()
	photo_thumbnail = ImageSpecField(
		source = 'photo', 		   # 원본 ImageField 명
		processors = [Thumbnail(100, 100)], # 처리할 작업목록
		format = 'JPEG',		   # 최종 저장 포맷
		options = {'quality': 60}) # 저장 옵션
```


## 활용 2. 원본 이미지를 재가공하여 저장 (원본x, 썸네일o) - ProcessedImageField (추천)
- `ProcessedImageField`

```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Post(models.Model):
	photo_thumbnail = ProcessedImageField(
		upload_to = 'blog/post',
		processors = [Thumbnail(100, 100)], # 처리할 작업 목룍
		format = 'JPEG',					# 최종 저장 포맷
		options = {'quality': 60})  		# 저장 옵션
```

## 활용 3. 템플릿에서 이미지 직접 처리 (추천)
- widht, height, crop, upscale 설정 가능

```html
{% raw %}

<!-- 썸네일 이미지 태그 생성 -->
{% thumbnail "100x100" post.photo %}

<!-- 썸네일 file object 획득 -->
{% thumbnail "100x100" post.photo as thumb %}
<img src="{{ thumb.url }}" alt="" width="{{ thumb.width }}" height="{{ thumb.height }}">

<!-- 추가 속성 정의 -->
{% thumbnail "100x100" post.photo -- style="" onclick="" class="" %}

{% endraw %}
```
