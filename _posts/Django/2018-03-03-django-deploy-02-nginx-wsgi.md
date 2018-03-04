---
layout: post
title: Django 배포연습 2 - nginx, wsgi 개념
category: Django
tags: [django, deploy, nginx, wsgi]
comments: false
---

> nginx, uwsgi, docker를 활용한 배포 연습 과정을 기록한 글입니다.   
> 개인 공부후 자료를 남기기 위한 목점임으로 내용상에 오류가 있을 수 있습니다.
>
> - nginx, uwsgi를 통해서 아마존 EC2에서 장고 앱 어플리케이션을 실행시켜 보는 것을 목표로 한다.
> - 최소한의 설정만을 포함한다.


![toy architecture](https://i.imgur.com/H9JNiKu.png)

#### 1. 클라이언트
웹서버(Nginx)로 HTTP 요청

#### 2. 웹서버(Nginx)
웹 서버. 클라이언트로부터의 HTTP요청을 받아 정적인 페이지/파일을 돌려준다. (동적인 부분은 uWSGI가 담당)
가벼움과 높은 성능을 목표로 한다. 웹 서버, 리버스 프록시 및 메일 프록시 기능을 가진다.


#### 3. Unix Socket
웹서버(Nginx) - 웹어플리케이션서버(uWSGI) 사이의 통신을 매개
HTTP 요청을 사용할 수도 있지만 서버 안쪽에서의 통신이기 때문에 socket 방식이 overhead가 적어서 더 효율이 좋음

#### 4. 웹어플리케이션서버(uWSGI)
웹 서버(Nginx)와 웹 애플리케이션(Django)간의 연결을 중계
(Nginx에서 받은 요청을 Django에서 처리하기 위한 중계인 역할을 해준다)
Nginx는 Python을 모르기 때문에 uWSGI는 HTTP 요청을 python으로,
Django로 부터 받은 응답을 Nginx가 알 수 있도록 변환해준다.

#### 5. Django
웹 애플리케이션. 웹 요청에 대해 동적데이터를 돌려준다.

#### WSGI
Web Server Gateway Interface  
파이썬에서 웹 서버와 웹 애플리케이션간의 동작을 중계해주는 인터페이스 표준
웹클라이언트의 HTTP 프로토콜 요청을 Python Call로 변환하기 위한 매핑관계로 WSGI를 표준으로 사용
uWSGI는 WSGI 표준의 구현 ([Wikipedia](https://ko.wikipedia.org/wiki/%EC%9B%B9_%EC%84%9C%EB%B2%84_%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4))


## 참고
- [AWS EC2 인스턴스에 Django+Nginx+uWSGI+PostgreSQL로 배포하기](http://technerd.tistory.com/55)
- [Python WSGI server와 관련된 공부](http://software-engineer.gatsbylee.com/w-htm/)
