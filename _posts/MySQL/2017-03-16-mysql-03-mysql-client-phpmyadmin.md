---
layout: post
title: MySQL 03. MySQL - DB생성, phpmyadmin
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

## SQL
- Structured Query Language
- 데이터베이스에서 데이터를 저장하거나 얻기 위해서 사용하는 **표준화된** 언어.

### Database
- 데이터가 실질적으로 적재되는 테이블들을 분류하는 상위 개념

### 생성

```shell
CREATE DATABASE `데이터베이스명` CHARACTER SET utf8 COLLATE utf8_general_ci;
```
### 삭제

```shell
DROP DATABASE `데이터베이스명`;
```
### 열람

```shell
SHOW DATABASE;
```

### 선택

```shell
USE `데이터베이스명`;
```


## phpmyadmin
- 웹 환경에서 DB를 제어할 수 있는 mysql client

### 실행방법
- Bitnami 설치 - [참고자료](https://opentutorials.org/course/1688/9338)
- Bitnami 실행 후 MySQL, Apache Web Server 구동
- http://localhost:8080/phpmyadmin/ 접속 (open phpMyAdmin)
- bitnami 설치시 지정한 암호로 (id : root) 접속


<center>
<figure>
<img src="/assets/post-img/mysql/bitnami.png" alt="views">
<figcaption>bitnami 설치를 통한 내부 웹서버 구동</figcaption>
</figure>
</center>

## 자료  
 - [mysql 한글 메뉴얼](http://www.mysqlkorea.com/sub.html?mcode=manual&scode=01&lang=k)
 - [w3school](https://www.w3schools.com/sql/default.asp)
 - [cheat sheet](http://cse.unl.edu/~sscott/ShowFiles/SQL/CheatSheet/SQLCheatSheet.html)
 - [데이터베이스 사랑넷](http://database.sarang.net/?criteria=mysql)
