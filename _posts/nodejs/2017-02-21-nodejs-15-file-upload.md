---
layout: post
title: nodejs 파일 업로드 - multer 모듈사용
category: nodejs
tags: [nodejs, Express, upload, file, multer]
comments: true
---
# nodejs 파일 업로드
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11959)      
>  사용자가 업로드한 파일을 받아서 저장하는 방법에 대해서 알아봅니다

## 파일 업로드 소개 및 준비

### 만드려고 하는 것
- 사용자가 앱에게 전달하는 정보는 크게 `텍스트`와 `파일` 2가지로 나눌 수 있다.
- 사용자가 `파일`을 앱에게 전달하는 방법에 대해서 알아본다.
- 동작 개요
  - 파일 선택 form
  - 파일 선택 후 submit 버튼을 눌르면 파일 전송
  - 루트 디렉토리 내 uploads 폴더에 전송된 파일이 저장
  - 전송된 파일명을 화면에 표시
- express는 사용자가 업로드한 파일을 받아서 저장하는 기본 기능을 제공하지 않는다.
- 따라서 모듈을 설치해서 (ex. multer) 사용자가 전송한 파일을 처리하는 작업을 해야한다.
- `multer 모듈` 설치코드 (터미널)

```
npm install --save multer
```

## 파일 업로드 양식 (form)

### 라우팅 1 - /upload path의 GET 방식 접속
-  http://localhost:3000/upload path 로 접속하면 업로드 화면을 보여주도록 라우터 연결

```javascript
// 업로드 - 파일 업로드 폼
app.get('/upload', function(req, res){
  res.render('upload');
});
```

### 탬플릿 파일
- 탬플릿 파일 저장 경로인 /views_file/ 폴더 내에 업로드 화면 구현을 위한 탬플릿 파일 작성 (upload.jade)
- form 의 type을 `enctype="multipart/form-data"` 로 설정해야 사용자가 전송한 파일을 서버로 전송할 수 있다.
- 업로드폼 탬플릿 파일 (upload.jade) 코드 예시

```
doctype html
html
  head
    meta(charset='utf-8')
  body
    form(action='upload' method='post' enctype="multipart/form-data")
      input(type='file' name='userfile')
      input(type='submit')
```
- 업로드폼 탬플릿 파일 (upload.jade) 랜더링 결과
<center>
<figure>
<img src="/assets/post-img/nodejs/upload.png" alt="jade 랜더링 결과">
<figcaption>upload.jade 파일 랜더링 결과</figcaption>
</figure>
</center>

### 라우팅 2 - /upload path의 post 방식 접속
- form을 통해서 입력된 데이터가 upload 경로로 post 방식으로 전송되었을 때 (action='upload' method='post') 전송된 데이터를 처리하기 위한 라우터 연결

```javascript
app.post('/upload', function(req, res){
  res.send('업로드 성공!');
});
```

## multer 소개
### multer 모듈 적용 코드

```javascript
var multer = require('multer'); // express에 multer모듈 적용 (for 파일업로드)
var upload = multer({ dest: 'uploads/' })
// 입력한 파일이 uploads/ 폴더 내에 저장된다.
// multer라는 모듈이 함수라서 함수에 옵션을 줘서 실행을 시키면, 해당 함수는 미들웨어를 리턴한다.
```

### multer 모듈을 사용하여 post로 전송된 파일 처리
- [multer 가이드 문서](https://github.com/expressjs/multer)
- 사용자가 post 방식으로 전송한 데이터가 upload 라는 디렉토리를 향하고 있다면,
- 그 다음 함수를 실행하여 콘트롤러로 연결한다.
- 미들웨어 `upload.single('avatar')`는 뒤의 `function(req, res)`함수가 실행되기 전에 먼저 실행.
- 미들웨어는 사용자가 전송한 데이터 중에서 만약 파일이 포함되어 있다면,
- 그 파일을 가공해서 req객체에 file 이라는 프로퍼티를 암시적으로 추가도록 약속되어 있는 함수.
- `upload.single('avatar')` 의 매개변수 `'avatar'`는 form을 통해 전송되는 파일의 `name`속성을 가져야 함.

```javascript
app.post('/upload', upload.single('userfile'), function(req, res){
  res.send('Uploaded! : '+req.file); // object를 리턴함
  console.log(req.file); // 콘솔(터미널)을 통해서 req.file Object 내용 확인 가능.
});
```
- 터미널 콘솔 결과화면 [file객체 상세 참고](https://github.com/expressjs/multer#api)
<center>
<figure>
<img src="/assets/post-img/nodejs/upload-console.png" alt="터미널 콘솔 결과">
<figcaption>console.log(req.file) 터미널 콘솔 결과화면</figcaption>
</figure>
</center>

## multer 심화
> multer 모듈을 통해서 post로 전송된 파일의 저장경로와 파일명 등을 처리한다.

### multer - 저장경로, 파일명 설정
- multer 모듈을 통해서 post로 전송된 파일의 저장경로와 파일명 등을 처리하기 위해서는 DiskStorage 엔진이 필요하다. ([참고](https://github.com/expressjs/multer#storage) DiskStorage : The disk storage engine gives you full control on storing files to disk.)
- DiskStorage 적용 예시 (app_file.js)

```javascript
var multer = require('multer'); // multer모듈 적용 (for 파일업로드)
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/') // cb 콜백함수를 통해 전송된 파일 저장 디렉토리 설정
  }
  filename: function (req, file, cb) {
    cb(null, file.originalname) // cb 콜백함수를 통해 전송된 파일 이름 설정
  }
})
var upload = multer({ storage: storage })
```
### 저장한 파일 조회 - static 파일 제공
- 정적인 파일이 위치할 디렉토리의 이름 선언 (app_file.js)
- 정적인 파일이 접근할 라우터 path 설정     
  (express.static 함수를 통해 제공되는 파일에 대한 가상 경로)

```javascript
app.use('/users', express.static('uploads'));

```
- 이를 통해서 /users 경로를 통해 uploads 디렉토리에 포함된 파일을 로드할 수 있음     
  `(ex. http://localhost:3000/users/siwa.png)`
