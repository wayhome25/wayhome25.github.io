---
layout: post
title: Nodejs 자동 재시작 패키지 - supervisor
category: nodejs
tags: [nodejs, Express, supervisor]
comments: true
---
# Nodejs를 자동으로 재시작 - supervisor
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11951)   
> 소스코드가 변경되었을 때 에플리케이션을 자동으로 재시작하는 방법을 알아본다.

## Supervisor
- nodejs 에서는 파일 수정시 터미널에서 `cmd+c(ctrl+c)`를 눌러 종료하고     
  `node 파일명(app.js)`을 입력하여 node를 다시 켜야하는 불편함이 있다.
- 이를 해결하기 위해서 [supervisor](https://www.npmjs.com/package/supervisor) 패키지를 사용할 수 있다.

### 설치
- 터미널에서 `npm install supervisor -g` 입력

### 사용
- 터미널에서 `supervisor 파일명(app.js)` 입력하면 이후 app.js의 수정사항이 자동으로 반영된다.
  (`node 파일명(app.js)` 의 입력을 대신한다.)
