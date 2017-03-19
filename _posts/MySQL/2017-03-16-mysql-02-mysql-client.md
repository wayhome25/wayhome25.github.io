---
layout: post
title: MySQL 02. MySQL Client - mysql monitor 기본
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

# mysql client 종류
 mysql-monitor
  - mysql을 설치하면 기본적으로 설치되는 프로그램
  - mysql -u아이디 -p비밀번호
- [mysql query browser](http://dev.mysql.com/downloads/gui-tools/5.0.html)
  - GUI 환경 제공
- [phpMyAdmin](http://www.phpmyadmin.net/home_page/index.php)
  - 서버에 직접 설치하는 웹프로그램으로, 웹으로 제공되는 서비스이기 때문에 어디서든지 웹환경에서 DB를 제어할 수 있다.
- navicat
  - 기능이 많고 안정적이다. 유료

# mysql monitor 사용법

## mysql monitor
- mysql 서버의 번들로 제공되는 기본 프로그램 (mysql client)
- 명령어 기반
- mysql 관련된 거의 모든 기능을 사용할 수 있고, mysql이 있는 곳에 함께 기본으로 설치되어 있다.

## 사용법
- mysql -u아이디 -p비밀번호
- mysql -h호스트주소 -p포트번호 -u아이디 -p비밀번호

## 데이터베이스 생성 및 조회

mysql > `CREATE DATABASE` music `CHARACTER SET` utf8 `COLLATE` utf8_general_ci;
mysql > show databases

## 데이터베이스 선택

mysql > `use` music

## 테이블 생성 및 조회

```shell
CREATE TABLE `favorite_music` (
  `title` varchar(255) NOT NULL,
  `musician` varchar(20) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `album` varchar(30) NOT NULL
) ENGINE=innodb;
```

mysql> `show tables;`

## 테이블에 데이터 추가

```shell
insert into favorite_music (`title`,`musician`, `duration`, `album`) values('Chasing Pavements', '아델', '3:30', 19);

```

## 입력된 데이터 조회

`select` * `from` favorite_music;

## 종료

mysql> `exit;`
