---
layout: post
title: MySQL 07. MySQL - 사용자 관리, 권한
category: MySQL
tags: [MySQL, 데이터베이스]
comments: true
---
> [생활코딩 - MySQL](https://opentutorials.org/course/195) 강의를 듣고 중요한 내용을 정리하였습니다.    

# 사용자 권한이란?
- 사용자에 따라서 접근할 수 있는 DB 데이터와 사용할 수 있는 기능을 제한

## GRANT
- 사용자를 생성하고, 권한을 부여 (grant : 승인하다)

```shell
# 문법
GRANT 권한 ON 데이터베이스.테이블 TO '아이디'@'호스트' IDENTIFIED BY '비밀번호'
```
### 사용자의 제한
- DB 서버에 접속하는 사용자를 제한한다.
- 아이디@호스트 중에서 호스트는 접속자가 사용하는 머신의 IP를 의미한다. IP를 특정하지 않으려면 '%'를 사용
  - dev@123.100.100.100 : IP 123.100.100.100인 머신에서 접속한 ID dev
  - dev@% : IP 관계없이 ID가 dev인 사용자

### 대상의 제한
- 사용자가 제어할 대상이 되는 데이터베이스, 테이블을 지정
- `*`를 사용하면 모든 데이터베이스, 테이블을 제어 대상으로 함 (`*.*`,`class.*`)

### 권한(기능)의 제한
- 사용할 수 있는 권한을 제한 (권한은 아래 표 참조 - 상황에 따라 달라진다)

| 개발자 |                               DELETE, INSERT, SELECT, UPDATE                               |
|:------:|:------------------------------------------------------------------------------------------:|
| 설계자 | ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, DELETE, INSERT, SELECT, UPDATE |
|   DBA  |                                             ALL                                            |

### 예제 - GRANT

- ID가 dev, 비밀번호가 1111인 사용자가 class 데이터베이스만 접근하게 하려면 아래와 같이 한다.

```shell
mysql> GRANT DELETE, INSERT, SELECT, UPDATE ON class.* TO `dev`@`%` IDENTIFIED BY '1111';

```

- ID가 archi, 비밀번호가 1111이고 클라이언트의 IP가 100.100.100.100인 사용자가 모든 데이터베이스에 접근하면서 설계자의 권한 템플릿을 이용하게 한다.

```shell
mysql> GRANT ALTER,CREATE,DELETE,DROP,INDEX,INSERT,SELECT,UPDATE ON *.* TO `archi`@`100.100.100.100` IDENTIFIED BY '1111';
```

## SHOW GRANTS
- __자신__ 의 권한이나, 특정 사용자의 권한을 열람한다.

```shell
# 문법
mysql> SHOW GRANTS [FOR 사용자]

#예제
mysql> SHOW GRANTS FOR dev;
+----------------------------------------------------------------+
| Grants for dev@%                                               |
+----------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'dev'@'%'                                |
| GRANT SELECT, INSERT, UPDATE, DELETE ON `class`.* TO 'dev'@'%' |
+----------------------------------------------------------------+

mysql> SHOW GRANTS FOR `archi`@`100.100.100.100`;
+------------------------------------------------------------------------------------------------------+
| Grants for archi@100.100.100.100                                                                     |
+------------------------------------------------------------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON *.* TO 'archi'@'100.100.100.100' |
+------------------------------------------------------------------------------------------------------+
```

## REVOKE
- 사용자의 권한을 제거

```shell
# 문법
REVOKE 권한 ON 데이터베이스.테이블 FROM 사용자

# 예제 : 사용자 dev의 데이터베이스 class의 DELETE 권한을 제거
revoke DELETE on class.* from dev;
```

## DROP USER
-  사용자를 삭제

```shell
# 문법
DROP USER user [, user] ...

# 예제
DROP USER `dev`@`%`;
```

## 권한 테이블
- [참고](https://opentutorials.org/course/195/1406)
<center>
 <figure>
 <img src="/assets/post-img/mysql/user_privileges.png" alt="views">
 <figcaption>DB 권한종류</figcaption>
 </figure>
 </center>

## phpMyAdmin
- mysql 클라이언트 phpMyAdmin을 통하여 위와 동일한 사용자 권한 관리가 가능하다.
- 클라이언트를 사용하면 사용자 관리를 편리하고, 정확하게 진행할 수 있기 때문에 가급적이면 phpMyAdmin과 같은 클라이언트를 사용하는 것을 권장한다.
