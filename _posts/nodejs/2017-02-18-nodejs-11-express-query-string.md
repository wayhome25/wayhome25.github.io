---
layout: post
title: Express-URL을 이용한 정보의 전달 - 쿼리스트링
category: nodejs
tags: [nodejs, Express, query]
comments: true
---
# Express-URL을 이용한 정보의 전달
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11945)      
> URL을 통해서 에플리케이션에 정보를 전달하는 방법에 대해서 알아본다.

## 쿼리 스트링 소개
- path : http://a.com/login 에서 /login 부분
- 하나의 path(라우터) 에서 경우에 따라 다른 결과를 보여주기 위해서는 쿼리스트링이 사용된다.
- 쿼리스트링은 어떤 애플리케이션에게 정보를 전달할 때 사용되는 URL에 약속되어 있는 국제적인 표준


<center>
<figure>
<img src="/assets/post-img/nodejs/querystring.png" alt="" width="500">
<figcaption>URL의 구성요소</figcaption>
</figure>
</center>


## Express의 query 객체의 사용  
> 동적인 파일을 통해서 (app.js 에 직접 작성) 쿼리스트링 사용에 대해 살펴본다.

- url 내의 쿼리스트링을 가져오려면 `req.query` 를 사용해야한다.
- express api reference [req.query](http://expressjs.com/en/4x/api.html#req) 참고
- 복수의 쿼리스트링을 가져오는 것도 가능하다.
```javascript
app.get('/topic', function(req, res) {
	// url이 http://a.com/topic?id=1&name=siwa 일때
	res.send(req.query.id+','+req.query.name); // 1,siwa 출력
})
```

## query 객체의 활용

```javascript
app.get('/topic', function(req, res){
	var topic = [
		'javascript is...',
		'nodejs is...',
		'express is...'
	];
	var li = `
	<li><a href="/topic?id=0">js</a></li>
	<li><a href="/topic?id=1">nodejs</a></li>
	<li><a href="/topic?id=2">express</a></li>
	`
  // 선택한 링크에 따라서 다른 정보를 출력하는 동적인 애플리케이션의 기본골격
	res.send(li + '<br>' + topic[req.query.id]);
})
```
## 의미론적인 URL (semantic url)
- 비전문가(사용자)에게 친숙한, (의미를 표현하는) 구조적인 URL [참고글 링크](https://elegantcoder.com/useful-semantic-url/)

일반 URL | 시맨틱 URL
:-------: | :--------:
board.php?id=notice&mode=list&page=1 | board/notice/list/1
board.php?id=notice&mode=view&entry=10 | board/notice/10

### Semantic URL의 장점
- 깔끔한 URL을 유지할 수 있다.
- 사용자가 URL을 기억하기 쉽다
- 주요정보를 변수로 처리하지 않고 디렉토리 인 것처럼 다루므로 SEO 에도 도움이 된다.

### 쿼리스트링이 아닌 path 방식의 URL의 사용
```javascript
app.get('/topic/:id/:mode', function(req, res){
// 라우터 경로의 변경 /:id/:mode 를 통해 path 방식 url 값을 가져올 수 있다.
	var topic = [
		'javascript is...',
		'nodejs is...',
		'express is...'
	];
	var li = `
	<li><a href="/topic/0">js</a></li>
	<li><a href="/topic/1">nodejs</a></li>
	<li><a href="/topic/2">express</a></li>
	`
	res.send(li + '<br>' + topic[req.params.id] + req.params.mode);
	//path 방식을 사용하는 url의 경우 params를 통해서 값을 가져올 수 있음
})
```
- Restful api 등을 통해서 시맨틱 URL을 잘 사용하는 방법에 대해서 익힐 수 있다.
