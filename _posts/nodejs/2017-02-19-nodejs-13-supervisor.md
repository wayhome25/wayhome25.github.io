---
layout: post
title: POST 방식을 이용한 정보의 전달
category: nodejs
tags: [nodejs, Express, post]
comments: true
---
# POST 방식을 이용한 정보의 전달
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11949)      
> post 방식을 통한 정보의 전달 방법에 대해서 살펴보고 express에서 post를 다루는 방법을 배운다.

## GET방식-POST방식 소개
### GET방식
- 사용자의 접속(요청)에 따라서 어플리케이션이 응답한 정보를 사용자가 GET 하는 것
- 기본적으로 웹브라우저에 URL을 입력하여 어떠한 정보를 가져오는 것을 GET 방식이라 한다.
- 경우에 따라서는 쿼리스트링을 통해서 어떠한 정보를 앱에 요청해서 가져오기도 한다.
### POST
- 서버에 있는 정보를 가져오는 것 (GET)이 아닌 사용자의 정보를 서버에 전송(POST) 하는 방식
- ex.사용자의 로그인 정보를 전송하거나, 작성한 글을 서버로 전송하는 것  

## 제출양식(form) 예시
- `jade 방식으로 form을 작성하여 라우터에 적용한다.`

### 템플릿 엔진을 사용하여 form.jade 파일 작성
```
doctype html
html
  head
    meta(charset='utf-8')
  body
    form(action='/form_receiver' method='get')
      p
        input(type='text' name='title')
      p
        textarea(name='desc')
      p
        input(type='submit')
```

### app.js에 라우터를 작성하여 form.jade와 연결
```javascript
app.set('view engine', 'jade'); // 템플릿엔진 설정
app.set('views', './views'); // 템플릿엔진 경로 설정
app.get('/form',function(req, res){
	res.render('form'); // 템플릿엔진 라우터 설정
});
app.get('/form_receiver', function(req, res){
	var title = req.query.title; //get방식으로 제출된 form 데이터에 접근
	var desc = req.query.desc;
	res.send(title+', '+desc);
});
```

## POST 방식으로 전송된 데이터의 사용 방법
### post 방식으로 전송한 데이터를 애플리케이션은 어떻게 받을 수 있는가?
- post 방식으로 데이터를 전송하면 app.get이 아닌 app.post 메소드에 콘트롤러를 연결 시켜서 실행 시킬 수 있으며, 추가로 미들웨어가 필요하다.
- body-parser 미들웨어 : post 방식으로 전송된 데이터를 애플리케이션에서 사용할 수 있도록 도와주는 플러그인(확장기능)  
### body-parser [적용방법]([https://www.npmjs.com/package/body-parser])
- 설치 `npm install body-parser`
- app.js에 해당 모듈 추가 `var bodyParser = require('body-parser')`
- app.js에 해당 모듈과 애플리케이션 연결     
  `app.use(bodyParser.urlencoded({ extended: false }))`
- 사용자에게 받은 모든 요청들은 bodyParser가 제일 먼저 실행되고, 사용자가 post 방식으로 전송한 데이터가 있다면, req 객체가 원래 갖고 있지 않았던 body라는 객체를 bodyParser가 추가한다. 그리고 사용자가 전송한 데이터의 이름이 title 이라면 body객체의 title 속성에 그 값을 넣는다.
```javascript
var express = require('express');
var app = express()
var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))

app.post('/form_receiver', function(req, res) {
  // bodyParser 미들웨어를 통해 req에 body 객체추가
	var t = req.body.title;
	var d = req.body.desc;
	res.send(t+','+d);
});
```

## GET과 POST의 차이
- GET 방식으로 정보를 전송하면 정보가 URL에 표시되어 보안의 문제가 있다.    
  (하지만 GET, POST 모두 보안에 불완전한 기술이다)
- GET 방식은 URL 길이 제한의 문제가 있다.
