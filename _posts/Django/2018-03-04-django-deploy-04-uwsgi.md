---
layout: post
title: Django 배포연습 4 - uwsgi 를 통한 Django 실행
category: Django
tags: [django, deploy, uwsgi]
comments: false
---

> nginx, uwsgi, docker를 활용한 배포 연습 과정을 기록한 글입니다.   
> 개인 공부 후 자료를 남기기 위한 목점임으로 내용상에 오류가 있을 수 있습니다.
>
> - nginx, uwsgi를 통해서 아마존 EC2에서 장고 앱 어플리케이션을 실행시켜 보는 것을 목표로 한다.
> - 최소한의 설정만을 포함한다.



# uWSGI 실행 옵션

### 웹 서버 관리용 유저 생성

```
> sudo adduser deploy-user
```

### uWSGI 설치

```
(virtualenv 환경 내부에서)
> pip install uwsgi
```

## uwsgi 실행 옵션에 대한 설명

```
uwsgi 1)--http 2):8000 3)--home (virtualenv경로) 4)--chdir (django프로젝트 경로) 5)-w (프로젝트명).wsgi
```

##### 1) uwsgi를 실행하는데 http로 오는 요청을 받겠다.   
nginx <-> wsgi 통신은 기본적으로 socket 방식을 사용한다.
HTTP 방식을 사용할 수 있지만 통신에서 로스가 많이 발생하는 단점이 있다.
그에 비해서 wsgi app은 서버 안쪽에서 서버의 요청을 django 어플리케이션에 중계하는 역할을 하기 때문에
무거운 HTTP 요청을 보다는 socket이라는 전송방식을 사용한다. (HTTP에 비해서 훨씬 가볍게 설정이 가능)

##### 2) 8000 포트번호로 오는 요청을 받겠다.   

##### 3) uwsgi가 돌아갈 파이썬 환경 홈    
uwsgi 자체가 파이썬 인터페이스이기 때문에 어떤 파이썬 환경에서 사용할지에 대한 경로가 필요함

##### 4) uwsgi가 요청을 받고 실행할 파이썬 어플리케이션의 경로로 이동 (change directory)    
manage.py가 있는 source root 폴더를 지정해야함

##### 5) 실행시 어떤 wsgi 설정 파일을 갖고 실행할지를 지정    
chdir 옵션을 통해서 이동한 장고 프로젝트 경로안에서 package 모듈 이름으로 찾는다   
(config/wsgi가 아닌 config.wsgi)


### uwsgi 실행 예시 (ubuntu 서버에서)

- ex) pyenv virtualenv이름이 mysite-env, django프로젝트가 /srv/mysite/django_app, 프로젝트명이 mysite일 경우
- 실행 후 <ec2도메인>:8000으로 접속하여 요청을 잘 받는지 확인

```
uwsgi --http :8000 --home ~/.pyenv/versions/mysite-env --chdir /srv/mysite/django_app -w mysite.wsgi
```

### uwsgi 실행 예시 (로컬에서)

- uwsgi는 로컬에서도 동일하게 실행 가능
- 단 wsgi.py 파일에서 settings가 debug를 바라보도록 수정 필요 (ALLOWED_HOSTS에 localhost포함)
- 로컬에서는 debug, 서버에서는 deploy settings를 바라보도록 하려면 wsgi.py 파일을 settings 처럼 분리하는것이 좋음


```
uwsgi --http :8000 --home /usr/local/var/pyenv/versions/deploy_ec2 --chdir /Users/Dev/deploy_ec2/django_app -w config.wsgi
```

----

# uWSGI 설정분리 및 실행

### wsgi 파일 분리하기
- wsgi 파일을 debug/deploy로 분리하여 uwsgi 실행시에 실행환경에 맞는 settings를 바라보도록 조절한다.

```shell
├── django_app
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── debug.py
│   │   │   └── deploy.py
│   │   ├── urls.py
│   │   ├── wsgi.py  # runserver용 wsgi 파일
│   │   └── wsgi  # uwsgi용 wsgi 파일
│   │       ├── __init__.py
│   │       ├── debug.py
│   │       └── deploy.py
│   ├── db.sqlite3
│   └── manage.py
```
- wsgi.py 예시 (runserver시에 사용)

```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.debug")

application = get_wsgi_application()

```

- wsgi 분기 예시 (uwsgi 실행시 사용)

```python
from django.core.wsgi import get_wsgi_application

# wsgi/debug.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.debug")

application = get_wsgi_application()

# wsgi/deploy.py

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.deploy")

application = get_wsgi_application()
```

## 로컬에서 uwsgi 실행

