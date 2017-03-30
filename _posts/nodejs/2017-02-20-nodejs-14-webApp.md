---
layout: post
title: nodejs 간단한 웹어플리케이션 제작
category: nodejs
tags: [nodejs, Express, post]
comments: true
---
# nodejs 간단한 웹어플리케이션 제작
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11950)      
>  전형적인 웹에플리케이션을 제작하는 방법을 알아봅니다. 현대적인 웹에플리케이션은 정보를 저장하는 공간으로 데이터베이스를 사용합니다만 우리는 수업의 난이도를 조절하기 위해서 배우기 쉬운 파일을 사용합니다. 데이터베이스를 활용하는 수업은 뒤에서 다시 다루겠습니다.


## 오리엔테이션

- 웹 어플리케이션의 전형적인 기능
  - 사용자로 부터 정보를 입력 받아서 서버에 저장하고 필요한 정보를 요청하면 그것을 제공하는 것
- 만들어 볼 것
  - 조회1 : 글 목록 출력
  - 조회2 : 글 내용 조회
  - 작성 : 글 내용 작성후 post 방식으로 전송
  - 저장 : post 방식으로 전송된 데이터 저장
- 현대적인 웹어플리케이션은 사용자가 입력한 정보를 데이터베이스에 저장하지만, 이번에는 간단하게 파일에 저장한다.   

### 만들어 볼 웹어플리케이션의 라우팅 구조
- 홈 : localhost:3000
- 작성 (글작성 폼)  : localhost:3000/topic/new
- 저장 (폼 전송 타겟) : localhost:3000/topic
- 조회 (글 리스트) : localhost:3000/topic
- 조회 (글 내용) : localhost:3000/topic/nodejs(글제목)


