---
layout: post
title: Express-간단한 웹에플리케이션 만들기
category: nodejs
tags: [nodejs, Express]
comments: true
---
# Express-간단한 웹에플리케이션 만들기
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11886)   
>  Express 프레임워크를 사용하여 간단한 nodejs 웹에플리케이션을 만든다.

## 예시 - 코드작성
- entry app 만들기 (app.js) [express 가이드 참고](http://expressjs.com/ko/starter/hello-world.html)
- main(entry) app, main(entry) file   
  : 가장 최초로 실행되는, 진입점이 되는 어플리케이션
- app.js 코드작성   
  - 앱은 서버를 시작하며 3000번 포트에서 연결을 청취 app.listen(포트번호)
  - 앱은 루트 URL(/) 또는 라우트에 대한 요청에 res.send(응답내용)으로 응답
- `예시 코드에 익숙해질 필요가 있음`

```javascript
var express = require('express');
var app = express();

app.get('/',function(req, res){
// 사용자가 root 디렉토리 (/)에 접속했을때!
// 여기서 get을 라우터라고 한다 (라우팅 : 길찾기)
	res.send('hello siwa!');
});
app.get('/login',function(req, res){
	res.send('<h1>login please siwa!</h1>');
});

app.listen(3000, function(){
	console.log('connected 3000 port!');
});
```

## 예시 - 코드실행
- 터미널에서 node app.js 입력하여 파일을 실행
- 브라우저에 http://localhost:3000, http://localhost:3000/login 로 접속하여 결과 확인
