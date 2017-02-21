---
layout: post
title: Express-정적파일을 서비스 하는 법
category: nodejs
tags: [nodejs, Express]
comments: true
---
# Express-정적파일을 서비스하는 법
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11857)   
>   이미지나 텍스트 파일와 같은 정적인 파일을 서비스하는 방법을 다룬다.

## Express에서 정적 파일 제공
- [가이드 문서 참고](http://expressjs.com/ko/starter/static-files.html)
- 서버를 시작하는 코드 내에 아래 코드 추가
```javascript
app.use(express.static('public'));
// public : **정적인 파일이 위치할 디렉토리의 이름**
```
- public 폴더 내에 bento.png 이미지 파일 생성
- `http://localhost:3000/bento.png` 로 접속하면 이미지 출력
- `http://localhost:3000/bento` 로 접속했을때 bento.png 이미지가 출력되도록 하는 코드
```javascript
app.get('/bento', function(req, res){
	res.send('hello bento! <img src="/bento.png">')
})
```

## 정적인 파일이 접근할 라우터 path 설정
> express.static 함수를 통해 제공되는 파일에 대한 가상 경로

```javascript
app.use('/users', express.static('uploads'));

```
- 이를 통해서 /users 경로를 통해 uploads 디렉토리에 포함된 파일을 로드할 수 있음     
  `(ex. http://localhost:3000/users/siwa.png)`
