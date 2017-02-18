---
layout: post
title: 모듈과 NPM - nodejs 모듈
category: nodejs
tags: [nodejs, npm, 모듈]
comments: true
---
# 모듈과 NPM - nodejs 모듈
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11854)   
> 에플리케이션에서 부품으로 사용할 로직인 모듈에 대해서 알아보고 모듈을 편리하게 관리하는 기술인 NPM을 사용하는 기본적인 방법을 알아본다.

## 모듈 기초

- `모듈 = 부품`
- 웹서버를 처음부터 끝까지 만드는 것은 아주 어려운 일
- 따라서 nodejs 에서는 기본적인 웹서버를 만들어 놓고, 사용자가 쓸 수 있도록 함
- 사용자는 nodejs가 마련해 놓은 웹서버를 가져다 쓸 수 있는 방법을 배운다.

## nodejs의 서버 접속 모듈

### 코드 전체
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

### http 모듈 호출 코드

```javascript
const http = require('http');
//아래 코드가 동작하게 위해서는 nodejs에서 제공하는 http라는 모듈(부품)이 필요하다.
//require라는 함수를 통해서 http 모듈을 가져오고 상수에 담는다.
```

- http 모듈 사용 설명서 : [nodejs document](https://nodejs.org/dist/latest-v6.x/docs/api/http.html)
    - http.createServer() 메소드 : Returns a new instance of http.Server    
      (http 모듈의 Server객체를 리턴)
    - http.createServer().listen() 메소드

- 모듈은 부품이다. `모듈이라는 부품을 사용하기 위해서는 require라는 함수로 호출`한다.
- nodejs는 기본적으로 앱을 만들기 위한 부품을 기본적으로 제공한다. (ex. http)
- 부품의 사용설명서는 nodejs 사이트의 [document](https://nodejs.org/dist/latest-v6.x/docs/api/)에서 확인 가능하다.

## nodejs의 os 모듈 사용해보기

### os.js

```javascript
const os = require('os');
console.log(os.platform());
// The os.platform() method returns a string identifying
// the operating system platform as set during compile time of Node.js.
```
### 터미널

```shell
$ node os.js
darwin
```
