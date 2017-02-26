---
layout: post
title: level 1. 행렬의 덧셈
category: 알고리즘 문제풀이
tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 행렬의 덧셈
> 출처 : http://tryhelloworld.co.kr/challenge_codes/9

## 문제

```
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬을 입력받는 sumMatrix 함수를 완성하여 행렬 덧셈의 결과를 반환해 주세요.

예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다.(어떠한 행렬에도 대응하는 함수를 완성해주세요.)
```

## 느낀 점
- 2차원 행렬을 만드는 것이 어려웠다.  
- .map() 메소드를 잘 활용하자. [참고](https://wayhome25.github.io/javascript/2017/02/17/js-method/)  
- 화살표 함수에 익숙해지자.[참고](https://wayhome25.github.io/javascript/2017/02/23/js-Arrow-functions/)

## 풀이 (Javascript)
```javascript
function sumMatrix(A,B){
	var answer = Array();
		for(var i = 0; i < A.length; i++){
      answer[i] = [];
      for(var j = 0; j < A[i].length; j++){
          answer[i][j] = A[i][j] + B[i][j];				
      }
		}
	return answer;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
```

## 다른사람 풀이
```javascript
function sumMatrix(A,B){
  return A.map((a,i) => a.map((b, j) => b + B[i][j]));
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

// 화살표 함수를 풀어 쓴 코드
function sumMatrix(A,B){
    return A.map(function(a, i){
             return a.map(function(b, j){
                     return b + B[i][j]
                   })
         })
}
```
