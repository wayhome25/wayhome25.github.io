---
layout: post
title: level 1. 문자열 다루기 기본
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍, 자바스크립트]
comments: true
---
# level 1. 문자열 다루기 기본
> 출처 : http://tryhelloworld.co.kr/challenge_codes/99#

## 문제
alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.
s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.
예를들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다


## 풀이
```javascript
function alpha_string46(s){
  var result
	// result = (s.length === 4 || s.length === 6) && !isNaN(s) : true : false;
  if((s.length === 4 || s.length === 6) && !isNaN(s)){
  	result = true
  } else
    result = false
  return result;
}
```

## 다른사람 풀이
```javascript
function alpha_string46(s){
  var result = false;
  if((s.length == 4 || s.length == 6) && /^[0-9]+$/.test(s)) {
    result = true;
  }

  return result;
}

```

## 배운점
- [정규표현식 익히자](https://opentutorials.org/course/909/5142)
