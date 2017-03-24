---
layout: post
title: level 1. 삼각형 출력하기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍, 자바스크립트]
comments: true
---
# level 1. 삼각형 출력하기
> 출처 : http://tryhelloworld.co.kr/challenge_codes/101

## 문제
printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.

```   
높이가 3일때

*
**
***
```

## 풀이

```javascript
function printTriangle(num) {
  var result = ''
  for(var i = 0; i < num; i++){
  	for(var j = 0; j <= i; j++){
    	result += '*'
    }
    result += '\n'
  }
  return result
}

```

## 다른사람 풀이
```javascript
function printTriangle(num) {
  var result = ''
  for(var i=num; i--;) {
    result += '*'.repeat(num-i) + '\n';
  }
  return result
}
```

## 배운점
- [str.repeat(count)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String/repeat) : 특정 스트링을 count 만큼 반복하여 리턴
