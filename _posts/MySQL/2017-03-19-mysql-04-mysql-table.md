---
layout: post
title: MySQL 04. MySQL - Table (create, 필드타입)
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

# Table
- 데이터가 실질적으로 저장되는 저장소

## 스키마(schema)
- 테이블에 적재될 데이터의 구조와 형식을 정의 하는 것

-----
# 테이블 관리 - mysql monitor
- phpMyAdmin를 통해서도 같은 작업을 수행 할 수 있다.
- 초심자는 GUI환경에서 먼저 연습하고 sql문에 점점 익숙해지는 편이 좋다.

## 테이블 생성
- GUI 환경에서 테이블을 생성하는 경우가 많음

```shell
CREATE TABLE table_name (
    칼럼명1 data_type,
    칼럼명2 data_type
)
```

```shell
CREATE TABLE `student` (
    `id`  tinyint NOT NULL ,
    `name`  char(4) NOT NULL ,
    `sex`  enum('남자','여자') NOT NULL ,
    `address`  varchar(50) NOT NULL ,
    `birthday`  datetime NOT NULL ,
    PRIMARY KEY (`id`)
);
```

## 테이블 리스트

```shell
SHOW tables;
```

## 테이블 스키마 열람

```shell
DESC `테이블명`
```

## 테이블 제거

```shell
DROP TABLE `테이블명`
```

## 데이터 타입

| type | 설명     | 기타 |
| :------------- | :------------- | :------------- |
| **문자** | | |
| CHAR( )       | 0 to 255 고정문자 길이|용량고정, 검색에 유리 |
| VARCHAR( )       | 	0~65535 가변 문자 길이 | 용량 절약에 유리, 글 제목|
| TINYTEXT       | 	최대 255 문자길이 | |
| TEXT       | 	최대 65535 문자길이 | 글 본문 |
| **숫자** | | |
| TINYINT( ) | -128 ~ 127 정수형, 0 ~ 255 정수형, UNSIGNED | |
| INT( ) | -2147483648 ~ 2147483647 정수형| |
| FLOAT	 |작은 부동소수점 | 10.35  |
| **날짜** | | |
| DATE | YYYY-MM-DD | |
| DATETIME | YYYY-MM-DD HH:MM:SS | |
| TIME |HH:MM:SS | |
| **기타** | | |
| ENUM ( ) | 정해진 값을 강제| ENUM ('여자', '남자' )|
