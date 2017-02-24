---
layout: post
title: javascript 코딩 스타일
category: javascript
tags: [javascript, 코딩스타일]
comments: true
---

# 자바스크립트 코딩 스타일
> 자주 사용되는 코딩 패턴에 대해서 알아본다. [참고 출처](http://blog.jui.io/?p=27)

## 변수 선언

### 수정 전
```javascript
var a = 10;
var b = 20;
var c = 30;
var d = 40;
```

### 수정 후
```javascript
var a = 10, b = 20, c = 30, d = 40;
// 변수의 유형이 다양한 경우
var a = 10
    , b = 20
    , c = 30
    , str = 'Hello, World'
    , arr = [ 1, 2, 3, 4, 5, 6 ];
```

## 띄어쓰기
<center>
<figure>
<img src="/assets/post-img/javascript/coding-pattern.jpg" alt="">
<figcaption>키워드별 띄어쓰기 (타 프로그래밍 언어 동일)</figcaption>
</figure>
</center>

## If 문 & Switch문 대체

### 수정 전
```javascript
function get(type) {
     if(type == 'todo') {
          return '할일';
     } else if(type == 'calendar') {
          return '달력';
     } else if(type == 'note') {
          return '공책';
     }
}

function get2(type) {
     var result = "";
     switch(type) {
          case 'todo':
          result = "할일";
          break;
          case 'calendar':
          result = "달력";
          break;
          case 'note':
          result = "공책";
          break;
     }

     return result;
}

alert(get('todo') + ", " + get2('note'));
```

### 수정 후 
```javascript

function get(type) {
     return {
          todo: '할일',
          calendar: '달력',
          note: '공책'
     }[type];
}

alert(get('todo'));
```
