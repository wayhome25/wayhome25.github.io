---
layout: post
title: nodejs 서버연결 및 인터넷의 동작 방법 2-1
category: nodejs
tags: [nodejs]
comments: true
---
# nodejs 간단한 웹앱 만들기
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11853)   
> Nodejs를 이용해서 간단한 서버 에플리케이션을 만들어 본다.

# nodejs 서버연결

## 서버연결을 위한 코드
- node.org > about 에서 파일 복사 후 `webserver.js` 파일에 붙여넣기

  ```javascript
  const http = require('http');

  const hostname = '127.0.0.1';
  const port = 3000;

  const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
  });

  server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
  });
  ```

- 터미널에서 `node webserver.js` 실행

  ```
  $ node webserver.js
  Server running at http://127.0.0.1:3000/
  ```
- 웹브라우저를 통해 http://127.0.0.1:3000/ 경로에 접속하면 브라우저에 `hello world` 가 출력

## 이것의 의미

- webserver.js 자바스크립트의 코드가 웹 브라우저를 통해서 요청한 내용을 받아서 우리에게 hello world 라는 텍스트를 전송 한 것
- 그 결과 우리의 웹브라우저는 화면에 hello world를 출력 할 수 있게 된 것  
- 이 개념을 이해하기 위해서는 인터넷, 도메인 네임,IP, port 개념을 먼저 이해할 필요가 있음 (개념에 대한 설명은 다음 글 참고)