#### uWSGI debug용 설정 파일 작성 예시
- 위의 예시와 같이 uwsgi 실행시 모든 옵션을 적어야한다면 번거롭기 때문에 설정파일을 따로 생성한다.
- 참고로 ini 파일에서는 ~/ (home폴더) 사용이 불가능하기 때문에 절대경로 입력이 필요하다.

```ini
[uwsgi]
home = /usr/local/var/pyenv/versions/deploy_ec2
chdir = /Users/Dev/deploy_ec2/django_app
module = config.wsgi.debug
http = :8000
```

#### uwsgi 실행
- 로컬 컴퓨터에서 실행후 localhost:8000 으로 접속 확인

```shell
uwsgi -i .config_secret/uwsgi/debug.ini
```

## ubuntu에서 uwsgi 실행

#### uWSGI deploy용 설정 파일 작성 에시
- linux 서버 정보를 기준으로 작성해야 한다.
- 파일경로 예시 : /srv/deploy_ec2/.config_secret/uwsgi/deploy.ini

```ini
[uwsgi]

# Django-related settings
# the base directory (full path)
chdir = /srv/deploy_ec2/django_app       
# Django's wsgi file
module = config.wsgi.deploy              
# the virtualenv (full path)
home = /home/ubuntu/.pyenv/versions/deploy_ec2 ; VirtualEnv location

uid = deploy-user       ; adduser 명령을 통해서 추가한 웹서버 관리용 유저
gid = deploy-user       ; group id

# the socket (use the full path to be safe
socket = /tmp/ec2.sock  ; 상기 유저가 해당 tmp 폴더에 대해서 모든 권한을 가져아함
chmod-socket = 666      ; 소켓 소유 권한 (읽고, 쓰기)
chown-socket = deploy-user:deploy-user ;소켓 소유자 adduser 명령을 통해서 추가한 유저 정보 (uid:gid)

# process-related settings
# master
master = true
enable-threads = true
pidfile = /tmp/ec2.pid

vacuum = true                  ;ec2.pid, ec2.sock 파일 자동삭제 (uwsgi 종료시)
logger = file:/tmp/uwsgi.log   ;log 경로
```

#### 폴더 권한 변경
- /tmp 폴더의 권한을 adduser를 통해서 추가한 deploy-user로 변경

```python
sudo chown -R deploy-user:deploy-user /tmp
```

#### uwsgi 실행
- /tmp/mysite.pid, /tmp/mysite.sock 파일을 생성하고 요청을 받을 준비완료

```shell
> sudo -u deploy-user /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi -i /srv/deploy_ec2/.config_secret/uwsgi/deploy.ini
```

- --http 옵션을 추가하면 <AWS DNS>:8000으로 접근 가능

```shell
> sudo -u deploy-user /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --http :8000 -ini /srv/deploy_ec2/.config_secret/uwsgi/deploy.ini
```

------

# 서버 접속시 uWSGI 자동 실행

### uWSGI 서비스 설정파일 작성
- [Systemd](http://uwsgi-docs.readthedocs.io/en/latest/Systemd.html)
- [How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units#service-management)
- 작성 파일 경로 : /etc/systemd/system/uwsgi.service

```
sudo vi /etc/systemd/system/uwsgi.service

[Unit]
Description=uWSGI Emperor service
After=syslog.target

[Service]
ExecPre=/bin/sh -c 'mkdir -p /run/uwsgi; chown deploy-user:deploy-user /run/uwsgi'
ExecStart=/home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --uid deploy_user --gid deploy_user --master --emperor /etc/uwsgi/sites

Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

### 리부팅 시 자동으로 실행되도록 설정
- 실행 실패시 에러로그는 /var/log/syslog에서 확인할 수 있다.

```shell
# 실행
> sudo systemctl start uwsgi.service
> sudo systemctl enable uwsgi
# 상태확인
> systemctl status uwsgi

● uwsgi.service - uWSGI Emperor service
   Loaded: loaded (/etc/systemd/system/uwsgi.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2018-03-04 09:51:25 UTC; 1min 10s ago
 Main PID: 6546 (uwsgi)
   Status: "The Emperor is governing 0 vassals"
   CGroup: /system.slice/uwsgi.service
           ├─6546 /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --uid deploy-user --gid deploy-user --master --emperor /etc/uwsgi/sites
           └─6547 /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --uid deploy-user --gid deploy-user --master --emperor /etc/uwsgi/sites

```

### 참고
- [Setting up Django and your web server with uWSGI and nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
- [Systemd](http://uwsgi-docs.readthedocs.io/en/latest/Systemd.html)
- [How To Use Systemctl to Manage Systemd Services and - Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units#service-management)
- [생활코딩-항상실행(daemon, service)](https://opentutorials.org/course/2598/14217)
