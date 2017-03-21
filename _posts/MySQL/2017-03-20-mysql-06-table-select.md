---
layout: post
title: MySQL 06. MySQL - Table (조회1 select, limit, where)
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

# mysql monitor
- CLI 환경인 mysql monitor에서 테이블 데이터를 조회 하는 방법을 살펴본다.
- GUI 환경인 phpMyAdmin에서 쉽게 동일한 작업이 가능하다.


## 조회
- 테이블에서 데이터를 조회

```shell
# 문법
# 중복 사용시 순서가 중요하다.
SELECT 칼럼명1, 칼럼명2
      [FROM 테이블명 ] # 생략가능
      [GROUP BY 칼럼명] # 생략가능
      [ORDER BY 칼럼명 [ASC | DESC]] # 생략가능
      [LIMIT offset, 조회 할 행의 수] # 생략가능
```

```shell
# 예시
SELECT * FROM student;
SELECT name, birthday FROM student;
SELECT * FROM student WHERE id=3;
SELECT * FROM student WHERE sex='남자' AND address='서울';
SELECT * FROM student WHERE sex='여자' OR address='서울';
SELECT * FROM student LIMIT 1; # 1개만
SELECT * FROM student LIMIT 1,1; # index 1번부터 1개만
SELECT * FROM student WHERE sex='남자' LIMIT 2; # 남자 중에 2개만
```
