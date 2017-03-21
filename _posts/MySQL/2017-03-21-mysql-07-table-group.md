---
layout: post
title: MySQL 06. MySQL - Table (조회2 그룹핑 group by)
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

# 그룹핑 (group by)
- 특정 칼럼을 기준으로 데이터를 그룹핑한다.
- 그룹이라고 하는 것은 여러개의 데이터가 어떻게 구성되어 있는지 원자화 시키는 것이다.  
- 각각의 그룹핑된 컬럼을 기준으로 특정한 다른 컬럼의 합계, 평균 등의 작업도 가능하다.

## 문법

```shell
SELECT * FROM 테이블명 GROUP BY 그룹핑 할 기준 칼럼명
```


## 예제
### 대상 테이블

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
INSERT INTO `student` VALUES (8, '김정인', '남자', '대전', 200, '1990-10-1 00:00:00');
INSERT INTO `student` VALUES (6, '김경진', '여자', '제주', 400, '1985-1-1 00:00:00');
INSERT INTO `student` VALUES (7, '박경호', '남자', '영동', 310, '1981-2-3 00:00:00');
```

### 그룹핑 group by 예시

```shell
select sex from student group by sex;
# 결과값
+--------+
| sex    |
+--------+
| 남자    |
| 여자    |
+--------+

select sex,sum(distance), avg(distance) from student group by sex;
# 결과값
+--------+---------------+---------------+
| sex    | sum(distance) | avg(distance) |
+--------+---------------+---------------+
| 남자    |          1060 |      212.0000 |
| 여자    |           600 |      300.0000 |
+--------+---------------+---------------+

```
