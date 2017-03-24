---
layout: post
title: django 07. 세번째 장고앱 04. 사진 업로드 모델 생성 / MEDIA_URL 설정
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)    
> 세번째 장고앱 '킬로그램'에 이미지 업로드 모델을 구현한다.

# 이미지 업로드 구현하기
- Photo 모델을 만들어 이미지 업로드 하고,
- 업로드한 이미지가 MEDIA_URL을 사용해서 저장이 되고 잘 보여지는지 확인한다.

## media url 설정하기

- mysite/settings.py 수정

```python
# Media files - 업로드를 하는 URL과 디렉토리 설정
MEDIA_URL = '/files/' # 업로드 할 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads') #로컬 디렉토리 어디에 저장할 것인지
```

## photo model 생성하기


### kilogram/model.py 수정

```python
from django.db import models
from django.conf import settings
# Create your models here.

def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png

class Photo(models.Model):
    image = models.ImageField(upload_to = user_path) # 어디로 업로드 할지 지정
    owner = models.ForeignKey(settings.AUTH_USER_MODEL) # 로그인 한 사용자, many to one relation
    thumname_image = models.ImageField(blank = True) # 필수입력 해제
    comment = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True) # 레코드 생성시 현재 시간으로 자동 생성
```

### pillow 설치

- ImageField 사용시 에러가 발생하므로 pillow 패키지를 설치한다.    
  (Cannot use ImageField because Pillow is not installed.)

```
$ pip install pillow
```

### migrate 수행

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### admin.py 수정 및 admin을 통한 확인
```
from .models import Photo

# Register your models here.
admin.site.register(Photo)
```

## media url 을 static url로 설정하기
- admin에서 업로드한 이미지 경로로 접속하면 Page not found 문제 발생 (배포관련 문제)
- 디버깅모드에서는 해당 문제 해결 옵션이 존재 (디버그 모드에서만 동작)
- **mysite/urls.py 수정**

```python
from django.conf import settings
from django.conf.urls.static import static

# 어떤 URL을 정적으로 추가할래? > MEDIA_URL을 static 파일 경로로 추가
# 실제 파일은 어디에 있는데? > MEDIA_ROOT 경로내의 파일을 static 파일로 설정
urlpatterns +=
  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),


```
