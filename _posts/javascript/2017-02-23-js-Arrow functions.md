---
layout: post
title: 자바스크립트 화살표 함수
category: javascript
tags: [javascript, 함수, 화살표 함수]
comments: true
---

# 화살표 함수 (Arrow functions)

## 설명
화살표 함수 표현(arrow function expression)은 function 표현에 비해 구문이 짧고, 화살표 함수는 항상 익명입니다. 이 함수 표현은 메소드 함수가 아닌 곳에 가장 적당합니다. 그래서 생성자로서 사용할 수 없습니다.  [MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/%EC%95%A0%EB%A1%9C%EC%9A%B0_%ED%8E%91%EC%85%98)

## 문법
```javascript
(param1, param2, …, paramN) => { statements }
(param1, param2, …, paramN) => expression
// 다음과 동일함:  => { return expression; }

// 매개변수가 하나뿐인 경우 괄호는 선택사항:
(singleParam) => { statements }
singleParam => { statements }

// 매개변수가 없는 함수는 괄호가 필요:
() => { statements }
```

## 예시
일부 함수 패턴에서는, 짧은 함수가 효율적이다. a2, a3의 결과는 같다.

```javascript
var a = [
  "Hydrogen",
  "Helium",
  "Lithium",
  "Beryl­lium"
];

var a2 = a.map(function(s){ return s.length });

var a3 = a.map( s => s.length );
```
