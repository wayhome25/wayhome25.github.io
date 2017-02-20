---
layout: post
title: nodejs 서버연결 및 인터넷의 동작 방법 2-2
category: nodejs
tags: [nodejs]
comments: true
---

# 인터넷의 동작 방법
> **서버, 클라이언트, ip, port** 의 개념에 대해서 이해한다.

## 용어 정의
- 클라이언트
  - 웹브라우저가 설치되어 있는 컴퓨터, a.com 주소를 쳐서 정보를 요청한다.
- 서버
  - a.com 에 해당하는 서버는 요청한 정보를 클라이언트에게 정보를 응답한다.
- 도메인 네임
  - a.com 이라는 주소의 컴퓨터(서버)의 주소 a.com 은 도메인 네임이라고 하며, 사람이 기억하기 쉽도록 만들어진 이름이다.
  - 실제로 컴퓨터에 접속할 때는 그 도메인에 해당되는 ip를 통해서 접속한다.

## 서버에서 일어나는 일 (포트)

<center><img src="/assets/post-img/nodejs/server.png" alt="" width="500"></center>

- a.com을 가진 서버 컴퓨터에는 여러가지 서버 sw (엡서버, 게임서버, 채팅서버 등)가 설치되어 있을 수 있다.
- 그럼 사용자가 a.com을 치고 서버 컴퓨터에 접속했을때, 서버 컴퓨터는 어떤 서버애플리케이션을 연결해서 그 애플리케이션이 응답할 수 있게 하는가?

<center><img src="/assets/post-img/nodejs/port.png" alt="" width="500"></center>

- 컴퓨터에는 0 ~ 65535번의 포트(port)라는 문이 있다.
- 보통 웹서버는 80번 포트에 연결시켜 놓는다.    
  (웹서버가 80번 포트를 바라보게 한다. 80번 포트를 웹서버가 리스닝 하고 있다.)
- 사용자가 `http://a.com:80` 주소를 입력하고 엔터를 땅 치면,
  - 웹브라우저는 우선 `http://a.com`에 해당되는 컴퓨터를 찾는다.
  - 그리고 `http://a.com`에 해당되는 컴퓨터에게 80번 포트와 연결하고 싶다고 이야기 한다.
  - 80번 포트는 웹서버를 호출해서 응답한다.
  - 매번 웹서버에 접속할때 마다 :80 port를 적는 것은 귀찮기 때문에 생략 가능하다.

```
http://naver.com:80
// :80생략 가능, https인 경우 오류발생
http://daum.net:80
// http를 통해서 접속하는 경우 웹서버는 80번 포트를 쓰자고 약속되어 있음
```




***


# nodejs 서버연결을 위한 코드 해석하기

## 서버연결을 위한 코드와 해석

  ```javascript
  const http = require('http');

  const hostname = '127.0.0.1'; // 서버 컴퓨터의 ip
  const port = 3000; //

  const server = http.createServer((req, res) => {
    // createServer 명령을 통해 서버 한대를 만든다.
    res.statusCode = 200; // 통신 성공
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
  });

  server.listen(port, hostname, () => {
    // 만든 서버가 이 컴퓨터에 리스닝을 하도록 시킨다.
    // 첫번째 인자 port는 3000번이고 hostname은 이 컴퓨터의 ip 같은 것
    console.log(`Server running at http://${hostname}:${port}/`);
  });
  ```
