---
layout: post
title: MySQL 06. MySQL - Table (조회5 join)
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    


# 여러개의 테이블 사용하기
- 데이터의 규모가 커지면서 하나의 테이블로 정보를 수용하기가 어려워지면 테이블을 분활하고 테이블 간의 관계성을 부여한다.

## 예제 테이블 1
-  예제 중 address는 distnace와 관련되어 있기 때문에 location이라는 별도의 테이블로 분할 할 수 있다.

```shell
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` tinyint(4) NOT NULL,
  `name` char(4) NOT NULL,
  `sex` enum('남자','여자') NOT NULL,
  `address` varchar(50) NOT NULL,
  `distance` INT NOT NULL,
  `birthday` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `student` VALUES (2, '박재숙', '남자', '서울',  10, '1985-10-26 00:00:00');
INSERT INTO `student` VALUES (1, '이숙경', '여자', '청주', 200, '1982-11-16 00:00:00');
INSERT INTO `student` VALUES (3, '백태호', '남자', '경주', 350, '1989-2-10 00:00:00');
INSERT INTO `student` VALUES (4, '김경훈', '남자', '제천', 190, '1979-11-4 00:00:00');
INSERT INTO `student` VALUES (8, '김정인', '남자', '제주', 400, '1990-10-1 00:00:00');
INSERT INTO `student` VALUES (6, '김경진', '여자', '제주', 400, '1985-1-1 00:00:00');
INSERT INTO `student` VALUES (7, '박경호', '남자', '영동', 310, '1981-2-3 00:00:00');
```

## 예제 테이블 2
- address, distance를 묶어서 별도의 테이블(location)로 만든다.

```shell
# student 테이블
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` tinyint(4) NOT NULL,
  `name` char(4) NOT NULL,
  `sex` enum('남자','여자') NOT NULL,
  `location_id` tinyint(4) NOT NULL,
  `birthday` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# location 테이블
DROP TABLE IF EXISTS `location`;
CREATE TABLE `location` (
`id`  tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,
`name`  varchar(20) NOT NULL ,
`distance`  tinyint UNSIGNED NOT NULL ,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;;
```

```shell
INSERT INTO `location` VALUES (1, '서울', 10);
INSERT INTO `location` VALUES (2, '청주', 200);
INSERT INTO `location` VALUES (3, '경주', 255);
INSERT INTO `location` VALUES (4, '제천', 190);
INSERT INTO `location` VALUES (5, '대전', 200);
INSERT INTO `location` VALUES (6, '제주', 255);
INSERT INTO `location` VALUES (7, '영동', 255);
INSERT INTO `location` VALUES (8, '광주', 255);
```

```shell
INSERT INTO `student` VALUES (1, '이숙경', '여자', 1, '1982-11-16 00:00:00');
INSERT INTO `student` VALUES (2, '박재숙', '남자', 2, '1985-10-26 00:00:00');
INSERT INTO `student` VALUES (3, '백태호', '남자', 3, '1989-2-10 00:00:00');
INSERT INTO `student` VALUES (4, '김경훈', '남자', 4, '1979-11-4 00:00:00');
INSERT INTO `student` VALUES (6, '김경진', '여자', 5, '1985-1-1 00:00:00');
INSERT INTO `student` VALUES (7, '박경호', '남자', 6, '1981-2-3 00:00:00');
INSERT INTO `student` VALUES (8, '김정인', '남자', 5, '1990-10-1 00:00:00');
```

# join
테이블간의 관계성에 따라서 복수의 테이블을 결합, 하나의 테이블인 것 처럼 결과를 출력

## join의 종류
- OUTTER JOIN : 매칭되는 행이 없어도 결과를 가져오고, 매칭되는 행이 없는 경우 NULL로 표시
  - `LEFT JOIN` : 왼쪽에 있는 테이블을 기준으로 오른쪽에 있는 테이블의 데이터를 가져온다.
  - RIGHT JOIN : 오른쪽에 있는 테이블을 기준으로 왼쪽에 있는 테이블의 데이터를 가져온다.
- INNER JOIN : 매칭되는 행이 있는 경우만 표시한다.

## LEFT JOIN
- 가장 많이 사용되는 조인의 형태
- AS : alias 의 약자
- 문법 : 기준 테이블 `AS` 별명 `LEFT JOIN` 결합할 테이블 `AS` 별명 `ON` 결합기준

```shell
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id;
```

## OUTTER JOIN과 INNER JOIN의 차이
- location 테이블에서 제주를 삭제 후 OUTTER JOIN(LEFT JOIN)과 INNER JOIN의 차이를 비교

```shell
# location 테이블에서 제주 레코드 삭제
DELETE FROM location WHERE name='제주';

# LEFT JOIN
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id;

+-----------+--------+---------+----------+
| name      | sex    | address | distance |
+-----------+--------+---------+----------+
| 이숙경      | 여자    | 서울     |       10 |
| 박재숙      | 남자    | 청주     |      200 |
| 백태호      | 남자    | 경주     |      255 |
| 김경훈      | 남자    | 제천     |      190 |
| 김경진      | 여자    | 대전     |      200 |
| 박경호      | 남자    | NULL    |     NULL |
| 김정인      | 남자    | 대전     |      200 |
+-----------+--------+---------+----------+

# INNER JOIN
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s INNER JOIN location AS l ON s.location_id = l.id;

+-----------+--------+---------+----------+
| name      | sex    | address | distance |
+-----------+--------+---------+----------+
| 이숙경      | 여자    | 서울     |       10 |
| 박재숙      | 남자    | 청주     |      200 |
| 백태호      | 남자    | 경주     |      255 |
| 김경훈      | 남자    | 제천     |      190 |
| 김경진      | 여자    | 대전     |      200 |
| 김정인      | 남자    | 대전     |      200 |
+-----------+--------+---------+----------+
```
