---
layout: post
title: Django 기본 05 - Migration
category: Django
tags: [python, Django, Migration]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# migrations

- [가이드문서](https://docs.djangoproject.com/en/1.10/topics/migrations/)
- 모델 변경내역 히스토리 관리
- 모델의 변경내역을 DB Schema (데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공
- migration 옵션을 끌수도 있다.

## 관련 명령어

```shell
# 마이그레이션 파일 생성
$ python manage.py makemigrations <app-name>

# 마이그레이션 적용
$ python manage.py migrate <app-name>

# 마이그레이션 적용 현황
$ python manage.py showmigrations <app-name>

# 지정 마이그레이션의 SQL 내역
 python manage.py sqlmigrate <app-name> <migration-name>
```

## 마이그레이션 파일 생성 및 적용
1. 마이그레이션 파일 (초안) 생성하기 : `makemigrations`
2. 해당 마이그레이션 파일을 DB에 반영하기 : `migrate`

<center>
 <figure>
 <img src="/assets/post-img/django/migration.png" alt="views">
 <figcaption>마이그레이션 절차 및 주의사항</figcaption>
 </figure>
 </center>

### tip
- makemigrations 이후에는 migration 폴더를 확인하는 습관을 갖는게 좋다. DB는 중요하기 때문에 무엇이 수정되었는지 다시 한번 확인하는 습관.
-  makemigrations [app-name] 처럼 app 이름을 명시하는 것이 좋다. (예상치 못한 migration을 방지)
- showmigrations 를 통해서 적용 상태를 조회할 수 있다. [x] : 적용 후 []: 적용 전
- 실제 DB에는 sql 쿼리로 명령이 전달이 된다. migration 파일은 쿼리는 아니다. 따라서 `sqlmigrate` 명령을 통해 sql로도 확인하는 습관이 필요하다.  
- 이미 적용한 migration 파일은 절대로 지우면 안된다.
- 프로젝트/앱 생성 후 처음 migrate 할 때는 app 이름을 명시하지 않는다. 이는 장고 기본 앱에, 여러 앱에 걸쳐서 적용할 migrate가 있기 때문이다.
- no such table, column 등의 오류는 migration 관련 문제이다.

## 마이그레이션 migrate 롤백 (Forward/Backward)
### 일반적인 migrate
```shell
$ python manage.py migrate <app-name>
```
- 미적용 마이그레이션 파일 부터 최근 마이그레이션 파일까지 `Forward 마이그레이션`을 순차적으로 수행한다.

### 특정 파일지정을 통한 migrate

```shell
$ python manage.py migrate <app-name> <마이그레이션 파일명>
```
- 지정한 마이그레이션 파일이 현재 적용된 마이그레이션 파일 보다
  - 이후라면, `Forward 마이그레이션` 을 순차적으로 진행
  - 이전이라면, `Backward 마이그레이션` 을 순차적으로 진행 (`롤백`)

## 마이그레이션 파일명 지정
- 전체 파일명을 지정하지 않더라도, 판독이 가능하다면 파일명 일부로도 지정이 가능하다.
- 롤백 후에 돌아오면 `테이블의 데이터 레코드가 사라진다`. 장고 모델의 migration은 스키마의 형상관리로, 데이터 백업을 지원하지 않는다. 따라서 `주기적인 백업`이 필요하다.

```shell
# 파일명 예시
blog/migrations/0001_initial.py
blog/migrations/0002_create_field.py
blog/migrations/0002_update_field.py

python manage.py migrate blog 0001 # OK
python manage.py migrate blog 0002 # FAIL (다수 파일 해당)
```
## 브라우저를 통한 SQLite 확인
- [SQLiteBrowser](http://sqlitebrowser.org/)
- 생성한 DB 내역을 GUI 환경에서 확인 (SQLite 사용시 가능)
- 데이터베이스 열기 메뉴를 통해서 프로젝트 폴더 내의 sqlite3.db 파일 열기

## id 필드
- 모든 데이터베이스 테이블에는 각 Row의 식별 기준인 기본키(Primary Key) 가 필요
- Django에는 기본키로 id(AutoField)가 디폴트로 지정되어 있음 (AutoField : 1부터 시작해서 값이 1씩 증가하는 것)
- 기본키는 줄여서 pk로도 접근 가능 (primary key)

## 기존 모델 클래스에 필수 필드 추가
- 필드옵션 blank, null의 디폴트 값은 False이다. 따라서 기본적으로 모든 필드는 필수 필드이다.
- 만약 새로운 필수 필드를 추가해서 makemigrations를 수행하면, 기존에 있는 레코드에 대해서 어떤 값을 채워 넣을지 설정해야한다.
  - 선택 1 : 지금 값을 입력
  - 선택 2 : 모델 클래스를 수정하여 디폴트 값을 제공
