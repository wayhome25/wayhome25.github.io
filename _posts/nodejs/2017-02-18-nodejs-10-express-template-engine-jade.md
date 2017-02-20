---
layout: post
title: Express-템플릿 엔진 (Jade)
category: nodejs
tags: [nodejs, Express, jade, template engine]
comments: true
---
# Express-템플릿 엔진 (Jade)
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11915)   
>  템플릿 엔진의 개념과 템플릿 엔진의 한 종류인 Jade를 사용하는 방법을 알아본다.

`jade의 이름이 pug로 변경되었다.` [참고](https://blog.outsider.ne.kr/1225)

## 소개
- 템플릿 엔진이란 동적인 파일과 정적인 파일의 장단점을 잘 결합한 형태의 새로운 체계이다.
- jade는 node.js용으로 만들어진 view 템플릿 엔진이다.
- jade 문법에 맞게 작성하면 해당 내용을 html이나 자바스크립트로 만들어 준다.
- [jade syntax 참고](https://naltatis.github.io/jade-syntax-docs/)


## 템플릿 엔진 사용하기
1. 템플릿 엔진 어플리케이션 설치 (Jade)
- express 자체는 템플릿 엔진의 기능을 갖고 있지 않기 때문에, 템플릿 엔진을 따로 설치할 필요가 있다.
```
// 템플릿 엔진 jade 설치 (터미널)
npm install jade --save
```
2. Jade와 express 연결  
- express가 jade를 렌더링 하려면 아래와 같은 2가지 어플리케이션 설정이 필요하다.
- express에게 template view engine을 알려주는 설정   
`app.set('view engine', 'jade')`
- express에게 template 파일이 모여있는 디렉토리를 알려주는 설정    
`app.set('views', './views')`
```javascript
// app.js (main file)
app.set('view engine', 'jade')
// 사용할 view engine을 express에게 알려주는 코드
// express 프레임워크와 jade 엔진을 연결!
app.set('views', './views')
// 템플릿이 있는 디렉토리를 express에게 알려주는 코드 (생략가능, 디폴트 경로 ./views)
```
3. 템플릿 렌더링
	- 템플릿 엔진이 적용된 페이지의 라우터를 추가한다.
```javascript
app.get('/template', function(req, res){
	res.render('temp');
})
// 템플릿 엔진의 소스코드를 가지고 와서 웹페이지를 만들어 내는 res 객체의 메소드
```
4. 렌더링된 페이지 확인
	- http://localhost:3000/template 경로로 get방식으로 접속한 사용자에게 fucntion이 실행이 되면서 'temp'라는 템플릿 파일을 렌더링해서 웹페이지로 전송한다.


##  템플릿 엔진 Jade의 사용법과 문법
### 기본문법
- [jade syntax 참고](https://naltatis.github.io/jade-syntax-docs/)
- /views/temp.jade 파일 작성
- 코드내용 (temp.jade)
	```
	html
	  head
	    title= _title
	  body
	    h1 hello Jade
	    ul
	      -for (var i=0; i<5; i++)
	        li coding
	    div= time
	```
- 렌더링 결과
	```html
	<html>
	<head>
	  <title>Jade</title>
	</head>
	<body>
	  <h1>hello Jade</h1>
	  <ul>
	    <li>coding</li>
	    <li>coding</li>
	    <li>coding</li>
	    <li>coding</li>
	    <li>coding</li>
	  </ul>
	  <div>Sat Feb 18 2017 17:50:48 GMT+0900 (KST)</div>
	</body>
	</html>
	```

### 변수 사용방법
- 변수의 정의는 jade 밖의 jade를 사용하는 express 에서 선언
```javascript
// app.js
app.get('/template', function(req, res){
	res.render('temp', {time: Date(), _title: 'Jade'});
	//.reder() 매소드의 2번째 인자로 템플릿 파일에서 사용할 변수를 객체에 담아서 정의
})
```
- 변수의 사용은 jade 파일 내에서 아래와 같이 입력
```
body
	p #{time}
	p #{_title}
```

- 참고) 렌더링된 html 파일이 편하게 출력되게 하려면 아래 코드 추가   
(구글 검색 키워드 : express jade html pretty)
```javascript
// app.js
app.locals.pretty = true;
```
