---
layout: post
title: 동기와 비동기 프로그래밍 (Asynchronous-synchronous)
category: nodejs
tags: [nodejs, 비동기, async, ajax]
comments: true
---
# 동기와 비동기 프로그래밍
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11884)   
> 노드 프로그래밍의 핵심인 비동기적인 프로그래밍에 대한 개요를 살펴본다.

## 간단한 정의
- 줄임말 : sync(동기) / Async(비동기)
- 동기적 일처리 방식 : 순차적으로 일을 스스로 끝내 나가는 방식
- 비동기적 일처리 방식 : 해야 할 일을 위임하고 기다리는 방식

## 예시(nodejs)
- nodejs 사이트 doc에서 [filse system](https://nodejs.org/dist/latest-v6.x/docs/api/fs.html#fs_fs_readdirsync_path_options) 모듈 참고
- filse system 모듈은 nodejs를 이용해서 file을 제어하는 것과 관련된 기능
- nodejs 기본적으로 시간이 필요한 작업들 (IO가 필요한 작업) 비동기 적으로 처리

### 동기적 방식 - 코드
```javascript
var fs = require('fs');
console.log(1); // 실행순서 1
var data = fs.readFileSync('data.txt', {encoding: 'utf8'});
console.log(data); // 실행순서 2, 만약 data 파일이 처리가 오래 걸린다면 동기적 방식에서는 그동안 다른 작업을 할 수 없음 
console.log(3); // 실행순서 3
```
### 동기적 방식 - 결과
```
1
Hello sync and async
```

### 비동기적 방식 - 코드
```javascript
var fs = require('fs');
console.log(2); // 실행순서 1
fs.readFile('data.txt', {encoding: 'utf8'}, function(err, data){
  console.log(3); // 실행순서 3
  console.log(data); // 실행순서 4
})
console.log(4); // 실행순서 2
```

### 비동기적 방식 - 결과
```
2
4
3
Hello sync and async
```
