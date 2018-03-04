---
layout: post
title: Django 배포연습 1 - settings, wsgi 분리
category: Django
tags: [django, deploy, settings, wsgi]
comments: false
---

> nginx, uwsgi, docker를 활용한 배포 연습 과정을 기록한 글입니다.   
> 개인 공부후 자료를 남기기 위한 목점임으로 내용상에 오류가 있을 수 있습니다.
>
> - nginx, uwsgi를 통해서 아마존 EC2에서 장고 앱 어플리케이션을 실행시켜 보는 것을 목표로 한다.
> - 최소한의 설정만을 포함한다.


# settings.py 분리하기
- 배포 전에 다양한 프로젝트 설정을 포함하는 settings.py를 실행환경별로 분리한다.  
  (실행 환경별로 필요한 프로젝트 설정이 다르기 때문)
  - base.py (공통)
  - debug.py (개발용)
  - deploy.py (배포용)
- 장고 어플리케이션의 기본 진입점
  - manage.py
  - 프로젝트/wsgi.py


## 설정파일 구성
- 각각의 설정파일에서 사용할 데이터 담은 파일을 .config_secret 폴더 안에 만든다.
- .gitignore 파일에 해당 폴더를 추가하여 저장소에서 관리되지 않도록 한다.

```
project_folder/
    .config_secret/
        settings_common.json
        settings_debug.json
        settings_deploy.json
    django_app/
        config/
            settings/
              __init__.py
              base.py
              debug.py
              deploy.py
            wsgi
              __init__.py
              debug.py
              deploy.py
            __init__py
            urls.py
        manage.py  
    ..
```

### settings_common.json 예시

```json
{
  "django": {
    "secret_key": "Django project secret key"
  }
}
```

### settings_debug.json 예시

```json
{
  "django": {
    "allowed_hosts": [
      "localhost",
      "127.0.0.1",
      ".compute.amazonaws.com"
    ]
  }
}
```

### settings_deploy.json 예시

```json
{
  "django": {
    "allowed_hosts": [
      ".compute.amazonaws.com"
    ]
  }
}
```

## settings.py에서 json 데이터 참조하기
- 참고 : [settings.py 의 SECRET_KEY 변경 및 분리하기](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)

### base.py 예시
```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

# .config_secret 폴더 및 하위 파일 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']
```

### debug.py 예시

```python
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'
```

### deploy.py 예시
```python
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'
```

---

# wsgi 분리하기
- uwsgi 명령을 통해서 직접 웹어플리케이션 서버를 실행할때 사용할 설정 파일을 실행환경별로 분리한다.
  (실행 환경별로 필요한 프로젝트 설정이 다르기 때문)
  - base.py (공통)
  - debug.py (개발용)
  - deploy.py (배포용)

## 설정파일 구성

```
project_folder/
    .config_secret/
        settings_common.json
        settings_debug.json
        settings_deploy.json
    django_app/
        config/
            settings/
              __init__.py
              base.py
              debug.py
              deploy.py
            wsgi
              __init__.py
              debug.py
              deploy.py
            __init__py
            urls.py
        manage.py  
    ..
```

### wsgi/debug.py 예시
```python

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.debug")

application = get_wsgi_application()

```

### wsgi/deploy.py 예시
```python

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.deploy")

application = get_wsgi_application()

```

---

# runserver
- 장고는 DJANGO_SETTINGS_MODULE 환경변수를 통해서 참고할 settings 파일의 경로를 확인한다.
- 환경변수가 설정되지 않으면 [wsgi.py](https://github.com/django/django/blob/1.10.6/django/conf/project_template/project_name/wsgi.py-tpl) 의 설정값을 사용
- 혹은 `python3 manage.py runserver` 시에 `--settings` 옵션을 통해서 지정 가능

```commandline
# local development
python3 manage.py runserver --settings=config.settings.debug

# 환경변수 설정예시
export DJANGO_SETTINGS_MODULE=config.settings.debug
echo $DJANGO_SETTINGS_MODULE
```

## 참고
- [Django settings](https://docs.djangoproject.com/en/1.11/topics/settings/)
- [How to deploy with WSGI](https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/)
- [Open Menu
Django settings.py 환경을 여러 개의 설정 파일로 분리하여 사용하기](https://cjh5414.github.io/django-settings-separate/)
