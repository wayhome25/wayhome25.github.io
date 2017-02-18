---
layout: post
title: 콜백(Callback)
category: nodejs
tags: [nodejs, 콜백]
comments: true
---
# 콜백(Callback)
> [생활코딩 Node.js 강의](https://opentutorials.org/course/2136/11861)   
> 콜백함수에 대하여 알아본다.



- 터미널에서 `node` 만 입력하면, 터미널 내에서 직접 자바스크립트 코드를 실행 할 수 있다.
- 어떤 함수의 매개변수 인자로 함수가 주어졌을 때, 호출 당한 해당 함수를 콜백 함수라고 한다.
- 예시

```javascript
var a = [3, 1, 2];
function b(v1, v2){return v2-v1;}
a.sort(); // 오름차순으로 정렬됨 [1, 2, 3]
a.sort(b); // 콜백함수 b가 실행되어 정렬방식을 결정 [3, 2, 1]
console.log(a);  
```
