---
layout: post
title: MySQL 06. MySQL - Table (조회4 index, where)
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL ](https://opentutorials.org/course/195)    

# index
- 색인, 조회할 때 원하는 행을 빠르게 찾을 수 있게 준비해둔 데이터
- 데이터베이스의 성능이 중요한 경우 인덱스 설계가 중요하다.

## 인덱스 정의 방법
- 자주 조회되는 칼럼에 적용
- 조회 시 오랜시간을 소모하는 컬럼에 적용
- 데이터가 긴 경우 인덱스를 사용하지 않는다.

## 인덱스의 종류
- primary key: 중복되지 않는 유일한 키
- unique key : 중복을 허용하지 않는 유일한 키
- normal key : 중복을 허용하는 인덱스
- foreign key : 다른 테이블과의 관계성을 부여하는 키
- full text : 자연어 검색, myisam에서만 지원


## 예제에서 사용한 테이블

```shell
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `name` char(4) NOT NULL,
  `address` varchar(50) NOT NULL,
  `department` enum('국문과','영문과','컴퓨터공학과','전자공학과','물리학과') NOT NULL,
  `introduction` text NOT NULL,
  `number` char(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_number` (`number`) USING BTREE,
  KEY `idx_department` (`department`),
  KEY `idx_department_name` (`department`,`address`),
  FULLTEXT KEY `idx_introduction` (`introduction`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

INSERT INTO `student` VALUES (1, '이숙경', '청주', '컴퓨터공학과', '저는 컴퓨터 공학과에 다닙니다. computer', '0212031');
INSERT INTO `student` VALUES (2, '박재숙', '서울', '영문과', '저는 영문과에 다닙니다.', '0512321');
INSERT INTO `student` VALUES (3, '백태호', '경주', '컴퓨터공학과', '저는 컴퓨터 공학과에 다니고 경주에서 왔습니다.', '0913134');
INSERT INTO `student` VALUES (4, '김경훈', '제천', '국문과', '제천이 고향이고 국문과에 다닙니다.', '9813413');
INSERT INTO `student` VALUES (6, '김경진', '제주', '국문과', '이번에 국문과에 입학한 김경진이라고 합니다. 제주에서 왔어요.', '0534543');
INSERT INTO `student` VALUES (7, '박경호', '제주', '국문과', '박경호입니다. 잘 부탁드립니다.', '0134511');
INSERT INTO `student` VALUES (8, '김정인', '대전', '영문과', '김정인입니다. 대전에서 왔고, 영문과에 다닙니다.', '0034543');
```
## primary key
- 테이블 전체를 통틀어서 중복되지 않는 값을 지정해야 한다.
- where 문을 이용해서 데이터를 조회할 때 가장 `고속`으로 데이터를 가져올 수 있다.
- 테이블마다 딱 하나의 primary key를 가질 수 있다.

```shell
# 설정
PRIMARY KEY (`id`)

# 예시
SELECT * FROM student WHERE id=3;
```

## unique key
- 테이블 전체를 통틀어서 중복되지 않는 값을 지정해야 한다. (== primary key)
- 고속으로 데이터를 가져올 수 있다.
- 여러개의 unique key를 지정할 수 있다.

```shell
# 설정
UNIQUE KEY `idx_number` (`number`) USING BTREE

# 예시
SELECT * FROM student WHERE number=0534543;
```

## normal key, 중복키
- 중복을 허용한다.
- primary, unique 보다 속도가 느리다.
- 여러개의 키를 지정할 수 있다.

```shell
# 설정
KEY `idx_department` (`department`),
KEY `idx_department_name` (`department`,`address`)

# 예시
SELECT * FROM student WHERE department='국문과';
SELECT * FROM student WHERE department='국문과' AND address='제주';
```

## Full Text
- mysql의 기본설정(ft_min_word_len)이 4로 되어 있기 때문에 최소 4글자 이상을 입력하거나 이 값을 조정해야 한다.
- mysql은 전문 검색 엔진이 아니기 때문에 한글 검색이 잘 안된다.
- 전문검색엔진으로 lucene, sphinx 참고 (무료, 성능 좋음)
- 스토리지 엔진 중 myisam에서만 사용가능

```shell
# 설정
ENGINE=MyISAM

# 예시
SELECT introduction, MATCH(introduction) AGAINST('영문과에') FROM student WHERE MATCH (introduction) AGAINST('영문과에');
```