## 라우팅
### express 모듈 적용 및 서버 연결
- [express 가이드 문서](http://expressjs.com/ko/starter/hello-world.html)
- 프로젝트 파일 내에 app_file.js 파일(main/entry file)을 작성한다.
- 코드 예시

```javascript
var express = require('express'); //express 모듈을 가져온다
var app = express(); //  express 모듈을 사용하여 app 객체를 생성한다.
app.listen(3000, function() {
  console.log('connected, 3000 port!')
//app객체가 가진 listen 메소드를 사용하여
//어플리케이션이 특정 포트를 리스닝 하도록 만든다
})
```
- 연결확인
  - 터미널에서 `node app_file.js` 혹은 `supervisor app_file.js `
  - 브라우저에서 `http://localhost:3000/` 접속


### 라우팅 및 템플릿 엔진 설정
- 라우팅 : 사용자의 요청을 적당한 콘트롤러와 연결시켜주는 연결작업
- [express 가이드 문서 - 라우팅](http://expressjs.com/ko/starter/basic-routing.html)
- 라우팅 작업 예시 (app_file.js)

```javascript
app.get('/topic/new', function(req, res){
  res.send('topic/new 경로에요');
})
```

### express-템플릿 엔진 연결 (app_file.js)
> 웹 어플리케이션에 템플릿엔진 (jade)를 연결하고 설정한다.

- [express 가이드 문서 - 템플릿 엔진](http://expressjs.com/ko/guide/using-template-engines.html)
- 프로젝트 폴더 내에 템플릿 파일을 모아둘 views_file 폴더를 만든다.
- entry file (app_file.js) 내에 템플릿 파일에 대한 설정을 한다.
- 탬플릿 설정 작업 예시 (app_file.js)

```javascript
app.set('view engine', 'jade') // 탬플릿 엔진 사용 선언
app.set('views','./views_file') // 탬플릿 파일들의 경로
app.get('/topic/new', function(req, res){
  res.render('new')
  // render : 템플릿 파일 사용(렌더링) 하겠다.
  // render('new') : 템플릿 폴더 (./views_file) 내의 new 라는 파일을 콘트롤러로 쓰겠다.  
})
```

### 템플릿 문서 작성 (new.jade)
> form 문서를 jade 템플릿을 사용하여 작성한다.    
> `jade의 이름이 pug로 변경되었다.` [참고](https://blog.outsider.ne.kr/1225)

- views_file 폴더 내에 템플릿 문서를 작성한다. (new.jade)
- title과 description을 사용자로부터 입력받아, `post` 방식으로 `/topic` 경로로 전송하는 문서
- 탬플릿 설정 작업 예시 (new.jade)

```
doctype html
html
  head
    meta(charset='utf-8')
  body
    form(action='/topic' method='post')
      p
        input(type='text' name='title' placeholder='title')
      p
        textarea(name='description')
      p
        input(type='submit')
```

### post로 전달받은 정보 사용
> post 방식으로 전송된 데이터를 가져온다.

- 폼을 통해 전송된 post 정보의 라우팅 예시 (app_file.js)

```javascript
app.post('/topic', function(req, res) {
  res.send('Hi, post!' + req.body.title)
})
```
- post 전달 정보를 express 에서 사용하기 위해서는 `미들웨어`가 필요하다. (ex.body-parser)
  - 설치 : 터미널에서  `npm install body-parser --save` 입력
  - express-미들웨어(body-parser) 연결 및 설정(app_file.js)

```javascript
var bodyParser = require('body-parser')
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))  
```
- 웹어플리케이션에 들어오는 모든 요청에 대해서 post 방식으로 들어오게 되면, body-parser가 어플리케이션 중간에서 요청을 가로채서 req 객체에 body라는 프로퍼티를 만들어서 post 데이터에 접근할 수 있게 해준다.


## 저장 - 본문저장
> post 방식으로 전송된 데이터를 별도 파일에 저장한다.

- 데이터베이스를 사용하지 않고 파일에 저장하는 것은 `아주 좋지 않은 방법`이지만, 어플리케이션의 대략적인 구조를 이해하고 복잡도를 줄이기 위해서 데이터를 파일에 저장하여 연습한다.
- 프로젝트 폴더 내에 data 폴더를 만든다.
- 사용자가 전송한 title 을 파일의 제목으로, description을 파일의 내용으로 data 폴더 내에 저장한다.
- 파일을 제어하기 위해서는 nodejs 가 제공하는 `file system 모듈` 사용이 필요하다.
  - [fs.writeFile 가이드 참고](https://nodejs.org/dist/latest-v6.x/docs/api/fs.html#fs_fs_writefile_file_data_options_callback)  
- post로 전송한 데이터를 파일을 만들어 저장하는 예시 (app_file.js)

```javascript
var fs = require('fs'); // file system nodejs 모듈 적용
var bodyParser = require('body-parser') // body-parser 미들웨어 설정
app.use(bodyParser.urlencoded({ extended: false }))  

app.post('/topic', function(req, res) {
  var title = req.body.title;
  var description = req.body.description;
  fs.writeFile('data/'+title, description, function(err){
    if(err){
      console.log(err);
      // 에러정보가 터미널에 표시된다.
      res.status(500).send('Internal Server Error');
      // send 메소드는, send가 실행되면 그 다음코드는 실행되지 않는다.
    }
    res.send('data saved!');
    // callback 함수가 실행된 후에 response가 가능하다.
  });
})
```

## 조회1 - 글 목록 만들기
> 별도 파일에 저장한 글들의 목록을 화면에 표시한다.

- http://localhost:3000/topic 에 접속했을 때 저장한 글 제목 목록이 표시되도록 한다.
- topic path에 대한 get방식 라우터를 만들고 콘트롤러로 템플릿 파일을 연결한다.
- data 폴더에 저장된 파일들을 가져오기 위해서는 `fs.readdir` 메소드가 필요하다. [참고](https://nodejs.org/dist/latest-v6.x/docs/api/fs.html#fs_fs_readdir_path_options_callback)
- 라우터 코드 예시 (app_file.js)

```javascript
// 조회 - 글목록 표시
app.get('/topic', function(req, res) {
  fs.readdir('data',function(err, files) {
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    res.render('view', {topics:files});
    // 변수 topic에 files 배열을 담아서 리턴
    // 이제 템플릿파일 view.jade에서 해당 변수를 사용할 수있음
  })
});
```
- 템플릿 코드 예시 (view.jade)
  - 반복문을 통해서 리스트를 출력한다. [jade 반복문 참고](https://pugjs.org/language/iteration.html)

```
doctype html
html
  head
    meta(charset='utf-8')
  body
    h1 Server Side Javascript
    ul
      each val in topics
        li
          a(href='/topic/'+val)= val
```

- 실행결과 (http://localhost:3000/topic)
<center>
<figure>
<img src="/assets/post-img/nodejs/jade_for.png" alt="jade 반복문 실행결과 화면">
<figcaption>Jade 반복문의 실행결과</figcaption>
</figure>
</center>

## 조회1 - 본문 읽기
- 어떻게 라우터와 연결할 것인가? `params`
  - path경로의 라우터 추가 코드 예시 (app_file.js)

```javascript
app.get('/topic/:id', function(req, res){
// path 방식을 사용하는 url의 경우 params를 통해서 값을 가져올 수 있음
  var id = req.params.id;
  res.send(id);
});
```

- 파일 내용은 어떻게 읽어올 것인가? `fs.readfile`
  - 파일을 읽어오려면 fs.readfile 메소드 사용 [가이드 참고](https://nodejs.org/api/fs.html#fs_fs_readfile_file_options_callback)
  - 별도 파일을 읽어오는 코드 예시 (app_file.js)

```javascript
// 조회 - 글내용 조회
app.get('/topic/:id', function(req, res){
  var id = req.params.id;
  fs.readdir('data',function(err, files) {
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    fs.readFile('data/'+id, 'utf8', function(err, data){
      if(err){
        console.log(err);
        res.status(500).send('Internal Server Error');
      }
      res.render('view', {topics: files, title: id, description: data});
    });
  });
});
```
  - 별도 파일을 읽어오는 코드 예시 (view.jade)

```
doctype html
html
  head
    meta(charset='utf-8')
  body
    h1 Server Side Javascript
    ul
      each val in topics
        li
          a(href='/topic/'+val) #{val}
    article
      h2 #{title}
      p #{description}
```
- 지금까지의 내용은 근대적인 어플리케이션을 구축하는데 있어서 소위 `미들웨어라고 하는 웹서버와 데이터베이스 사이에 존재하는 nodejs, JS, express` 등이 하는 역할의 가장 중요한 부분이다.  

## 코드의 개선
### 중복 제거
- app_file.js 에서 중복된 부분을 제거한다.
- 중복 제거의 장점
  - 유지보수의 용이
  - 코드의 양이 줄어들어 가독성 개선
- 중복 제거 연습방법
  - 일단 중복과 상관 없이 코드를 짠다.
  - 나중에 한발짝 물러나서 자신이 작성한 코드를 살펴본다.
  - 중복이 보이면 제거한다.
- 중복 제거 이전 코드  

```javascript
// 조회1 - 글목록 표시
app.get('/topic', function(req, res) {
  fs.readdir('data',function(err, files) {
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    res.render('view', {topics:files});
    // .reder() 매소드의 2번째 인자로 템플릿 파일에서 사용할 변수를 객체에 담아 정의
    // 변수 topic에 files 배열을 담아서 리턴
    // 이제 템플릿파일 view.jade에서 해당 변수를 사용할 수있음
  });
});

// 조회2 - 글내용 조회
app.get('/topic/:id', function(req, res){
  var id = req.params.id;
  fs.readdir('data',function(err, files) {
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    fs.readFile('data/'+id, 'utf8', function(err, data){
      if(err){
        console.log(err);
        res.status(500).send('Internal Server Error');
      }
      res.render('view', {topics: files, title: id, description: data});
    });
  });
});
```

- 중복 제거 이후 코드
- 라우트는 배열로 여러개의 path를 가질 수 있다. [express 가이드](http://expressjs.com/ko/4x/api.html#app.get.method)


```javascript
// 조회 - 글목록 표시, 글내용
app.get(['/topic', '/topic/:id'], function(req, res) {
// 라우트는 배열로 여러개의 path를 가질 수 있음
  fs.readdir('data',function(err, files) {
    if(err){
      console.log(err);
      res.status(500).send('Internal Server Error');
    }
    var id = req.params.id;
    if(id){
      // id 값이 있을 때
      fs.readFile('data/'+id, 'utf8', function(err, data){
        if(err){
          console.log(err);
          res.status(500).send('Internal Server Error');
        }
        res.render('view', {topics: files, title: id, description: data});
      });
    }else{
      // id 값이 없을 때
      res.render('view', {topics:files, title:'welcome', description:'hello JS for server'});
    }
  });
});
```

### 스타일 통일
- 각 페이지의 (조회, 작성, 저장)의 스타일을 통일한다.

### 전체코드 링크
- [app_file.js](https://github.com/wayhome25/nodejs/blob/master/opentutorials/app_file.js)
- [jade file](https://github.com/wayhome25/nodejs/tree/master/opentutorials/views_file)
