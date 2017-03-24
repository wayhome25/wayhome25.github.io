---
layout: post
title: MySQL 05. MySQL - Table (insert, update, delete)
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

# mysql monitor
- CLI 환경인 mysql monitor에서 테이블 데이터를 삽입, 수정, 삭제, 조회 하는 방법을 살펴본다.
- GUI 환경인 phpMyAdmin에서 쉽게 동일한 작업이 가능하다.

## 삽입
- 테이블에 데이터를 삽입한다.  
- `insert into` 명령어를 사용

```shell
# 문법
INSERT INTO table_name VALUES (value1, value2, value3,...)
INSERT INTO table_name (column1, column2, column3,...) VALUES (value1, value2, value3,...)

# 예제
INSERT INTO `student` VALUES ('2', 'leezche', '여자', '서울', '2000-10-26');
INSERT INTO `student` (`id`, `name`, `sex`, `address`, `birthday`) VALUES ('1', 'egoing', '남자', 'seoul', '2000-11-16');
```
-----
## 수정
- 테이블에 데이터 변경한다.
- `update ... set` 명령어를 사용

```shell
# 문법
UPDATE 테이블명 SET 컬럼1=컬럼1의 값, 컬럼2=컬럼2의 값 WHERE 대상이 될 컬럼명=컬럼의 값

#예제
UPDATE `student` SET address='서울';
UPDATE `student` SET name='이진경' WHERE id=1;
UPDATE `student` SET name='이고잉', birthday='2001-4-1' WHERE id=3;
```
-----
## 삭제
- 테이블에 데이터를 삭제한다.
- `DELETE FROM`, `TRUNCATE`, `DROP TABLE` 명령어를 사용한다.
### DELETE

```shell
# 문법
DELETE FROM 테이블명 [WHERE 삭제하려는 칼럼 명=값]

# 예제
DELETE FROM student WHERE id = 2;
```

### TRUNCATE
- 테이블의 전체 데이터를 삭제
- 테이블에 외부키(foreign key)가 없다면 DELETE보다 훨씬 빠르게 삭제됨

```shell
# 문법
TRUNCATE 테이블명

# 예제
TRUNCATE student;
```

### DROP TABLE
- 테이블을 삭제한다

```shell
# 문법
DROP TABLE 테이블명;

# 예제
DROP TABLE student;
```

---
