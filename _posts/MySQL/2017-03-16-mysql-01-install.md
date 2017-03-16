---
layout: post
title: MySQL 01. MySQL 설치 및 환경설정
category: Django
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    


# 데이터베이스와 MYSQL
- 데이터베이스란 : 데이터의 저장소

## 데이터베이스의 종류
- 관계형 데이터베이스
  - mysql, oracle, mssql
- nosql
  - mongodb 등

## 데이터베이스 시스템의 구성

<center>
 <figure>
 <img src="/assets/post-img/mysql/db.png" alt="views">
 <figcaption></figcaption>
 </figure>
 </center>

### Database Server
- DB 서버 안에 데이터를 저장하고, 저장된 데이터를 수정하거나 삭제하는 등의 제어 관리 기능을 갖고 있는 것

### Database
- Table을 카테고리로 분류한것   

### table
- row(행) : 서로 연관되어 있는 데이터의 세트
- column(열) : 데이터의 성격에 대한 구분
- field : 한칸 한칸에 들어가 있는 구체적인 데이터
- record : 행의 구체적인 데이터   

### Database Client
- DB 서버에게 요청해서 여러가지 명령을 하거나, 데이터를 가져온다거나 서버의 상태를 체크하기 위한 시스템
- mysql-client 는 mysql을 설치하면 기본적으로 설치된다.

## MySQL 설치
