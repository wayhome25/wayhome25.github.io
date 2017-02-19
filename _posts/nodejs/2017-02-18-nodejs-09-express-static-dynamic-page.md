---
layout: post
title: Express-동적파일을 서비스 하는 법
category: nodejs
tags: [nodejs, Express, static]
comments: true
---
# Express-웹페이지를 표현하는 방법
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11857)   
>   웹페이지를 정적으로 만드는 방법과 동적으로 만드는 방법의 장점과 단점을 살펴본다.

## 정적인(static) 파일을 전달하는 방법
- express에게 정적인 파일이 모여있는 디렉토리 경로를 알려준다. `app.use(express.static('public'));`
- 정적인 파일의 디렉토리로 설정한 public 폴더 내에 static.html 파일을 작성한다.
- 해당 페이지는 `http://localhost:3000/static.html` 경로를 통해서 접근 가능하다.
- 정적인 파일의 변경사항은 node application의 재기동 (터미널에서 `node app.js` 입력) 없이도 바로 반영시킬 수 있다.


## 동적인(dynamic) 파일을 전달하는 방법
- app.js 파일 (main file) 내에 라우터를 추가한다.
```javascript
app.get('/dynamic', function(req, res){
	var lis = '';
	for(var i = 0; i <5; i++){
		lis += '<li>coding ' + i + '</li>';
	}
	// 자바스크립트 새로운 표준 formatted text 기능
	// ` `(grave accent) 사용을 통해서 JS에서 여려줄의 코드를 넣을 수 없는 문제를 해결
	var output =
	`<!DOCTYPE html>
	<html>
	  <head>
	    <meta charset="utf-8">
	  </head>
	  <body>
	    hello Dynamic html~~!
			<ul>
				${lis} <!--문자열 내에서 변수 사용-->
			</ul>
	  </body>
	</html>`;
	res.send(output);
});
```

- 터미널에 `node app.js` 입력 후, `http://localhost:3000/dynamic` 경로를 통해서 결과 확인한다.
- 동적인 파일의 변경사항은 node application의 재기동이 필요하다.

## 장단점
### 정적인 파일 (static)
- 장점
	- 작성이 편리하다
	- 변경내용 적용을 위해 node application의 재기동이 필요하지 않다.
	- app.js에 라우터 설정이 필요없다. (http://localhost:3000/sample.html 처럼 파일명으로 바로 접속 가능)
- 단점
	- 반복, 변수 등의 프로그래밍적인 요소를 사용할 수 없다.

### 동적인 파일 (dynamic)
- 장점
	- 반복, 변수 등의 프로그래밍적인 요소를 사용할 수 있다.  
- 단점
	- js안에서 html작성이 까다롭다.

## 템플릿 엔진
- 정적인 것의 장점과 동적인 것의 장점을 합친 방법
- 라우터 설정 필요, html 작성 편리, 변수 사용 가능, 수정 후 재기동 불필요
- [템플릿 엔진 jade 알아보기](https://wayhome25.github.io/nodejs/2017/02/18/nodejs-10-express-template-engine-jade/)
