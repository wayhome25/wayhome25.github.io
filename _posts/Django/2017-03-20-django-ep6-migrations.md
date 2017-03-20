---
layout: post
title: Django 기본 05 - Migration
category: Django
tags: [python, Django, Migration]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

```shell
1.7 버전 이전에는 syncdb 커맨드 사용
- 테이블에 변경이 발생하면 반영하는 기능이 없다. 최초 생성만
- migration 명령은 모델의 내용이 변경되면, DB에 반영한다.
- migration 옵션을 끌수도 있다.
- makemigrations 이후에는 migration 폴더를 확인하는 습관을 갖는게 좋다.
- makemigrations [app-name] 처럼 app 이름을 명시하는 것이 좋다. (예상치 못한 migration을 방지)
- showmigrations 를 통해서 적용 상태를 조회할 수 있다.
- 이미 적용한 migration 파일은 절대로 지우면 안된다.
- 프로젝트/앱 생성 후 처음 migrate 할 때는 app 이름을 명시하지 않는다. 이는 장고 기본 앱에, 여러 앱에 걸쳐서 적용할 migrate가 있기 때문이다.
- no such table, column 등의 오류는 migration 관련 문제이다.
- sqlmigrate : 실제 DB에는 sql 쿼리로 명령이 전달이 된다. migration 파일은 쿼리는 아니다. 따라서 sql로도 확인하는 습관이 필요하다.  
- settings.py 의 DATABASES 항목을 통해 하나의 장고 프로젝트에 여러개의 DB 설정이 가능하다.
- sqlbrowser을 통해서 sqlite3
- 롤백 후에 돌아오면 테이블의 데이터 레코드가 사라진다. 장고 모델의 migration은 스키마의 형상관리로, 데이터 백업을 지원하지 않는다. 따라서 주기적인 백업이 필요하다.
- blank 필드옵션의 디폴트는 False, null 필드옵션의 디폴트는 False이다. 기본적으로 모든 필드는 필수 필드이다.
- 새로운 필수 필드를 추가해서 makemigrations 을 실행하면, 기존에 있는 레코드에 대해서 어떤 값을 채워 넣을지 설정해야한다. 

```
