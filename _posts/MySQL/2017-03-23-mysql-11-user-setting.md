---
layout: post
title: MySQL 07. MySQL - 사용자 관리, 권한
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

```shell
- ALTER : 테이블의 스키마 변경
- 테이블 안의 데이터를 제어 / 테이블 자체를 설계하는 역할에 따른 권한 부여
- DBA : DataBase Administrator DB 관리자  
- 예제 :
  - 누구 : dev라는 id를 가진 이용자, 접속 ip와 상관 없음
  - 무엇 : class 데이터베이스의 모든 테이블의
  - 어떻게 : 테이블의 행을 삭제, 추가, 조회, 업데이트하는 권한만 부여하겠다.
```

```shell
# 권한이 없을 때 예시
mysql> CREATE DATABASE `test` CHARACTER SET utf8 COLLATE utf8_general_ci;
ERROR 1044 (42000): Access denied for user 'dev'@'%' to database 'test'
```
